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

magazineTitle = u'Natur'


def buildCoverPages(w, h, year):
	
    r, g, b = 0xAA/255, 0x00/255, 0x1E/255

    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
   # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_2574-50.jpg', (-1, -10), h=h+20)
    
    context.save()
    #context.setGradient(gradient, (0, h*3/4), w, h/5) # Add self to define start/end from relative size.
    context.fill((r, g, b, 0.8))
    context.rect(0, h*4/5, w, h/5)
    context.restore()
    
    y = h
    
    # Title of cover, make it fit in with and add shadow
    # PageBot bug: automatic sizing with tracking does not work now
    #coverTitleStyle = dict(font='Upgrade-Medium', fontSize=100, textFill=1, rTracking=-0.5)
    #bs = context.newString(magazineTitle, style=coverTitleStyle, w=w-4*M)  
    coverTitleStyle = dict(font='Upgrade-Medium', fontSize=100, textFill=1)
    bs = context.newString(magazineTitle, style=coverTitleStyle)  
    bs += context.newString('2', style=dict(font='Upgrade-Medium', textFill=1, fontSize=100, openTypeFeatures=dict(sinf=True)))
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (M*4, y-th*0.62))
    context.resetShadow()
    
    y -= th
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Book', fontSize=h/21, textFill=1, rLeading=1.1)
    bs = context.newString('Upgraded\nPinkers', style=style)  
    tw, th = bs.size()  
    context.text(bs, (w*2/3, y+th*1.33))

   # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-LightItalic', fontSize=28, textFill=1)
    bs = context.newString('February', style=coverTitleStyle)  
    context.text(bs, (M*6, MB+16))
    
   
def buildCoverPages1(w, h, year):
	
    r, g, b = 0x18/255, 0x24/255, 0x35/255

    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
   # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_2643-50.jpg', (-1000, 0), h=h)
    
    context.save()
    #context.setGradient(gradient, (0, h*3/4), w, h/5) # Add self to define start/end from relative size.
    context.fill((r, g, b, 0.8))
    context.rect(0, h*4/5, w, h/5)
    context.restore()
    
    y = h
    
    # Title of cover, make it fit in with and add shadow
    # PageBot bug: automatic sizing with tracking does not work now
    #coverTitleStyle = dict(font='Upgrade-Medium', fontSize=100, textFill=1, rTracking=-0.5)
    #bs = context.newString(magazineTitle, style=coverTitleStyle, w=w-4*M)  
    coverTitleStyle = dict(font='Upgrade-Medium', fontSize=100, textFill=1)
    bs = context.newString(magazineTitle, style=coverTitleStyle)  
    bs += context.newString('3', style=dict(font='Upgrade-Medium', textFill=1, fontSize=100, openTypeFeatures=dict(sups=True)))
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (M*4, y-th*0.62))
    context.resetShadow()
    
    y -= th
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Book', fontSize=h/21, textFill=1, rLeading=1.1)
    bs = context.newString('Upgraded\nBrass & Blue', style=style)  
    tw, th = bs.size()  
    context.text(bs, (w*2/3, y+th*1.33))

   # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-LightItalic', fontSize=28, textFill=1)
    bs = context.newString('March', style=coverTitleStyle)  
    context.text(bs, (M*6, MB+16))
    

