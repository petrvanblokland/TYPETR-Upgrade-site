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
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/'+imagePath, (0, 0), h=h)
    
    priceStyle1 = dict(font='Upgrade-Book', fontSize=15, textFill=1, rTracking=0.02)
    priceStyle2 = dict(font='Upgrade-Book', textFill=1, fontSize=15, openTypeFeatures=dict(sups=True))
    bs = context.newString(u'Zomer 2017 | No. 35 | €5', style=priceStyle1)
    bs +=  context.newString('95',style=priceStyle2)
    bx, by, bw, bh = bs.bounds()
    context.text(bs, (w-M-(bx+bw), MB))

    y = h - M
    
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Light', fontSize=15.5, textFill=1, openTypeFeatures=dict(smcp=True, c2sc=True, ss08=True), rLeading=0.9, rTracking=0.02)
    #bs = context.newString('onafhankelijk smaakmakend\rmagazine over speciaal bier', style=style)  
    bs = context.newString('onafhankelijk smaakmakend\r'.upper(), style=style)  
    style['rTracking'] = 0.042
    bs += context.newString('magazine over speciaal bier'.upper(), style=style)  
    bx, by, bw, bh = bs.bounds()
    context.text(bs, (w/2.3, y-bh))

    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Black', fontSize=100, textFill=1)
    bs = context.newString(magazineTitle, style=coverTitleStyle, w=w)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (w/2-(bw+bx)/2, y-bh))
    context.resetShadow()

    y -= (bh-by)+2*LM

    style = dict(font='Upgrade-Italic', fontSize=64, textFill=(1, 1, 1, 0.8), rLeading=1)
    bs = context.newString('Bierreis grensstreek', style=style, w=w*2/3.2)  
    bx, by, bw, bh = bs.bounds()
    context.text(bs, (M, y-bh))
    
    y -= (bh-by)+LM-8

    style = dict(font='Upgrade-Semibold', fontSize=50, textFill=(0xd4/255, 0x89/255, 0x5a/255, 0.8), rTracking=0.02, rLeading=0.7, openTypeFeatures=dict(smcp=True))
    bs = context.newString(u'Droomweekend bier', style=style, w=w/2)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (M, y-bh))
    context.resetShadow()
    
    y -= (bh-by)+LM

    style = dict(font='Upgrade-Black', fontSize=60, textFill=(0xd4/255, 0x89/255, 0x5a/255, 0.1), textStroke=(1, 1, 1, 0.5), textStrokeWidth=3, rTracking=0.02)
    bs = context.newString('Italiaans abdijbier', style=style, w=w-2*M)  
    bx, by, bw, bh = bs.bounds()
    context.text(bs, (M, y-bh))

    y -= (bh-by)-LM

    t = (
        u'Kompaan brouwt het beste bier van Nederland',  
        u'Wederopbouw: Help de monniken met “Deep Roots”',  
        u'Two Chefs Brewing opent microbrouwerij van Amsterdam',  
        u'Brouwerij em distilleerderij in Weesper kerk',  
    )
    style = dict(font='Upgrade-Regular', fontSize=100, textFill=(1, 1, 1, 0.95), rTracking=0.02)
    bs = context.newString(t[page], style=style, w=w-2*M)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (M, 6*M))
    context.resetShadow()
    
IMAGES = (
    ('docs/documents/bierCoverPages1.pdf', W, H, buildCoverPages1, 'IMG_2034-50.jpg', 0),    ('docs/images/bierCoverPages1.png', W, H, buildCoverPages1, 'IMG_2034-50.jpg', 0),    ('docs/documents/bierCoverPages2.pdf', W, H, buildCoverPages1, 'IMG_4890-50.jpg', 1),    ('docs/images/bierCoverPages2.png', W, H, buildCoverPages1, 'IMG_4890-50.jpg', 1),    ('docs/documents/bierCoverPages3.pdf', W, H, buildCoverPages1, 'IMG_9037-50.jpg', 2),    ('docs/images/bierCoverPages3.png', W, H, buildCoverPages1, 'IMG_9037-50.jpg', 2),    ('docs/documents/bierCoverPages4.pdf', W, H, buildCoverPages1, 'IMG_9070-50.jpg', 3),    ('docs/images/bierCoverPages4.png', W, H, buildCoverPages1, 'IMG_9070-50.jpg', 3),)        
      
for path, w, h, m, imagePath, page in IMAGES:
    newDrawing()
    m(w, h, imagePath, page)
    saveImage(path, multipage=True)
    print path
    