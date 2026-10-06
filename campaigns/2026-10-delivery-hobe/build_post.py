import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R='/home/user/brandasset/'
IMG='/tmp/claude-0/-home-user-brandasset/d264e1ec-edf2-5cf5-9cbc-793486275170/images/2.png'  # supplied Delivery Hobe logo
PK=(255,98,155);GD=(255,213,109);CO=(69,0,1);WH=(255,255,255)
W,H=1080,1350
F=lambda n,s:ImageFont.truetype(R+'assets/fonts/web/'+n,s)
# --- hero photo (real), extended downward with its own backdrop gradient
ph=Image.open(R+'assets/marketing/product-hero/02-woas-red-velvet.jpg').convert('RGB').crop((0,0,1200,1075))
ph=ph.resize((W,int(1075*W/1200)),Image.LANCZOS)
row=np.array(ph.crop((0,ph.height-6,W,ph.height)).filter(ImageFilter.GaussianBlur(25)))[3:4]
row=np.array(Image.fromarray(np.repeat(row,40,axis=0)).filter(ImageFilter.GaussianBlur(70)))[20:21]
ext=np.repeat(row,H-ph.height,axis=0)
cv=Image.new('RGB',(W,H)); cv.paste(ph,(0,0)); cv.paste(Image.fromarray(ext),(0,ph.height))
# soften seam
m=Image.new('L',(W,60),0)
for y in range(60): ImageDraw.Draw(m).line((0,y,W,y),fill=int(255*y/60))
cv.paste(Image.fromarray(ext[:60]),(0,ph.height-60),m)
d=ImageDraw.Draw(cv)
# --- logo (supplied file)
lg=Image.open(R+'assets/logo/Waffle Up Logo - RBG.png').convert('RGBA'); lg=lg.crop(lg.split()[3].getbbox())
lg=lg.resize((330,int(lg.height*330/lg.width)),Image.LANCZOS); cv.paste(lg,(60,64),lg)
# --- Delivery Hobe badge (supplied logo, red field kept) with hard cocoa shadow
hx=Image.open(IMG).convert('RGB').crop((25,20,435,425)).convert('RGBA')
px=np.array(hx.convert('RGB')).astype(int)
isred=((px[:,:,0]>180)&(px[:,:,1]<110)&(px[:,:,2]<110)).astype('uint8')*255
fl=Image.fromarray(np.dstack([isred]*3))
ImageDraw.floodfill(fl,(2,2),(0,255,0))
outside=np.array(fl)[:,:,1]==255
outside&=np.array(fl)[:,:,0]==0
hexm=Image.fromarray(((~outside)*255).astype('uint8')).filter(ImageFilter.GaussianBlur(0.8))
bb=hexm.getbbox(); hx=hx.crop(bb); hexm=hexm.crop(bb)
hw=270; hx=hx.resize((hw,int(hx.height*hw/hx.width)),Image.LANCZOS); hexm=hexm.resize(hx.size,Image.LANCZOS)
bx,by=735,720
sh=Image.new('RGBA',hx.size,CO+(255,)); cv.paste(sh,(bx+14,by+14),hexm)
cv.paste(hx,(bx,by),hexm)
# --- hero type: shadow -> outline -> fill
def hero(txt,xy,size,fill):
    f=F('FuturaExtraBold.otf',size)
    d.text((xy[0]+7,xy[1]+7),txt,font=f,fill=CO,stroke_width=7,stroke_fill=CO)
    d.text(xy,txt,font=f,fill=fill,stroke_width=7,stroke_fill=WH)
hero('SQUARE IS THE',(60,1000),100,PK)
hero('NEW HEART',(60,1110),100,PK)
d.text((60,1262),'WAFFLES ON A STICK. NOW ON DELIVERY HOBE.',font=F('BebasNeue.otf',50),fill=CO)
cv.save(R+'output/delivery-hobe-launch-4x5.png')
