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


def buildCoverPages1(w, h):
	
    magazineTitle = 'Magazin'

    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_2000-50.jpg', (0, 0), h=h)
    
    priceStyle1 = dict(font='Upgrade-Book', fontSize=15, textFill=1, rTracking=0.02)
    priceStyle2 = dict(font='Upgrade-Book', textFill=1, fontSize=15, openTypeFeatures=dict(sups=True))
    bs = context.newString(u'$3', style=priceStyle1)
    bs +=  context.newString('50',style=priceStyle2)
    tw, th = bs.size()
    context.text(bs, (w-5*M-tw, th))
    
    y = h
    
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-SemiboldItalic', fontSize=18, textFill=TYPETR_COLOR+[0.5])
    bs = context.newString('Summer %d' % (now().year+1), style=style)  
    tw, th = bs.size()  
    context.text(bs, (w/2+tw/10, y-th*1.2))

    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-UltraBlack', fontSize=100, textFill=1)
    bs = context.newString(magazineTitle, style=coverTitleStyle, w=w-2*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML, y-th*0.7))
    context.resetShadow()

    y = h*5/6

    style = dict(font='Upgrade-HairlineItalic', fontSize=64, textFill=0, rLeading=1)
    bs = context.newString('Upgrade\nHairlines', style=style)  
    tw, th = bs.size()  
    context.text(bs, (M*4, y-th*0.5))
    
    y -= th*1.1
    style = dict(font='Upgrade-Semibold', fontSize=40, textFill=TYPETR_COLOR+[0.8], rTracking=0.05, rLeading=0.7, openTypeFeatures=dict(smcp=True))
    bs = context.newString(u'counters\n& curves', style=style, w=w/2)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (M*6, y-th*0.5))
    context.resetShadow()
    

    y -= th*1.3
    style = dict(font='Upgrade-Black', fontSize=60, textFill=None, textStroke=(0, 0, 0, 0.5), textStrokeWidth=1, rTracking=-0.01)
    bs = context.newString('BLACK', style=style)  
    tw, th = bs.size()  
    context.text(bs, (4*M, y-th*0.5))

    y -= th*0.7
    style = dict(font='Upgrade-Thin', fontSize=100, textFill=0, rTracking=-0.01)
    bs = context.newString('Regular weights', style=style, w=w/2)  
    tw, th = bs.size()  
    context.text(bs, (4*M, y-th*0.5))
    
    y -= th*0.85
    style = dict(font='Upgrade-Regular', fontSize=100, textFill=(1, 1, 1, 0.95), rTracking=0.02)
    bs = context.newString('Typographic Solutions', style=style, w=w-9*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (4*M, h/8.5))
    context.resetShadow()
    
    style = dict(font='Upgrade-Black', fontSize=100, textFill=(1, 1, 1, 0.95), rTracking=0.2)
    bs = context.newString(u'HOW TO LICENSE THE TYPE FROM TYPETR•COM', style=style, w=w-10*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*5, h/14))
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
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_1382-50.jpg', (-w/3, 0), h=h)

    monthStyle = dict(font='Upgrade-Regular', fontSize=15, textFill=(1, 1, 1, 0.95), rTracking=0.05)
    bs = context.newString(u'%s %d' % (now().fullmonthname, now().year), style=monthStyle)
    tw, th = bs.size()
    context.text(bs, (w-7*M-tw, 8*M))

    priceStyle1 = dict(font='Upgrade-Light', fontSize=15, textFill=0, rTracking=0.02)
    priceStyle2 = dict(font='Upgrade-Light', textFill=0, fontSize=15, openTypeFeatures=dict(sups=True))
    bs = context.newString(u'$4', style=priceStyle1)
    bs +=  context.newString('95',style=priceStyle2)
    tw, th = bs.size()
    context.text(bs, (w-5*M-tw, h-th))
    
    y = h

    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-UltraBlack', fontSize=100, textFill=1)
    bs = context.newString(u'U', style=coverTitleStyle, w=w/2)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (w/4-tw/2, y-th*0.50))
    context.resetShadow()

    y -= th*0.55

    style = dict(font='Upgrade-Thin', fontSize=100, textFill=1)
    bs = context.newString('UPGRADE', style=style, w=w/2.2)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (w/4-tw/2, y-th*0.5))
    context.resetShadow()

    y -= th*0.7

    style = dict(font='Upgrade-Book', fontSize=100, textFill=1)
    bs = context.newString('STYLES', style=style, w=w/2.1)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (w/4-tw/2, y-th*0.5))
    context.resetShadow()

    
    y -= th*0.16
    style = dict(font='Upgrade-Light', fontSize=30, textFill=1, xTextAlign=CENTER, rLeading=0.95)
    style_sc = dict(font='Upgrade-Light', fontSize=30, textFill=1, xTextAlign=CENTER, rLeading=0.95, rTracking=0.2, openTypeFeatures=dict(smcp=True))
    bs = context.newString('Magazine\nTypography\n', style=style)  
    bs += context.newString('Sketching\n', style=style_sc)  
    bs += context.newString('Code Designers', style=style)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (w/4-tw/2, y-th*0.5))
    context.resetShadow()
    
    y -= th*1.4
    style = dict(font='Upgrade-Black', fontSize=40, textFill=(1, 0.5, 0.7, 0.7), rTracking=0.01)
    bs = context.newString(u'PAGEBOT PAGINA’S', style=style)  
    tw, th = bs.size()  
    context.text(bs, (w/2-tw/2, y-th*0.5))
    
    y -= th*0.85
    style = dict(font='Upgrade-Medium', fontSize=100, textFill=(0xE5/255, 0xE5/255, 0xDe/255, 0.7), rTracking=-0.01)
    bs = context.newString('RegularThin', style=style, w=w-20*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (w/2-tw/2, y-th*0.5))
    context.resetShadow()
    
    y -= th*0.75
    style = dict(font='Upgrade-Semibold', fontSize=100, textFill=(1, 1, 1, 0.95), rTracking=0.2)
    bs = context.newString(u'HOW TO LICENSE THE TYPE FROM TYPETR•COM', style=style, w=w-10*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*5, y-th*0.5))
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
    bs = context.newString('LOVE LETTERS', style=style, w=w-8*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*4, y-th*0.5))
    context.resetShadow()
    
    y -= th*0.65
    style = dict(font='Upgrade-Book', fontSize=100, textFill=1, rTracking=0.2)
    bs = context.newString('HOW TO BUY TYPE FROM TYPENETWORK/TYPETR', style=style, w=w-12*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*7, y-th*0.5))
    context.resetShadow()
    
IMAGES = (
    ('docs/documents/fashionCoverPages1.pdf', W, H, buildCoverPages1),    ('docs/images/fashionCoverPages1.png', W, H, buildCoverPages1),    #('docs/documents/fashionCoverPages2.pdf', W, H, buildCoverPages2),    #('docs/images/fashionCoverPages2.png', W, H, buildCoverPages2),    #('docs/documents/fashionCoverPages3.pdf', W, H, buildCoverPages3),    #('docs/images/fashionCoverPages3.png', W, H, buildCoverPages3),    #('docs/documents/fashionCoverPages4.pdf', W, H, buildCoverPages4),    #('docs/images/fashionCoverPages4.png', W, H, buildCoverPages4),)        
      
for path, w, h, m in IMAGES:
    newDrawing()
    m(w, h)
    saveImage(path, multipage=True)
    print path
    