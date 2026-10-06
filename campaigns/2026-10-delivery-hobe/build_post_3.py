import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R='/home/user/brandasset/'
SP='/tmp/claude-0/-home-user-brandasset/d264e1ec-edf2-5cf5-9cbc-793486275170/scratchpad/'
IMG='/tmp/claude-0/-home-user-brandasset/d264e1ec-edf2-5cf5-9cbc-793486275170/images/2.png'
PK=(255,98,155);GD=(255,213,109);CO=(69,0,1);WH=(255,255,255)
W,H,FL=1080,1350,985
F=lambda n,s:ImageFont.truetype(R+'assets/fonts/web/'+n,s)
# --- set: cyan wall with soft pool of light, pale ice-blue floor
yy,xx=np.mgrid[0:H,0:W]
r=np.sqrt(((xx-600)/700)**2+((yy-480)/600)**2); t=np.clip(r,0,1)[...,None]
wall=(np.array([120,255,252])*(1-t)+np.array([4,222,232])*t)
fy=np.clip((yy-FL)/(H-FL),0,1)[...,None]
floor=np.array([214,243,250])*(1-fy)+np.array([176,226,240])*fy
img=np.where((yy<FL)[...,None],wall,floor).astype('uint8')
cv=Image.fromarray(img).convert('RGBA'); d=ImageDraw.Draw(cv)
d.rectangle((0,FL-5,W,FL),fill=(255,255,255))   # crisp wall/floor seam
# --- hero cutout (real photo, background removed)
cut=Image.open(SP+'cut.png').convert('RGBA').crop((0,30,675,1145))
sc=0.80; cut=cut.resize((int(cut.width*sc),int(cut.height*sc)),Image.LANCZOS)
wx,wy=330,150
# hard cast shadow on the floor: flattened + sheared silhouette
al=cut.split()[3]; sw,sh_=al.size
fl=al.resize((sw,int(sh_*0.17)),Image.LANCZOS)
fl=fl.transform((fl.width+260,fl.height),Image.AFFINE,(1,-1.1,0,0,1,0),Image.BICUBIC)
fl=fl.filter(ImageFilter.GaussianBlur(3)).point(lambda v:int(v*0.55))
shad=Image.new('RGBA',fl.size,CO+(255,)); shad.putalpha(fl)
cv.alpha_composite(shad,(wx-40,FL+45))
# soft contact/drop shadow on the wall behind
dsh=Image.new('RGBA',cut.size,CO+(255,)); dsh.putalpha(al.point(lambda v:int(v*0.22)))
cv.alpha_composite(dsh,(wx+22,wy+26))
cv.alpha_composite(cut,(wx,wy))
# --- logo
lg=Image.open(R+'assets/logo/Waffle Up Logo - RBG.png').convert('RGBA'); lg=lg.crop(lg.split()[3].getbbox())
lg=lg.resize((330,int(lg.height*330/lg.width)),Image.LANCZOS); cv.alpha_composite(lg,(60,60))
# --- Delivery Hobe badge (supplied logo), hexagon cut + hard shadow
hx=Image.open(IMG).convert('RGB').crop((25,20,435,425)).convert('RGBA')
px=np.array(hx.convert('RGB')).astype(int)
isred=((px[:,:,0]>180)&(px[:,:,1]<110)&(px[:,:,2]<110)).astype('uint8')*255
f2=Image.fromarray(np.dstack([isred]*3)); ImageDraw.floodfill(f2,(2,2),(0,255,0))
f_=np.array(f2); outside=(f_[:,:,1]==255)&(f_[:,:,0]==0)
hm=Image.fromarray(((~outside)*255).astype('uint8')).filter(ImageFilter.GaussianBlur(0.8))
bb=hm.getbbox(); hx=hx.crop(bb); hm=hm.crop(bb)
hw=360; hx=hx.resize((hw,int(hx.height*hw/hx.width)),Image.LANCZOS); hm=hm.resize(hx.size,Image.LANCZOS)
bx,by=60,330
s2=Image.new('RGBA',hx.size,CO+(255,)); cv.paste(s2,(bx+14,by+14),hm); cv.paste(hx,(bx,by),hm)
d.text((bx+8,by-72),'NOW ON',font=F('BebasNeue.otf',64),fill=CO)
# --- type on the floor
def hero(txt,xy,size,fill,anchor='la'):
    f=F('FuturaExtraBold.otf',size)
    d.text((xy[0]+8,xy[1]+8),txt,font=f,fill=CO,stroke_width=8,stroke_fill=CO,anchor=anchor)
    d.text(xy,txt,font=f,fill=fill,stroke_width=8,stroke_fill=WH,anchor=anchor)
hero('JOY TRAVELS.',(W//2,1090),122,PK,'ma')
d.text((W//2,1272),'WAFFLES ON A STICK. NOW ON DELIVERY HOBE.',font=F('BebasNeue.otf',46),fill=CO,anchor='ma')
cv.convert('RGB').save(R+'output/delivery-hobe-launch-v3-4x5.png')
