"""Replace the AI waffles in the Delivery Hobe red post with real square waffles (Nutella product photo cutout)."""
import cv2, numpy as np
from PIL import Image
S='/tmp/claude-0/-home-user-brandasset/d264e1ec-edf2-5cf5-9cbc-793486275170/scratchpad/'
base=cv2.cvtColor(cv2.imread(S+'g1.png'),cv2.COLOR_BGR2RGB)
base=cv2.resize(base,(1080,1080),interpolation=cv2.INTER_AREA).astype(float)
H,W=base.shape[:2]; R_,G_,B_=base[:,:,0],base[:,:,1],base[:,:,2]
yy,xx=np.mgrid[0:H,0:W]
# red-field model (quadratic fit) used to repaint the erased area
red=(R_-G_>70)&(G_<70)&(B_<80)
inner=(yy>425)&(yy<900)&(xx>80)&(xx<1000)
outer=(yy>270)&(yy<1010)&(xx>0)&(xx<1080)
fit=red&~inner&outer&(yy<880)
u=xx.ravel()/W; v=yy.ravel()/H
X=np.stack([np.ones(H*W),u,v,u*u,v*v,u*v,u**3,v**3,u*u*v,u*v*v],1)
idx=np.flatnonzero(fit.ravel())[::3]; bg=np.zeros_like(base)
for c in range(3):
    bg[:,:,c]=(X@np.linalg.lstsq(X[idx],base[:,:,c].ravel()[idx],rcond=None)[0]).reshape(H,W)
bg=np.clip(bg,0,255)
# erase mask: old waffles, keep hearts/sparks, badge and the old stick tops
prot=[(135,393,243,519),(75,513,180,633),(885,495,1011,651),(955,643,1062,753)]
nonred=~((R_-G_>55)&(G_<80)&(B_<95))
box=np.zeros((H,W),bool); box[425:900,100:965]=True; box[425:474,425:695]=False
old=(nonred&box).astype('uint8')
old=cv2.morphologyEx(old,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
cnt,_=cv2.findContours(old,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
fill=np.zeros_like(old)
for c in cnt:
    if cv2.contourArea(c)>3000: cv2.drawContours(fill,[c],-1,1,-1)
pl=np.zeros_like(fill)
for q in [[(265,435),(545,505),(460,875),(130,770)],[(540,505),(835,438),(945,785),(650,888)]]: cv2.fillPoly(pl,[np.array(q,np.int32)],1)
fill=np.maximum(fill,pl)
er=cv2.dilate(fill,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(61,61)))>0
for x0,y0,x1,y1 in prot: er[y0:y1,x0:x1]=False
er[845:900,215:325]=False; er[845:900,735:865]=False
er[820:890,590:660]=True
er[900:,:]=False
a=cv2.GaussianBlur(er.astype('float32'),(0,0),5)[...,None]
out=base*(1-a)+bg*a

# --- continuous stick section: plain wood strip from the real waffle shoot, runs under the waffle and under the engraved stick
strip=cv2.imread(S+'stick_strip.png')
def stick_piece(out,top,ang_deg,width=56,length=90):
    st=cv2.resize(strip,(width,length),interpolation=cv2.INTER_AREA)
    tile=np.zeros((length+40,width+40,4),np.uint8); tile[20:20+length,20:20+width,:3]=st; tile[20:20+length,20:20+width,3]=255
    # rotate about the strip's top-centre; ang>0 is ccw in cv2 (left stick leans bottom-left => clockwise => negative)
    M=cv2.getRotationMatrix2D((20+width/2,20),ang_deg,1.0)
    M[0,2]+=top[0]-(20+width/2); M[1,2]+=top[1]-20
    w=cv2.warpAffine(tile,M,(W,H),flags=cv2.INTER_LINEAR,borderValue=(0,0,0,0))
    al=cv2.GaussianBlur(w[:,:,3].astype(np.float32)/255,(0,0),0.8)
    fade=np.clip((868-np.arange(H))/16.,0,1)[:,None]; al=(al*fade)[...,None]   # only fills the gap; the engraved stick takes over below
    rgb=cv2.cvtColor(w[:,:,:3],cv2.COLOR_BGR2RGB).astype(float)
    return out*(1-al)+rgb*al
p0=eval(open(S+'params.txt').read())
out=stick_piece(out,(288,828),-p0['L'][2])
out=stick_piece(out,(797,836), p0['R'][2])
# real waffle cutout
cut=cv2.imread(S+'tri.png',cv2.IMREAD_UNCHANGED)     # Higgsfield tri-chocolate waffle, chroma-keyed, squared 1:1
cx,bot,bw=eval(open(S+'tri_anchor.txt').read())
cut=cut[:int(bot)+6]; ANCHOR=(cx,bot-14); LEAN=0.
WA=np.zeros((H,W),np.float32)
def place(out,target,lean_t,scale,mirror):
    global WA
    c=cut[:,::-1].copy() if mirror else cut
    ax=(c.shape[1]-ANCHOR[0]) if mirror else ANCHOR[0]
    ang=(lean_t-LEAN) if mirror else -(lean_t-LEAN)      # cv2: +ccw
    M=cv2.getRotationMatrix2D((ax,ANCHOR[1]),ang,scale)
    M[0,2]+=target[0]-ax; M[1,2]+=target[1]-ANCHOR[1]
    w=cv2.warpAffine(c,M,(W,H),flags=cv2.INTER_LANCZOS4,borderValue=(0,0,0,0))
    rgb=cv2.cvtColor(w[:,:,:3],cv2.COLOR_BGR2RGB).astype(float); al=(w[:,:,3:]/255.)
    WA=np.maximum(WA,al[:,:,0].astype(np.float32))
    return out*(1-al)+rgb*al
p=eval(open(S+'params.txt').read())
out=place(out,p['L'][0],p['L'][2],p['L'][1],False)
out=place(out,p['R'][0],p['R'][2],p['R'][1],True)
# everything below the seam comes straight from the generated post (hands + sticks)
tan=(R_>150)&(R_-B_>40)&(G_>80)&~((R_>200)&(G_>170)&(B_>150))
keep=tan&(yy>=840); keep=cv2.dilate(keep.astype('uint8'),np.ones((3,3),np.uint8))
keep=cv2.morphologyEx(keep,cv2.MORPH_OPEN,np.ones((5,5),np.uint8)).astype('float32')
keep=cv2.GaussianBlur(keep,(0,0),1.2)[...,None]
# only hands + old stick tops come back from the generated post; red field stays modelled
keep[:, :]=keep; keep[820:890,590:660]=0
keep=keep*(1-WA[...,None])
out=out*(1-keep)+base*keep
cv2.imwrite(S+'red_tri.png',cv2.cvtColor(np.clip(out,0,255).astype('uint8'),cv2.COLOR_RGB2BGR))
