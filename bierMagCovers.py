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


def buildCoverPages1(w, h, imagePath):
	
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

    style = dict(font='Upgrade-Regular', fontSize=100, textFill=(1, 1, 1, 0.95), rTracking=0.02)
    bs = context.newString('Kompaan brouwt het beste bier van Nederland', style=style, w=w-2*M)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (M, 6*M))
    context.resetShadow()
    

def buildCoverPages2(w, h):
	
    footNoteRef = 12

    magazineTitle = 'Magazin'
    chapterTitle = 'Design Design Space'

    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_1978-50.jpg', (-w/2, 0), h=h)
    
    y = h
    
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-SemiboldItalic', fontSize=100, textFill=1)
    bs = context.newString(now().fullmonthname, style=style, w=w/4)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (w/2+tw/10, y-th*0.9))
    context.resetShadow()

    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-UltraBlack', fontSize=100, textFill=1)
    bs = context.newString(magazineTitle, style=coverTitleStyle, w=w-2*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML, y-th*0.7))
    context.resetShadow()

def buildCoverPages3(w, h):
	    
    M = 2 # Margin
    ML, MR, MT, MB = 2*M, 2*M, 2*M, 1.5*M
    cw = w - ML - MR
    L = 12
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_1382-50.jpg', (-w/3, 0), h=h)

    y = h - MT
    
    monthStyle = dict(font='Upgrade-Regular', fontSize=15, textFill=(1, 1, 1, 0.95), rTracking=0.05)
    bs = context.newString(u'%s %d' % (now().fullmonthname, now().year), style=monthStyle)
    bx, by, bw, bh = bs.bounds()
    context.text(bs, (w-7*M-bw, 8*M))

    priceStyle1 = dict(font='Upgrade-Light', fontSize=15, textFill=0, rTracking=0.02)
    priceStyle2 = dict(font='Upgrade-Light', textFill=0, fontSize=15, openTypeFeatures=dict(sups=True))
    bs = context.newString(u'$4', style=priceStyle1)
    bs +=  context.newString('95',style=priceStyle2)
    tw, th = bs.size()
    bx, by, bw, bh = bs.bounds()
    context.text(bs, (w-3*M-tw, y-bh-7*M))

    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-UltraBlack', fontSize=100, textFill=1)
    bs = context.newString(u'U', style=coverTitleStyle, w=w/2)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (-bx+8*M, y-bh-6*M))
    context.resetShadow()

    y -= (bh-by)+L+6*M

    style = dict(font='Upgrade-Thin', fontSize=100, textFill=1)
    bs = context.newString('UPGRADE', style=style, w=w/2.2)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (w/4-(bw-bx)/2, y-bh))
    context.resetShadow()

    y -= bh+4*M

    style = dict(font='Upgrade-Book', fontSize=100, textFill=1)
    bs = context.newString('STYLES', style=style, w=w/2.1)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (w/4-(bw-bx)/2, y-bh))
    context.resetShadow()

    
    y -= bh+4*M
    
    style = dict(font='Upgrade-Light', fontSize=30, textFill=1, xTextAlign=CENTER, rLeading=0.95)
    style_sc = dict(font='Upgrade-Light', fontSize=30, textFill=1, xTextAlign=CENTER, rLeading=0.95, rTracking=0.2, openTypeFeatures=dict(smcp=True))
    bs = context.newString('Magazine\nTypography\n', style=style)  
    bs += context.newString('Sketching\n', style=style_sc)  
    bs += context.newString('Code Designers', style=style)  
    bx, by, bw, bh = bs.bounds()
    tw, th = bs.size()
    context.setShadow(shadow)
    context.text(bs, (w/4-(bw-bx)/2, y-bh))
    context.resetShadow()
    
    y -= th+4+M
    style = dict(font='Upgrade-Black', fontSize=40, textFill=(1, 0.5, 0.7, 0.8), rTracking=0.01)
    bs = context.newString(u'PAGEBOT PAGINA’S', style=style)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (w/2-(bw-bx)/2, y-bh))
    context.resetShadow()
    
    y -= bh+6*M
    style = dict(font='Upgrade-Medium', fontSize=100, textFill=(0xE5/255, 0xE5/255, 0xDe/255, 0.7), rTracking=-0.01)
    bs = context.newString('MediumLight', style=style, w=w-20*M)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (w/2-(bw-bx)/2, y-bh))
    context.resetShadow()
    
    y -= bh-by+3*M
    style = dict(font='Upgrade-Semibold', fontSize=100, textFill=(1, 1, 1, 0.95), rTracking=0.2)
    bs = context.newString(u'HOW TO LICENSE THE TYPE FROM TYPETR•COM', style=style, w=w-12*M)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (w/2-(bw-bx)/2, y-bh))
    context.resetShadow()
        
