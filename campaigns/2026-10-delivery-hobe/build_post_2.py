import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R='/home/user/brandasset/'
SP='/tmp/claude-0/-home-user-brandasset/d264e1ec-edf2-5cf5-9cbc-793486275170/scratchpad/'
IMG='/tmp/claude-0/-home-user-brandasset/d264e1ec-edf2-5cf5-9cbc-793486275170/images/2.png'
PK=(255,98,155);GD=(255,213,109);CO=(69,0,1);WH=(255,255,255)
W,H=1080,1350
F=lambda n,s:ImageFont.truetype(R+'assets/fonts/web/'+n,s)
# backdrop: brand wave pattern crop
pt=Image.open(R+'assets/pattern/Brand-Pattern.jpg').convert('RGB')
X0=int(__import__('sys').argv[1]) if len(__import__('sys').argv)>1 else 700
cw=int(pt.height*W/H); bg=pt.crop((X0,0,X0+cw,pt.height)).resize((W,H),Image.LANCZOS)
cv=bg.convert('RGBA'); d=ImageDraw.Draw(cv)
# logo
lg=Image.open(R+'assets/logo/Waffle Up Logo - RBG.png').convert('RGBA'); lg=lg.crop(lg.split()[3].getbbox())
lg=lg.resize((330,int(lg.height*330/lg.width)),Image.LANCZOS); cv.alpha_composite(lg,(60,60))
# hero type
def hero(txt,xy,size,fill):
    f=F('FuturaExtraBold.otf',size)
    d.text((xy[0]+9,xy[1]+9),txt,font=f,fill=CO,stroke_width=8,stroke_fill=CO)
    d.text(xy,txt,font=f,fill=fill,stroke_width=8,stroke_fill=WH)
hero('JOY',(60,185),160,GD); hero('TRAVELS.',(60,330),160,GD)
# waffle cutout (real photo, background removed)
cut=Image.open(SP+'cut.png').convert('RGBA'); cut=cut.crop((0,30,675,1145))
sc=0.84; cut=cut.resize((int(cut.width*sc),int(cut.height*sc)),Image.LANCZOS)
wx,wy=420,395
# hard cocoa shadow (offset silhouette)
sh=Image.new('RGBA',cut.size,CO+(255,)); sh.putalpha(cut.split()[3].point(lambda v:int(v*0.9)))
cv.alpha_composite(sh,(wx+26,wy+30)); cv.alpha_composite(cut,(wx,wy))
# Delivery Hobe badge
hx=Image.open(IMG).convert('RGB').crop((25,20,435,425)).convert('RGBA')
px=np.array(hx.convert('RGB')).astype(int)
isred=((px[:,:,0]>180)&(px[:,:,1]<110)&(px[:,:,2]<110)).astype('uint8')*255
fl=Image.fromarray(np.dstack([isred]*3)); ImageDraw.floodfill(fl,(2,2),(0,255,0))
f_=np.array(fl); outside=(f_[:,:,1]==255)&(f_[:,:,0]==0)
hm=Image.fromarray(((~outside)*255).astype('uint8')).filter(ImageFilter.GaussianBlur(0.8))
bb=hm.getbbox(); hx=hx.crop(bb); hm=hm.crop(bb)
hw=330; hx=hx.resize((hw,int(hx.height*hw/hx.width)),Image.LANCZOS); hm=hm.resize(hx.size,Image.LANCZOS)
bx,by=60,H-60-hx.height-10
s2=Image.new('RGBA',hx.size,CO+(255,)); cv.paste(s2,(bx+14,by+14),hm); cv.paste(hx,(bx,by),hm)
d.text((bx+6,by-70),'NOW ON',font=F('BebasNeue.otf',64),fill=CO)
cv.convert('RGB').save(R+'output/delivery-hobe-launch-v2-4x5.png')
