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
#     businessCards.py
#
from pagebot.contexts import defaultContext as context
from pagebot.fonttoolbox.objects.font import getFontByName
from pagebot.style import USBusinessCard, CENTER, DISPLAY_BLOCK, RIGHT, LEFT
from pagebot import Gradient, Shadow
from pagebot.toolbox.dating import now

W, H = USBusinessCard

def buildBusinessCard1(w, h):
	
    M = 4 # Margin
    
    # Page 66
    context.newPage(w, h) 
        
    y = h
    
    context.image('docs/images/IMG_2381-50.jpg', (0, 0), w=w)
    
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Regular', fontSize=14, textFill=1, xTextAlign=CENTER)
    styleTitle = dict(font='Upgrade-Italic', fontSize=10, textFill=1, xTextAlign=CENTER)
    styleEmail = dict(font='Upgrade-Light', fontSize=8, textFill=1, xTextAlign=CENTER, leading=10, rTracking=0.02)
    bs = context.newString('Petr van Blokland\n', style=style)  
    bs += context.newString('Designer | Educator | Founder\n', style=styleTitle)  
    bs += context.newString('buro@petr.com | @petrvanblokland', style=styleEmail)
    tw, th = bs.size()  
    context.text(bs, (w/2-tw/2, h*0.55))

    logoStyle = dict(font='Upgrade-Black', fontSize=22, textFill=1, rTracking=1.4)
    bs = context.newString(u'.TYPETR', style=logoStyle)
    tw, th = bs.size()
    context.text(bs, (w/2-tw/2-3, 2*M)) 
 
    
def buildBusinessCard2(w, h):
	
    M = 4 # Margin
    
    # Page 66
    context.newPage(w, h) 
        
    y = h

    context.image('docs/images/IMG_2379-50.jpg', (0, 0), w=w*1.3)
    
    # Title of cover, make it fit in with and add shadow
    style = dict(font='Upgrade-Regular', fontSize=14, textFill=1, xTextAlign=CENTER)
    styleTitle = dict(font='Upgrade-Italic', fontSize=10, textFill=(0xEC/255, 0x3E/255, 0x2B/255), xTextAlign=CENTER)
    styleEmail = dict(font='Upgrade-Light', fontSize=8, textFill=1, xTextAlign=CENTER, leading=10, rTracking=0.02)
    bs = context.newString('Claudia Mens\n', style=style)  
    bs += context.newString('Designer | Educator | Founder\n', style=styleTitle)
    bs += context.newString('claudia@peppertom.com ', style=styleEmail)
    tw, th = bs.size()  
    context.textBox(bs, (w/2-tw/2, h/2-th/2, tw, th))
 
    styleLogo = dict(font='Upgrade-Thin', fontSize=14, textFill=1, openTypeFeatures=dict(case=True))
    bs = context.newString('PEPPER+TOM', style=styleLogo, w=w)
    context.text(bs, (0, M))  


buildBusinessCard1(W, H)
buildBusinessCard2(W, H)      

saveImage('docs/images/businessCards.png', multipage=True)
saveImage('docs/documents/businessCards.pdf', multipage=True)