def buildCoverPages4(w, h):
	
    footNoteRef = 12

    magazineTitle = 'Magazin'
    chapterTitle = 'Design Design Space'

    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    L = 6*M
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_1645-50.jpg', (-w/1.5, 0), h=h)
    
    y = h-10*M
    """
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-SemiboldItalic', fontSize=100, textFill=1)
    bs = context.newString(now().fullmonthname, style=style, w=w/4)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (w/2+tw/10, y-th*0.9))
    context.resetShadow()
    """
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Medium', fontSize=100, textFill=1)
    bs = context.newString('M', style=coverTitleStyle, w=w/2)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (w-bw-10*M, y-bh))
    context.resetShadow()

    y -= bh+L

    monthStyle = dict(font='Upgrade-Book', fontSize=16, textFill=0, rTracking=0.02)
    bs = context.newString(u'December %d' % now().year, style=monthStyle, w=w/3-26*M)
    bx, by, bw, bh = bs.bounds()
    context.text(bs, (w-(bw-bx)-10*M, y-bh))

    y = h/2

    priceStyle1 = dict(font='Upgrade-Book', fontSize=20, textFill=0.7, rTracking=0.02)
    priceStyle2 = dict(font='Upgrade-Book', textFill=0.7, fontSize=20, openTypeFeatures=dict(sups=True))
    bs = context.newString(u'$4', style=priceStyle1)
    bs +=  context.newString('99',style=priceStyle2)
    bx, by, bw, bh = bs.bounds()
    context.text(bs, (w-10*M-(bw-bx), y+5*M))


    y = h/2-L
    style = dict(font='Upgrade-Thin', fontSize=100, textFill=1)
    bs = context.newString('THE MATH ISSUE', style=style, w=w-10*M)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (ML*5, y-bh))
    context.resetShadow()

    y -= bh+L
    style = dict(font='Upgrade-Book', fontSize=100, textFill=1)
    bs = context.newString('FESTIVAL STYLES', style=style, w=w-10*M)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (ML*5, y-bh))
    context.resetShadow()
    
    y -= bh+L
    style = dict(font='Upgrade-Book', fontSize=100, textFill=1, rTracking=0.2)
    bs = context.newString('UPGRADED MAGAZINE TYPOGRAPHY', style=style, w=w-10*M)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (ML*6, y-bh))
    context.resetShadow()
    
    y -= bh+L
    style = dict(font='Upgrade-Light', fontSize=100, textFill=1, rTracking=0.1)
    bs = context.newString('PAGEBOT FASHION', style=style, w=w-9*M)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (ML*5, y-bh))
    context.resetShadow()
    
    y -= bh+L
    style = dict(font='Upgrade-Book', fontSize=100, textFill=1, rTracking=0.02)
    bs = context.newString('HEAD & BODY CURVES', style=style, w=w-9*M)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (ML*5, y-bh))
    context.resetShadow()
    
    y -= bh+L
    style = dict(font='Upgrade-ExtraLight', fontSize=100, textFill=1, rTracking=0.02)
    bs = context.newString('LOVE LETTERS', style=style, w=w-8*M)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (ML*4, y-bh))
    context.resetShadow()
    
    y -= bh+L
    style = dict(font='Upgrade-Book', fontSize=100, textFill=1, rTracking=0.2)
    bs = context.newString('HOW TO BUY TYPE FROM TYPENETWORK/TYPETR', style=style, w=w-12*M)  
    bx, by, bw, bh = bs.bounds()
    context.setShadow(shadow)
    context.text(bs, (ML*7, y-bh))
    context.resetShadow()
   
IMAGES = (
    ('docs/documents/bierCoverPages1.pdf', W, H, buildCoverPages1, 'IMG_2034-50.jpg'),    ('docs/images/bierCoverPages1.png', W, H, buildCoverPages1, 'IMG_2034-50.jpg'),    #('docs/documents/bierCoverPages2.pdf', W, H, buildCoverPages1, 'IMG_3397-50.jpg'),    #('docs/images/bierCoverPages2.png', W, H, buildCoverPages1, 'IMG_3397-50.jpg'),    ('docs/documents/bierCoverPages2.pdf', W, H, buildCoverPages1, 'IMG_4890-50.jpg'),    ('docs/images/bierCoverPages2.png', W, H, buildCoverPages1, 'IMG_4890-50.jpg'),    ('docs/documents/bierCoverPages3.pdf', W, H, buildCoverPages1, 'IMG_9037-50.jpg'),    ('docs/images/bierCoverPages3.png', W, H, buildCoverPages1, 'IMG_9037-50.jpg'),    ('docs/documents/bierCoverPages4.pdf', W, H, buildCoverPages1, 'IMG_9070-50.jpg'),    ('docs/images/bierCoverPages4.png', W, H, buildCoverPages1, 'IMG_9070-50.jpg'),)        
      
for path, w, h, m, imagePath in IMAGES:
    newDrawing()
    m(w, h, imagePath)
    saveImage(path, multipage=True)
    print path
    