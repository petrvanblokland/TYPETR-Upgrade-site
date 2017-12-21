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

W, H = A4[0], A4[1]

magazineTitle1 = u'Travel'
magazineTitle2 = u'Martha’s\nVineyard'


def buildCoverPages(w, h, year):
	
    bodyStyle = dict(font='Upgrade-Light', fontSize=26, textFill=1, rTracking=0.01)
    bodyItalicStyle = dict(font='Upgrade-LightItalic', fontSize=26, textFill=1, rTracking=0.01)

    mvText = (
        (u'Martha’s Vineyard, a', bodyStyle),
        (u' Massachusetts', bodyItalicStyle),
        (u' island, sits in the Atlantic just south of ', bodyStyle),
        (u'Cape Cod.', bodyItalicStyle),
        (u' A longtime New England summer colony, it encompasses harbor towns and lighthouses, sandy beaches and farmland.\n\n\n\nIt’s accessible only by boat or air. ', bodyStyle),
        (u'Vineyard Haven,', bodyItalicStyle),
        (u' on the eastern end, is a ferry port and the island’s commercial center. ', bodyStyle),
        (u'Oak Bluffs', bodyItalicStyle),
        (u' has Carpenter Gothic cottages and an iconic carousel.', bodyStyle)
    )
	 
    r, g, b = 0x18/255, 0x24/255, 0x35/255

    M = 2 # Margin
    ML, MR, MT, MB = R = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
   # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_2971-50.jpg', (0, 0), w=w*1, h=h*1)
     
    y = h
    
    # Title of cover, make it fit in with and add shadow
    # PageBot bug: automatic sizing with tracking does not work now
    #coverTitleStyle = dict(font='Upgrade-Medium', fontSize=100, textFill=1, rTracking=-0.5)
    #bs = context.newString(magazineTitle, style=coverTitleStyle, w=w-4*M)  
    coverTitleStyle = dict(font='Upgrade-Semibold', fontSize=130, textFill=(0x38/255, 0x75/255, 0xCF/255, 0.6), rLeading=0.8)
    bs = context.newString(u'Martha’s\n', style=coverTitleStyle, w=w-M)  
    coverTitleStyle = dict(font='Upgrade-Semibold', fontSize=130, textFill=(0x5E/255, 0x9D/255, 0xEE/255, 0.4), rLeading=0.8)
    bs += context.newString(u'Vineyard', style=coverTitleStyle, w=w-2*M)  
    tw, th = bs.size()  
    context.text(bs, (0, y-th/2))

    coverTitleStyle = dict(font='Upgrade-Hairline', fontSize=52, textFill=1, rLeading=0.8)
    bs = context.newString(magazineTitle1, style=coverTitleStyle, w=w/3-4*M)  
    tw, th = bs.size()  
    context.text(bs, (w-4*M-tw, y-th*1.1))
      
   # Title of cover, make it fit in with and add shadow
    bs = context.newText(mvText)  
    tw, th = context.textSize(bs, w=w-M*20)
    context.textBox(bs, (M*10, M*20, w-M*20, th))
    

  
def buildCoverPages1(w, h, year):
    BODY_SIZE = 35
    bodyStyle = dict(font='Upgrade-Light', fontSize=BODY_SIZE, textFill=1, rTracking=0.01)
    bodyItalicStyle = dict(font='Upgrade-LightItalic', fontSize=BODY_SIZE, textFill=1, rTracking=0.01)

    mvText = (
        (u'Martha’s Vineyard, a ', bodyStyle),
        (u'Massachusetts ', bodyItalicStyle),
        (u'island, sits in the Atlantic just south of ', bodyStyle),
        (u'Cape Cod.', bodyItalicStyle),
        (u' A longtime ', bodyStyle),
        (u'New England ', bodyItalicStyle),
        (u'summer colony, it encompasses harbor towns and lighthouses, sandy beaches and farmland.\n\n\n\n\nIt’s accessible only by boat or air. ', bodyStyle),
        (u'Vineyard Haven,', bodyItalicStyle),
        (u' on the eastern end, is a ferry port and the island’s commercial center. ', bodyStyle),
        (u'Oak Bluffs', bodyItalicStyle),
        (u' has Carpenter Gothic cottages and an iconic carousel.', bodyStyle)
    )
	 
    r, g, b = 0x18/255, 0x24/255, 0x35/255

    M = 2 # Margin
    ML, MR, MT, MB = R = M, 0.75*M, M, 1.5*M
    cw = w-ML-MR
    
    # Page 66
    context.newPage(w, h) 
    
   # Draw image, covering all page, scaled.
    context.image('docs/images/IMG_2597-50.jpg', (0, 0), w=w*1, h=h*1)
     
    y = h
    
    # Title of cover, make it fit in with and add shadow
    # PageBot bug: automatic sizing with tracking does not work now
    #coverTitleStyle = dict(font='Upgrade-Medium', fontSize=100, textFill=1, rTracking=-0.5)
    #bs = context.newString(magazineTitle, style=coverTitleStyle, w=w-4*M)  
    coverTitleStyle = dict(font='Upgrade-Semibold', fontSize=130, textFill=(0x38/255, 0x75/255, 0xCF/255, 0.6), rLeading=0.8)
    bs = context.newString(u'Martha’s\n', style=coverTitleStyle, w=w-M)  
    coverTitleStyle = dict(font='Upgrade-Semibold', fontSize=130, textFill=(0x5E/255, 0x9D/255, 0xEE/255, 0.4), rLeading=0.8)
    bs += context.newString(u'Vineyard', style=coverTitleStyle, w=w-2*M)  
    tw, th = bs.size()  
    context.text(bs, (0, y-th/2))

    coverTitleStyle = dict(font='Upgrade-Thin', fontSize=52, textFill=1, rLeading=0.8)
    bs = context.newString(magazineTitle1, style=coverTitleStyle, w=w/3-4*M)  
    tw, th = bs.size()  
    context.text(bs, (w-4*M-tw, y-th*1.1))
      
   # Title of cover, make it fit in with and add shadow
    bs = context.newText(mvText)  
    tw, th = context.textSize(bs, w=w-M*20)
    context.textBox(bs, (M*10, M*30, w-M*20, th))
    

   
IMAGES = (
    ('docs/documents/travelCoverPages.pdf', W, H, now().year, buildCoverPages),    ('docs/images/travelCoverPages.png', W, H, now().year, buildCoverPages),    ('docs/documents/travelCoverPages1x.pdf', W, H, now().year+1, buildCoverPages1),    ('docs/images/travelCoverPages1x.png', W, H, now().year+1, buildCoverPages1),)        
      
for path, w, h, year, m in IMAGES:
    newDrawing()
    m(w, h, year)
    saveImage(path, multipage=True)
    print path
    