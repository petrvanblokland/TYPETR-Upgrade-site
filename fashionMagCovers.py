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

W, H = A4


def buildCoverPages1(w, h):
	
    footNoteRef = 12

    magazineTitle = 'Magazin'
    chapterTitle = 'Design Design Space'

    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_2000-50.jpg', (0, 0), h=h)
    
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
	
    footNoteRef = 12

    magazineTitle = 'Magazin'
    chapterTitle = 'Design Design Space'

    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_1382-50.jpg', (-w/3, 0), h=h)
    
    y = h
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
    coverTitleStyle = dict(font='Upgrade-UltraBlack', fontSize=100, textFill=1)
    bs = context.newString('M', style=coverTitleStyle, w=w/2)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML, y-th*0.6))
    context.resetShadow()
    
def buildCoverPages4(w, h):
	
    footNoteRef = 12

    magazineTitle = 'Magazin'
    chapterTitle = 'Design Design Space'

    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_1645-50.jpg', (-w/1.5, 0), h=h)
    
    y = h
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
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (w-tw-M, y-th*0.6))
    context.resetShadow()

    y -= th*0.6

    monthStyle = dict(font='Upgrade-Book', fontSize=16, textFill=0, rTracking=0.02)
    bs = context.newString(u'December 2017', style=monthStyle, w=w/3-20*M)
    tw, th = bs.size()
    context.text(bs, (w*2/3+10*M, y-th))

    y = h/2

    priceStyle1 = dict(font='Upgrade-Book', fontSize=20, textFill=0.7, rTracking=0.02)
    priceStyle2 = dict(font='Upgrade-Book', textFill=0.7, fontSize=20, openTypeFeatures=dict(sups=True))
    bs = context.newString(u'$4', style=priceStyle1)
    bs +=  context.newString('99',style=priceStyle2)
    tw, th = bs.size()
    context.text(bs, (w-10*M-tw, y+5*M))


    y = h/2.1
    style = dict(font='Upgrade-Thin', fontSize=100, textFill=1)
    bs = context.newString('THE MATH ISSUE', style=style, w=w-10*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*5, y-th*0.5))
    context.resetShadow()

    y -= th*0.7
    style = dict(font='Upgrade-Book', fontSize=100, textFill=1)
    bs = context.newString('FESTIVAL STYLES', style=style, w=w-10*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*5, y-th*0.5))
    context.resetShadow()
    
    y -= th*0.67
    style = dict(font='Upgrade-Book', fontSize=100, textFill=1, rTracking=0.2)
    bs = context.newString('UPGRADED MAGAZINE TYPOGRAPHY', style=style, w=w-10*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*6, y-th*0.5))
    context.resetShadow()
    
    y -= th
    style = dict(font='Upgrade-Light', fontSize=100, textFill=1, rTracking=0.1)
    bs = context.newString('PAGEBOT FASHION', style=style, w=w-9*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*5, y-th*0.5))
    context.resetShadow()
    
    y -= th*0.77
    style = dict(font='Upgrade-Book', fontSize=100, textFill=1, rTracking=0.02)
    bs = context.newString('HEAD & BODY CURVES', style=style, w=w-9*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*5, y-th*0.5))
    context.resetShadow()
    
    y -= th*0.82
    style = dict(font='Upgrade-ExtraLight', fontSize=100, textFill=1, rTracking=0.02)
    bs = context.newString('LOVE LETTERS', style=style, w=w-9*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*5, y-th*0.5))
    context.resetShadow()
    
    y -= th*0.65
    style = dict(font='Upgrade-Book', fontSize=100, textFill=1, rTracking=0.2)
    bs = context.newString('HOW TO BUY TYPE FROM TYPENETWORK/TYPETR', style=style, w=w-9*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*5, y-th*0.5))
    context.resetShadow()
    
IMAGES = (
    ('docs/documents/fashionCoverPages1.pdf', W, H, buildCoverPages1),    ('docs/images/fashionCoverPages1.png', W*3/4, H*3/4, buildCoverPages1),    ('docs/documents/fashionCoverPages2.pdf', W, H, buildCoverPages2),    ('docs/images/fashionCoverPages2.png', W*3/4, H*3/4, buildCoverPages2),    ('docs/documents/fashionCoverPages3.pdf', W, H, buildCoverPages3),    ('docs/images/fashionCoverPages3.png', W*3/4, H*3/4, buildCoverPages3),    ('docs/documents/fashionCoverPages4.pdf', W, H, buildCoverPages4),    ('docs/images/fashionCoverPages4.png', W*3/4, H*3/4, buildCoverPages4),)        
      
for path, w, h, m in IMAGES:
    newDrawing()
    m(w, h)
    saveImage(path, multipage=True)
    print path
    