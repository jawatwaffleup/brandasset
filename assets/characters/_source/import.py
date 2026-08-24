# -*- coding: utf-8 -*-
"""
Import Jeremy Lord's character masters from a mounted Google Drive into this tree.

Usage:
    python import.py "G:/My Drive/WaffleUp_ jeremy"          # everything except CMYK
    python import.py "G:/My Drive/WaffleUp_ jeremy" --cmyk   # include the 2.2 GB print set
    python import.py "G:/My Drive/WaffleUp_ jeremy" --dry-run

Matches files by basename against manifest.json, so it does not care how Drive
lays the folders out locally. Renames everything to brand names on the way in
(popsicle -> icy, Spacie -> spacy, Stovie -> stovy, TV -> tvy, merlion -> merlulu).

Re-runnable: files already present with the right size are skipped.
"""
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Exact Drive filename -> path relative to this directory.
SPECIAL = {
    "family.ai":                 "vector-masters/family.ai",
    "merlion 02.ai":             "merlulu/merlulu.ai",
    "merlion 02.psd":            "merlulu/merlulu.psd",
    "type.ai":                   "typography/type.ai",
    "type flat.ai":              "typography/type-flat.ai",
    "WU group tee redux.ai":     "apparel/wu-group-tee-redux.ai",
    "expressions.jpg":           "reference/expressions-sheet.jpg",
    "waffle revolution copy.jpg": "reference/waffle-revolution.jpg",
}


def target_for(rec):
    """Return the path relative to HERE for a manifest record, or None to skip."""
    title, group, char, pose = rec["title"], rec["group"], rec["char"], rec["pose"]

    if title in SPECIAL:
        return SPECIAL[title]
    if title == ".DS_Store":
        return None

    if group == "chars":
        if title.endswith(".ai"):
            return "vector-masters/%s.ai" % char
        if "T pose" in title:
            return "t-poses/%s-t-pose.psd" % char
    if group == "facial":
        return "expressions/%s-expressions.psd" % char
    if group == "rgb" and pose:
        return "poses-rgb/%s/%s-%s.psd" % (char, char, pose)
    if group == "cmyk" and pose:
        return "poses-cmyk/%s/%s-%s-cmyk.psd" % (char, char, pose)
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = set(a for a in sys.argv[1:] if a.startswith("--"))
    if not args:
        print(__doc__)
        return 1

    src_root = args[0]
    if not os.path.isdir(src_root):
        print("Source not found: %s" % src_root)
        print("Is Drive for Desktop mounted, and the folder added to My Drive?")
        return 1

    dry = "--dry-run" in flags
    want_cmyk = "--cmyk" in flags

    manifest = json.load(open(os.path.join(HERE, "manifest.json"), encoding="utf-8"))
    records = manifest["files"]

    # Index every file on disk under the source root by basename.
    on_disk = {}
    for dirpath, _dirnames, filenames in os.walk(src_root):
        for fn in filenames:
            on_disk.setdefault(fn, os.path.join(dirpath, fn))

    copied = skipped = missing = 0
    copied_bytes = 0
    absent = []

    for rec in records:
        if rec["group"] == "cmyk" and not want_cmyk:
            continue
        rel = target_for(rec)
        if rel is None:
            continue

        src = on_disk.get(rec["title"])
        if src is None:
            missing += 1
            absent.append(rec["title"])
            continue

        dst = os.path.join(HERE, rel)
        if os.path.exists(dst) and os.path.getsize(dst) == rec["size"]:
            skipped += 1
            continue

        print("%s  ->  %s" % (rec["title"], rel))
        if not dry:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
        copied += 1
        copied_bytes += rec["size"]

    print("")
    print("copied %d (%.1f MB)   already present %d   not found in source %d"
          % (copied, copied_bytes / 1048576.0, skipped, missing))
    if absent:
        print("")
        print("Not found under %s:" % src_root)
        for t in absent[:20]:
            print("  - %s" % t)
        if len(absent) > 20:
            print("  ... and %d more" % (len(absent) - 20))
    if not want_cmyk:
        print("")
        print("CMYK print set skipped (2.2 GB). Re-run with --cmyk if a printer needs it.")
    if dry:
        print("")
        print("DRY RUN - nothing was written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
