/// WaffleUp Design Tokens — Flutter  ·  v1.0.0
/// Generated from tokens/wup-tokens.json. Do not hand-edit; edit the JSON.
library wup_tokens;

import 'package:flutter/material.dart';

class WupColors {
  static const cyan  = Color(0xFF0BF9F6);
  static const pink  = Color(0xFFFF629B);
  static const gold  = Color(0xFFFFD56D);
  static const cocoa = Color(0xFF450001); // ink — never use black
  static const white = Color(0xFFFFFFFF);

  static const cyan100 = Color(0xFFDFFEFD);
  static const cyan700 = Color(0xFF06B5B3);
  static const pink100 = Color(0xFFFFE7EF);
  static const pink700 = Color(0xFFD93C74);
  static const gold100 = Color(0xFFFFF6E2);
  static const gold700 = Color(0xFFE0AE38);
  static const cocoa300 = Color(0xFFA56A6B);

  static const success = Color(0xFF1FBF6B);
  static const warning = gold700;
  static const danger  = pink700;
  static const info    = cyan700;

  /// Correct text colour to place on a brand field.
  static Color on(Color bg) =>
      (bg == pink || bg == cocoa) ? white : cocoa;
}

class WupType {
  static const display   = 'CHUM';
  static const headline  = 'Futura';
  static const condensed = 'BebasNeue';
  static const body      = 'GeneralSans';
  static const bangla    = 'NotoSansBengali';
}

class WupShape {
  static const double radiusSm = 8;
  static const double radius   = 16;
  static const double radiusLg = 28;
  static const double stroke   = 3;
  static const double touchMin = 48; // staff use phones one-handed
}

class WupSpace {
  static const double s1 = 4, s2 = 8, s3 = 12, s4 = 16, s5 = 24, s6 = 32, s7 = 48, s8 = 64;
}

/// Base theme. Sticker shape language: rounded, cocoa outline, hard offset shadow.
ThemeData wupTheme() => ThemeData(
      useMaterial3: true,
      scaffoldBackgroundColor: WupColors.white,
      fontFamily: WupType.body,
      colorScheme: const ColorScheme.light(
        primary: WupColors.pink,
        onPrimary: WupColors.white,
        secondary: WupColors.cyan,
        onSecondary: WupColors.cocoa,
        tertiary: WupColors.gold,
        onTertiary: WupColors.cocoa,
        surface: WupColors.white,
        onSurface: WupColors.cocoa,
        error: WupColors.danger,
      ),
      textTheme: const TextTheme(
        displayLarge: TextStyle(fontFamily: WupType.display, color: WupColors.cocoa),
        headlineLarge: TextStyle(fontFamily: WupType.headline, color: WupColors.cocoa),
        bodyMedium: TextStyle(color: WupColors.cocoa),
      ),
      cardTheme: CardTheme(
        color: WupColors.white,
        elevation: 0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(WupShape.radius),
          side: const BorderSide(color: WupColors.cocoa, width: WupShape.stroke),
        ),
      ),
      filledButtonTheme: FilledButtonThemeData(
        style: FilledButton.styleFrom(
          backgroundColor: WupColors.gold,
          foregroundColor: WupColors.cocoa,
          minimumSize: const Size(WupShape.touchMin, WupShape.touchMin),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(999),
            side: const BorderSide(color: WupColors.cocoa, width: WupShape.stroke),
          ),
        ),
      ),
    );

/// Format money the WaffleUp way: whole taka, no decimals.
String bdt(num amount, {bool symbol = false}) {
  final n = amount.round().toString();
  return symbol ? '৳$n' : 'BDT $n';
}
