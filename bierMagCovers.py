# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#
#     P A G E B O T
#
#     Free to use. Licensed under MIT conditions
#
#     Supporting usage of DrawBot, www.drawbot.com
#     Supporting usage of Flat, https://github.com/xxyxyz/flat
# -----------------------------------------------------------------------------
#
#     publications.py
#
from pagebot.contexts import defaultContext as context
from pagebot.fonttoolbox.objects.font import getFontByName
from pagebot.style import A4, CENTER, DISPLAY_BLOCK, RIGHT, LEFT
from pagebot import Gradient, Shadow
from pagebot.toolbox.dating import now

shadow = Shadow(offset=(6, -6), blur=10, color=(0.2, 0.2, 0.2, 0.5))

W, H = A4[0]*3/4, A4[1]*3/4

TYPETR_COLOR = [0x1D/255, 0x42/255, 0x9A/255]


def buildCoverPages1(w, h, imagePath, page):
	
    magazineTitle = 'Bier!'

    M = 10 # Margin
    ML, MR, MT, MB = M, M, M, 1.5*M
    cw = w-ML-MR
    LM = 2*M
    
    # Page 66
    context.newPage(w, h) 
    
    biw, bih = ((None, h), (w, None), (None, h), (None, h))[page]
    # Draw image, covering all page, scaled.
    context.image('docs/images/'+imagePath, (0, 0), w=biw, h=bih)

    t = (
        u'Voorjaar 2018 | No. 36 | €5',  
        u'Zomer 2018 | No. 37 | €5',  
        u'Najaar 2018 | No. 38 | €5',  
        u'Winter 2018 | No. 39 | €5',  
    )
    
    priceStyle1 = dict(font='Upgrade-Book', fontSize=15, textFill=1, rTracking=0.02)
    priceStyle2 = dict(font='Upgrade-Book', textFill=1, fontSize=15, openTypeFeatures=dict(sups=True))
    bs = context.newString(t[page], style=priceStyle1)
    bs +=  context.newString('95',style=priceStyle2)
    bx, by, bw, bh = bs.bounds()
    context.text(bs, (w-M-(bx+bw), MB))

    y = h - M
    
    c = ( # Title colors per page
        0, 1, 0, 1   
    )
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Light', fontSize=15.5, textFill=c[page], openTypeFeatures=dict(smcp=True, c2sc=True, ss08=True), rLeading=0.9, rTracking=0.02)
    #bs = context.newString('onafhankelijk smaakmakend\rmagazine over speciaal bier', style=style)  
    bs = context.newString('onafhankelijk smaakmakend\r'.upper(), style=style)  
    style['rTracking'] = 0.042
    bs += context.newString('magazine over speciaal bier'.upper(), style=style)  
    bx, by, bw, bh = bs.bounds()
    context.text(bs, (w/2.3, y-bh-M/2))

    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Black', fontSize=100, textFill=1, rTracking=-0.025)
    bs = context.newString(magazineTitle, style=coverTitleStyle, w=w)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (w/2-(bw+bx)/2, y-bh))
    context.resetShadow()

    y -= (bh-by)+2*LM

    t = (
        (u'Leven in de brouwerij', w*2/3.2),
        (u'De Koninck Late Night', w*2/3.2),
        (u'Brouwerijtour', w/2),
        (u'Bierreis grensstreek', w*2/3.2)
    )
    style = dict(font='Upgrade-Italic', fontSize=64, textFill=(1, 1, 1, 0.8), rLeading=1)
    bs = context.newString(t[page][0], style=style, w=t[page][1])  
    bx, by, bw, bh = bs.bounds()
    context.text(bs, (M, y-bh))
    
    y -= (bh-by)+LM-8

    t = (
        (u'Hommels', w/2),
        (u'Geproefde bieren', w/2-2*M),
        (u'Beer Battle', w/2-2*M),
        (u'Droomweekend bier', w/2),
    )
    style = dict(font='Upgrade-Semibold', fontSize=50, textFill=(0xd4/255, 0x89/255, 0x5a/255, 0.8), rTracking=0.02, rLeading=0.7)
    bs = context.newString(t[page][0], style=style, w=t[page][1])  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (M, y-bh))
    context.resetShadow()
    
    y -= (bh-by)+3.5*LM

    t = (
        (u'De Baronie\nWestmalle\nCafé Trappisten', w-2*M, (0x3e/255, 0x1a/255, 0x09/255, 0.2)),
        (u'Vlaamse\nBiergaai', w/2-3*M, (0xd4/255, 0x89/255, 0x5a/255, 0.1)),
        (u'.\n\n\nHollandse\nHopvogel', w/2-2*M, (0xd4/255, 0x89/255, 0x5a/255, 0.1)),
        (u'Italiaans abdijbier', w-2*M, (0xd4/255, 0x89/255, 0x5a/255, 0.1)),   
    )
    style = dict(font='Upgrade-Black', fontSize=60, textFill=t[page][2], textStroke=(1, 1, 1, 0.5), textStrokeWidth=3, rTracking=0.03, rLeading=0.9)
    bs = context.newString(t[page][0], style=style, w=t[page][1])  
    bx, by, bw, bh = bs.bounds()
    context.text(bs, (M, y-bh))

    y -= (bh-by)-LM

    t = (
        u'Kompaan brouwt het beste bier van Nederland',  
        u'Wederopbouw: Help de monniken met “Deep Roots”',  
        u'Two Chefs Brewing opent microbrouwerij Amsterdam',  
        u'Brouwerij in distilleerderij in Weesper kerk',  
    )
    style = dict(font='Upgrade-Regular', fontSize=100, textFill=(1, 1, 1, 0.95), rTracking=0.02)
    bs = context.newString(t[page], style=style, w=w-3*M)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (1.5*M, 6*M))
    context.resetShadow()
    
IMAGES = (
    ('docs/documents/bierCoverPages1.pdf', W, H, buildCoverPages1, 'IMG_2034-50.jpg', 0),    ('docs/images/bierCoverPages1.png', W, H, buildCoverPages1, 'IMG_2034-50.jpg', 0),    ('docs/documents/bierCoverPages2.pdf', W, H, buildCoverPages1, 'IMG_4890-50.jpg', 1),    ('docs/images/bierCoverPages2.png', W, H, buildCoverPages1, 'IMG_4890-50.jpg', 1),    ('docs/documents/bierCoverPages3.pdf', W, H, buildCoverPages1, 'IMG_9037-50.jpg', 2),    ('docs/images/bierCoverPages3.png', W, H, buildCoverPages1, 'IMG_9037-50.jpg', 2),    ('docs/documents/bierCoverPages4.pdf', W, H, buildCoverPages1, 'IMG_9070-50.jpg', 3),    ('docs/images/bierCoverPages4.png', W, H, buildCoverPages1, 'IMG_9070-50.jpg', 3),)        
      
for path, w, h, m, imagePath, page in IMAGES:
    newDrawing()
    m(w, h, imagePath, page)
    saveImage(path, multipage=True)
    print path
    