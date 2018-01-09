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

magazineTitle = u'Habit'

W, H = A4[0]*3/4, A4[1]*3/4

M = 4 # Margin
LM = 4*M # Line margin
ML, MR, MT, MB = M, 2*M, 3*M, 1.5*M
cw = W - ML - MR

def buildCoverPages1(w, h, year):
	
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled. Disproportional scale.
    context.image('docs/images/IMG_0672-50.jpg', (-150, -5), w=w*1.07, h=h*1.05)
    
    y = h - MT
    
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Bold', fontSize=100, textFill=1)
    bs = context.newString(magazineTitle, style=coverTitleStyle, w=cw)  
    bx, by, bw, bh = bs.bounds() # by is negative amount under baseline. bh is amount above baseline.
    context.setShadow(shadow)
    context.text(bs, (ML, y-bh))
    context.resetShadow()

    y = y - bh + by - LM
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Light', fontSize=100, textFill=0.1)
    bs = context.newString('Upgrade loveables', style=style, w=w*0.75-18*M)  
    bx, by, bw, bh = bs.bounds() # by is negative amount under baseline. bh is amount above baseline.
    context.text(bs, (ML*8, y - bh))
 
     # Title of cover, make it fit in with and add shadow
    yearStyle = dict(font='Upgrade-BlackItalic', fontSize=100, textStroke=1, textStrokeWidth=2, textFill=None)
    bs = context.newString(year, style=yearStyle, w=w/2.5-12*M)  
    tw, th = bs.size()  
    context.text(bs, (w*3/5, MB+4*M))
    
def buildCoverPages2(w, h, year):
	
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_3076-50.jpg', (-14, -145), h=h*1.05)
    
    y = h - MT
    
    # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-Bold', fontSize=100, textFill=(0.85, 0.85, 1, 0.95))
    bs = context.newString(magazineTitle, style=coverTitleStyle, w=cw)  
    bx, by, bw, bh = bs.bounds() # by is negative amount under baseline. bh is amount above baseline.
    context.setShadow(shadow)
    context.text(bs, (ML, y-bh))
    context.resetShadow()

    y = y - bh + by - LM

    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Light', fontSize=100, textFill=1, rLeading=1)
    bs = context.newString('Upgrade\nServices', style=style, w=w/4)  
    bx, by, bw, bh = bs.bounds() # by is negative amount under baseline. bh is amount above baseline.
    context.text(bs, (w*2/3, y-bh))

   # Title of cover, make it fit in with and add shadow
    yearStyle = dict(font='Upgrade-BlackItalic', fontSize=100, textStroke=(1, 1, 1, 0.6), textStrokeWidth=2.5, textFill=None)
    bs = context.newString(year, style=yearStyle, w=w/2.5-12*M)  
    context.text(bs, (M*3, MB+4*M))
    

IMAGES = (
    ('docs/documents/habitCoverPages1.pdf', W, H, now().year, buildCoverPages1),    ('docs/images/habitCoverPages1.png', W, H, now().year, buildCoverPages1),    ('docs/documents/habitCoverPages2.pdf', W, H, now().year+1, buildCoverPages2),    ('docs/images/habitCoverPages2.png', W, H, now().year+1, buildCoverPages2),)        
      
for path, w, h, year, m in IMAGES:
    newDrawing()
    m(w, h, year)
    saveImage(path, multipage=True)
    print path
    