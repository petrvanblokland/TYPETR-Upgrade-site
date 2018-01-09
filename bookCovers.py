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
#     bookCovers.py
#
from pagebot.contexts import defaultContext as context
from pagebot.fonttoolbox.objects.font import getFontByName
from pagebot.style import A4, CENTER, DISPLAY_BLOCK, RIGHT, LEFT
from pagebot import Gradient, Shadow
from pagebot.toolbox.dating import now

shadow = Shadow(offset=(6, -6), blur=10, color=(0.2, 0.2, 0.2, 0.5))

W, H = A4

def buildCoverPages(w, h, year):
	
    footNoteRef = 12

    magazineTitle = 'Habit'

    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_0672-50.jpg', (-14, -5), w=w*1.05, h=h*1.05)
    
    y = h
    
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Bold', fontSize=100, textFill=1)
    bs = context.newString(magazineTitle, style=coverTitleStyle, w=w-4*M)  
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (ML, y-th*0.65))
    context.resetShadow()

    y -= th
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Light', fontSize=100, textFill=0.1)
    bs = context.newString('Upgrade loveables', style=style, w=w*0.75-18*M)  
    tw, th = bs.size()  
    context.text(bs, (ML*14, y+th*0.65))
 
     # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-BlackItalic', fontSize=100, textStroke=1, textStrokeWidth=2, textFill=None)
    bs = context.newString(year, style=style, w=w/2-24*M)  
    tw, th = bs.size()  
    context.text(bs, (w/2, MB+20))
    
def buildCoverPages1(w, h, year):
	
    footNoteRef = 12

    magazineTitle = u'Habit'

    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_3076-50.jpg', (-14, -5), w=w*1.05, h=h*1.05)
    
    y = h
    
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Bold', fontSize=100, textFill=(0.85, 0.85, 1, 0.95))
    bs = context.newString(magazineTitle, style=coverTitleStyle, w=w-4*M)  
    tw, th = bs.size()  
    context.text(bs, (ML, y-th*0.65))

    y -= th
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Light', fontSize=100, textFill=1, rLeading=1)
    bs = context.newString('Upgrade\nServices', style=style, w=w/3.5)  
    tw, th = bs.size()  
    context.text(bs, (w*2/3, y+th/2))

   # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-BlackItalic', fontSize=100, textStroke=(1, 1, 1, 0.6), textStrokeWidth=2.5, textFill=None)
    bs = context.newString(year, style=coverTitleStyle, w=w/2.5-24*M)  
    tw, th = bs.size()  
    context.text(bs, (M*3, MB+20))
    

IMAGES = (
    ('docs/documents/bookCoverPages.pdf', W, H, now().year, buildCoverPages),    ('docs/images/bookCoverPages.png', W*3/4, H*3/4, now().year, buildCoverPages),    ('docs/documents/bookCoverPages1.pdf', W, H, now().year+1, buildCoverPages1),    ('docs/images/bookCoverPages1.png', W*3/4, H*3/4, now().year+1, buildCoverPages1),)        
      
for path, w, h, year, m in IMAGES:
    newDrawing()
    m(w, h, year)
    saveImage(path, multipage=True)
    print path
    