def buildCoverPages2(w, h, year):

    r, g, b = 0x40/255, 0x76/255, 0x1F/255

    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_1728-50.jpg', (-100, -10), h=h+20)
    
    context.save()
    #context.setGradient(gradient, (0, h*3/4), w, h/5) # Add self to define start/end from relative size.
    context.fill((r, g, b, 0.8))
    context.rect(0, h*4/5, w, h/4)
    context.restore()
    
    y = h
    
    # Title of cover, make it fit in with and add shadow
    # PageBot bug: automatic sizing with tracking does not work now
    #coverTitleStyle = dict(font='Upgrade-Medium', fontSize=100, textFill=1, rTracking=-0.5)
    #bs = context.newString(magazineTitle, style=coverTitleStyle, w=w-4*M)  
    coverTitleStyle = dict(font='Upgrade-Medium', fontSize=100, textFill=1)
    bs = context.newString(magazineTitle, style=coverTitleStyle)  
    bs += context.newString('8', style=dict(font='Upgrade-Medium', textFill=1, fontSize=100, openTypeFeatures=dict(sinf=True)))
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (M*4, y-th*0.62))
    context.resetShadow()
    
    y -= th
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Book', fontSize=h/21, textFill=1, rLeading=1.1)
    bs = context.newString('Upgraded\nGingers', style=style)  
    tw, th = bs.size()  
    context.text(bs, (w*2/3, y+th*1.33))

   # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-LightItalic', fontSize=28, textFill=1)
    bs = context.newString('August', style=coverTitleStyle)  
    context.text(bs, (w*2/3, MB+12))
    

def buildCoverPages3(w, h, year):

    r, g, b = 0x45/255, 0x76/255, 0x76/255
    #gradient = Gradient(start=(0, 0), end=(0, 1), locations=(0, 1), colors=((r, g, b, 0 ), (r, g, b, 1)))
	
    M = 2 # Margin
    ML, MR, MT, MB = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
    # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_0750-50.jpg', (-w/2.4, -8), h=h+16)
    
    context.save()
    #context.setGradient(gradient, (0, h*3/4), w, h/5) # Add self to define start/end from relative size.
    context.fill((r, g, b, 0.8))
    context.rect(0, h*4/5, w, h/4)
    context.restore()
    
    y = h
    
    # Title of cover, make it fit in with and add shadow
    # PageBot bug: automatic sizing with tracking does not work now
    #coverTitleStyle = dict(font='Upgrade-Medium', fontSize=100, textFill=1, rTracking=-0.5)
    #bs = context.newString(magazineTitle, style=coverTitleStyle, w=w-4*M)  
    coverTitleStyle = dict(font='Upgrade-Medium', fontSize=100, textFill=1)
    bs = context.newString(magazineTitle, style=coverTitleStyle) 
    bs += context.newString('9', style=dict(font='Upgrade-Medium', textFill=1, fontSize=100, openTypeFeatures=dict(sups=True)))
    tw, th = bs.size()  
    context.setShadow(shadow)
    context.text(bs, (M*4, y-th*0.62))
    context.resetShadow()
    
    y -= th
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Book', fontSize=h/21, textFill=1, rLeading=1.1)
    bs = context.newString('Upgraded\nExperience', style=style)  
    tw, th = bs.size()  
    context.text(bs, (w*2/3, y+th*1.33))

   # Title of cover, make it fit in with and add shadow
    coverTitleStyle = dict(font='Upgrade-LightItalic', fontSize=28, textFill=1)
    bs = context.newString('September', style=coverTitleStyle)  
    context.text(bs, (w*2/3, MB+12))
    
   
IMAGES = (
    ('docs/documents/naturCoverPages.pdf', W, H, now().year, buildCoverPages),    ('docs/images/naturCoverPages.png', W, H, now().year, buildCoverPages),    ('docs/documents/naturCoverPages1.pdf', W, H, now().year+1, buildCoverPages1),    ('docs/images/naturCoverPages1.png', W, H, now().year+1, buildCoverPages1),    ('docs/documents/naturCoverPages2.pdf', W, H, now().year+1, buildCoverPages2),    ('docs/images/naturCoverPages2.png', W, H, now().year+1, buildCoverPages2),    ('docs/documents/naturCoverPages3.pdf', W, H, now().year+1, buildCoverPages3),    ('docs/images/naturCoverPages3.png', W, H, now().year+1, buildCoverPages3),)        
      
for path, w, h, year, m in IMAGES:
    newDrawing()
    m(w, h, year)
    saveImage(path, multipage=True)
    print path
    