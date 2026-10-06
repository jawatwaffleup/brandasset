from PIL import Image, ImageDraw, ImageFont, ImageChops
R='/home/user/brandasset/'
IMG='/tmp/claude-0/-home-user-brandasset/d264e1ec-edf2-5cf5-9cbc-793486275170/images/2.png'
RED=(234,51,35);CY=(11,249,246);PK=(255,98,155);GD=(255,213,109);CO=(69,0,1);WH=(255,255,255)
W,H=1080,1350
cv=Image.new('RGB',(W,H),RED)
d=ImageDraw.Draw(cv)
F=lambda n,s:ImageFont.truetype(R+'assets/fonts/web/'+n,s)
# logo
lg=Image.open(R+'assets/logo/Waffle Up Logo - RBG.png').convert('RGBA'); lg=lg.crop(lg.split()[3].getbbox())
lw=400; lg=lg.resize((lw,int(lg.height*lw/lg.width)),Image.LANCZOS)
cv.paste(lg,((W-lw)//2,70),lg)
# hex (white, keyed from supplied Delivery Hobe logo)
hx=Image.open(IMG).convert('RGB').crop((25,20,435,425))
a=hx.convert('L').point(lambda v:255 if v>235 else max(0,(v-150)*255//85) if v>150 else 0)
# keep red out: use min channel (white has high G/B)
a=hx.split()[1].point(lambda v:0 if v<90 else min(255,(v-90)*255//120))
wh=Image.new('RGBA',hx.size,WH+(255,)); wh.putalpha(a)
wh=wh.crop(wh.getbbox())
def hexat(w):
    return wh.resize((w,int(wh.height*w/wh.width)),Image.LANCZOS)
# headline: shadow, outline, fill
def hero(txt,xy,size,anchor='la'):
    f=F('FuturaExtraBold.otf',size)
    d.text((xy[0]+9,xy[1]+9),txt,font=f,fill=CO,anchor=anchor,stroke_width=10,stroke_fill=CO)
    d.text(xy,txt,font=f,fill=GD,anchor=anchor,stroke_width=10,stroke_fill=WH)
hero('JOY TRAVELS.',(W//2,215),112,'ma')
# photo panel
ph=Image.open(R+'assets/marketing/product-hero/03-woas-tri-chocolate.jpg').convert('RGB')
pw,pht=520,760
s=pw/ph.width; ph=ph.resize((pw,int(ph.height*s)),Image.LANCZOS)
ph=ph.crop((0,150,pw,150+pht))
px,py=500,400
m=Image.new('L',(pw,pht),0); ImageDraw.Draw(m).rounded_rectangle((0,0,pw-1,pht-1),40,fill=255)
d.rounded_rectangle((px+16,py+16,px+pw+16,py+pht+16),40,fill=CO)
cv.paste(ph,(px,py),m)
d.rounded_rectangle((px,py,px+pw,py+pht),40,outline=WH,width=8)
# left column
d.text((60,400),'WAFFLES ON',font=F('BebasNeue.otf',92),fill=WH)
d.text((60,490),'A STICK.',font=F('BebasNeue.otf',92),fill=WH)
d.rounded_rectangle((60,610,440,700),20,fill=PK)
d.text((250,655),'NOW ON',font=F('BebasNeue.otf',64),fill=WH,anchor='mm')
hb=hexat(360)
cv.paste(hb,(60,730),hb)
# CTA
d.rounded_rectangle((60+8,1190+8,W-60+8,1290+8),50,fill=CO)
d.rounded_rectangle((60,1190,W-60,1290),50,fill=CY)
d.text((W//2,1240),'ORDER ON DELIVERY HOBE',font=F('BebasNeue.otf',78),fill=CO,anchor='mm')
d.text((W//2,1322),'SQUARE IS THE NEW HEART',font=F('BebasNeue.otf',34),fill=WH,anchor='mm')
cv.save(R+'output/delivery-hobe-launch-4x5.png')
