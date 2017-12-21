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

def buildCoverPages(w, h):
	
    footNoteRef = 12

    magazineTitle = 'Magazin'
    chapterTitle = 'Design Design Space'

    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/PepperTomSkirt_img0093.png', (0, 0), w=w, h=h)
    
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
    
    y -= th
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Regular', fontSize=100, textFill=(0.2, 0.2, 0.7))
    bs = context.newString('Pepper+Tom', style=style, w=w*0.75-12*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*10, y-th*0.5))
    context.resetShadow()
    
    y -= th*0.9
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-MediumItalic', fontSize=100, textFill=(0.2, 0.25, 0.7))
    bs = context.newString('Upgrade Fashion', style=coverTitleStyle, w=w*0.75-18*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*10, y-th*0.5))
    context.resetShadow()
    
    y -= th
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Book', fontSize=100, textFill=(0.95, 0.95, 1, 0.7))
    bs = context.newString('&', style=coverTitleStyle, w=w*0.75-30*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*10, y-th*0.6))
    context.resetShadow()
    
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Bold', fontSize=100, textFill=(0.1, 0.15, 0.7, 0.8))
    bs = context.newString('Models', style=coverTitleStyle, w=w*0.75-24*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*10, y-th*0.5))
    context.resetShadow()
    
    #context.b.lineCap('')
    
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Black', fontSize=100, textStroke=(0.2, 0.2, 0.2, 0.5), textStrokeWidth=4, textFill=None)
    bs = context.newString('Boots', style=coverTitleStyle, w=w-ML*20)  
    tw, th = bs.size()  
    context.text(bs, (ML*10, 12*MB))
    coverTitleStyle = dict(font='Upgrade-Black', fontSize=100, textStroke=(1, 0, 0.3, 0.9), textStrokeWidth=1, textFill=None)
    bs = context.newString('Boots', style=coverTitleStyle, w=w-ML*20)  
    tw, th = bs.size()  
    context.text(bs, (ML*10-2, 12*MB+2))
    
    """
    pn = context.newString(66, style=coverTitleStyle)
    context.text(pn, (w/2 - pn.w/2, M/2))

    pt = context.newString(bookTitle, style=pageTitleStyle)
    context.textBox(pt, (ML, h-MT*0.75, cw, pt.h))

    # Page 67
    context.newPage(w, h) 
    
    # Assume that we have a footnote on this page, calc it's space.
    fnMark = context.newString(footNoteRef, style=footNoteRefStyle)
    fn = fnMark + ' ' + context.newString(footNoteText, style=footNoteStyle)
    fnw, fnh = fn.textSize(cw)
    cfnh = fnh+bodyStyle['fontSize']*bodyStyle['rLeading']
    ch = h-MB-MT-cfnh
    R = (ML, MB+cfnh, cw, ch)
    context.textBox(overFill, R)

    context.textBox(fn, (ML, MB, cw, fnh))

    pt = context.newString(chapterTitle, style=pageChapterStyle)
    context.textBox(pt, (ML, h-MT*0.75, cw, pt.h))
    
    pn = context.newString(67, style=pageNumberStyle)
    context.text(pn, (w/2 - pn.w/2, M/2))
    """


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
    
    y -= th
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Regular', fontSize=100, textFill=(0.2, 0.2, 0.7))
    bs = context.newString('Pepper+Tom', style=style, w=w*0.75-12*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*10, y-th*0.5))
    context.resetShadow()
    
    y -= th*0.9
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-MediumItalic', fontSize=100, textFill=(0.2, 0.25, 0.7))
    bs = context.newString('Upgrade Fashion', style=coverTitleStyle, w=w*0.75-18*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*10, y-th*0.5))
    context.resetShadow()
    
    y -= th
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Book', fontSize=100, textFill=(0.95, 0.95, 1, 0.7))
    bs = context.newString('&', style=coverTitleStyle, w=w*0.75-30*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*10, y-th*0.6))
    context.resetShadow()
    
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Bold', fontSize=100, textFill=(0.1, 0.15, 0.7, 0.8))
    bs = context.newString('Models', style=coverTitleStyle, w=w*0.75-24*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML*10, y-th*0.5))
    context.resetShadow()
    
    #context.b.lineCap('')
    
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Black', fontSize=100, textStroke=(0.2, 0.2, 0.2, 0.5), textStrokeWidth=4, textFill=None)
    bs = context.newString('Boots', style=coverTitleStyle, w=w-ML*20)  
    tw, th = bs.size()  
    context.text(bs, (ML*10, 12*MB))
    coverTitleStyle = dict(font='Upgrade-Black', fontSize=100, textStroke=(1, 0, 0.3, 0.9), textStrokeWidth=1, textFill=None)
    bs = context.newString('Boots', style=coverTitleStyle, w=w-ML*20)  
    tw, th = bs.size()  
    context.text(bs, (ML*10-2, 12*MB+2))
 
IMAGES = (
    #('docs/documents/fashionCoverPages.pdf', W, H, buildCoverPages),    #('docs/images/fashionCoverPages.png', W*3/4, H*3/4, buildCoverPages),    ('docs/documents/fashionCoverPages1.pdf', W, H, buildCoverPages1),    ('docs/images/fashionCoverPages1.png', W*3/4, H*3/4, buildCoverPages1),)        
      
for path, w, h, m in IMAGES:
    newDrawing()
    m(w, h)
    saveImage(path, multipage=True)
    print path
    