# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#     
#     Supporting usage of DrawBot, www.drawbot.com
#     Supporting usage of Flat, https://github.com/xxyxyz/flat
# -----------------------------------------------------------------------------
#
#     upgradeImages.py
#
upgradeFonts = []
from random import choice
for fontName in installedFonts():
    if 'Upgrade' in fontName:
        upgradeFonts.append(fontName)  

def image1(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#1', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image2(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#2', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image3(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#3', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image4(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#4', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image5(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#5', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image6(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#6', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image7(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#7', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image8(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#8', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image9(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#9', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image10(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#10', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image11(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#11', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image12(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#12', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image13(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#13', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image14(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#14', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image15(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#15', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image16(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#16', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def slide01(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('TYPETR Upgrade', font=choice(upgradeFonts), fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide02(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('TYPETR Upgrade', font=choice(upgradeFonts), fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide03(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('TYPETR Upgrade', font=choice(upgradeFonts), fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide04(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('TYPETR Upgrade', font=choice(upgradeFonts), fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide05(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('TYPETR Upgrade', font=choice(upgradeFonts), fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide06(w, h):
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('TYPETR Upgrade', font=choice(upgradeFonts), fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
        
         
IMAGES = (
    ('pic01.jpg', 384, 182, image1),    ('pic02.jpg', 384, 182, image2),    ('pic03.jpg', 384, 182, image3),    ('pic04.jpg', 384, 182, image4),    ('pic05.jpg', 282, 242, image5),    ('pic06.jpg', 102, 102, image6),    ('pic07.jpg', 102, 102, image7),    ('pic08.jpg', 102, 102, image8),    ('pic09.jpg', 102, 102, image9),    ('pic10.jpg', 102, 102, image10),    ('pic11.jpg', 102, 102, image11),    ('pic12.jpg', 78, 78, image12),    ('pic13.jpg', 78, 78, image13),    ('pic14.jpg', 78, 78, image14),    ('pic15.jpg', 78, 78, image15),    ('pic16.jpg', 78, 78, image16),    ('slide01.jpg', 1200, 440, slide01),    ('slide02.jpg', 1200, 440, slide02),    ('slide03.jpg', 1200, 440, slide03),
    ('slide04.jpg', 1200, 440, slide04),
    ('slide05.jpg', 1200, 440, slide05),
    ('slide06.jpg', 1200, 440, slide06),
)        
      
for path, w, h, m in IMAGES:
    newDrawing()
    newPage(w, h)
    m(w, h)
    imagePath = 'docs/images/'+path
    saveImage(imagePath)
    print imagePath
    