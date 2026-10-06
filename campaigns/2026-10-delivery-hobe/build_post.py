import numpy as np
from PIL import Image, ImageDraw, ImageFont
R='/home/user/brandasset/'
IMG='/tmp/claude-0/-home-user-brandasset/d264e1ec-edf2-5cf5-9cbc-793486275170/images/2.png'  # supplied Delivery Hobe logo
RED=(234,51,35);PK=(255,98,155);GD=(255,213,109);CO=(69,0,1);WH=(255,255,255)
W,H,BAND=1080,1350,300
F=lambda n,s:ImageFont.truetype(R+'assets/fonts/web/'+n,s)
# photo: scale, crop around product, extend flat backdrop sideways
ph=Image.open(R+'assets/marketing/product-hero/03-woas-tri-chocolate.jpg').convert('RGB')
sc=1.5; ph=ph.resize((int(ph.width*sc),int(ph.height*sc)),Image.LANCZOS)
top=int(430*sc); ph=ph.crop((0,top,ph.width,top+(H-BAND)))
a=np.array(ph); pad=(W-ph.width)//2
a=np.pad(a,((0,0),(pad,W-ph.width-pad),(0,0)),mode='reflect')
cv=Image.new('RGB',(W,H)); cv.paste(Image.fromarray(a),(0,0)); d=ImageDraw.Draw(cv)
# red band
d.rectangle((0,H-BAND,W,H),fill=RED)
d.rectangle((0,H-BAND-8,W,H-BAND),fill=CO)
# logo
lg=Image.open(R+'assets/logo/Waffle Up Logo - RBG.png').convert('RGBA'); lg=lg.crop(lg.split()[3].getbbox())
lg=lg.resize((340,int(lg.height*340/lg.width)),Image.LANCZOS); cv.paste(lg,(60,64),lg)
# Delivery Hobe hex (white, keyed from supplied logo)
hx=Image.open(IMG).convert('RGB').crop((25,20,435,425))
al=hx.split()[1].point(lambda v:0 if v<90 else min(255,(v-90)*255//120))
wh=Image.new('RGBA',hx.size,WH+(255,)); wh.putalpha(al); wh=wh.crop(wh.getbbox())
hw=240; wh=wh.resize((hw,int(wh.height*hw/wh.width)),Image.LANCZOS)
cv.paste(wh,(60,H-BAND+(BAND-wh.height)//2+4),wh)
# copy
x=370; cy=H-BAND//2
d.text((x,cy-62),'WAFFLES ON A STICK.',font=F('BebasNeue.otf',72),fill=WH,anchor='lm')
d.text((x,cy+14),'NOW ON DELIVERY HOBE.',font=F('BebasNeue.otf',72),fill=GD,anchor='lm')
d.text((x,cy+80),'SQUARE IS THE NEW HEART',font=F('BebasNeue.otf',36),fill=WH,anchor='lm')
cv.save(R+'output/delivery-hobe-launch-4x5.png')
