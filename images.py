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
TYPETR_BLUE = (0x25/255.0, 0x58/255.0, 0xAA/255.0)

upgradeFonts = []
from random import choice
for fontName in installedFonts():
    if 'Upgrade' in fontName:
        upgradeFonts.append(fontName)  
print upgradeFonts
UpgradeWeightsItalic = (
    'Upgrade-HairlineItalic',    'Upgrade-ThinItalic',    'Upgrade-ExtraLightItalic',    'Upgrade-LightItalic',    'Upgrade-BookItalic',    'Upgrade-RegularItalic',    'Upgrade-MediumItalic',    'Upgrade-SemiboldItalic',    'Upgrade-BoldItalic',    'Upgrade-BlackItalic',    'Upgrade-ExtraBlackItalic',    'Upgrade-UltraBlackItalic',)
UpgradeWeights = (    'Upgrade-Hairline',    'Upgrade-Thin',    'Upgrade-ExtraLight',    'Upgrade-Light',    'Upgrade-Book',    'Upgrade-Regular',    'Upgrade-Medium',    'Upgrade-Semibold',    'Upgrade-Bold',    'Upgrade-Black',    'Upgrade-ExtraBlack',    'Upgrade-UltraBlack',)
masterWeights = (
    'Upgrade-Hairline',    'Upgrade-Light',    'Upgrade-Medium',    'Upgrade-Bold',    'Upgrade-UltraBlack',    
)
def image1(w, h):
    for frame in range(len(UpgradeWeights)):
        newPage(w, h)
        frameDuration(0.25)
        fill(1)
        rect(0, 0, w, h)
        for n in range(len(UpgradeWeights)):
            if frame == n:
                strokeC = TYPETR_BLUE
                sw = 0.5
            else:
                strokeC = 0.2
                sw = 0.1
            weightName = UpgradeWeights[n]
            fs = FormattedString('a', font=weightName, fontSize=h*1.5, fill=None, stroke=strokeC, strokeWidth=sw)
            tw, th = textSize(fs)
            text(fs, (w/4-tw/2, h/2-th/5-5))
            weightName = UpgradeWeightsItalic[n]
            fs = FormattedString('a', font=weightName, fontSize=h*1.5, fill=None, stroke=strokeC, strokeWidth=sw)
            tw, th = textSize(fs)
            text(fs, (w*3/4-tw/2-20, h/2-th/5-5))

    for frame in range(len(UpgradeWeights)-1, -1, -1):
        newPage(w, h)
        frameDuration(0.25)
        fill(1)
        rect(0, 0, w, h)
        for n in range(len(UpgradeWeights)):
            if frame == n:
                strokeC = TYPETR_BLUE
                sw = 0.5
            else:
                strokeC = 0.2
                sw = 0.1
            weightName = UpgradeWeights[n]
            fs = FormattedString('a', font=weightName, fontSize=h*1.5, fill=None, stroke=strokeC, strokeWidth=sw)
            tw, th = textSize(fs)
            text(fs, (w/4-tw/2, h/2-th/5-5))
            weightName = UpgradeWeightsItalic[n]
            fs = FormattedString('a', font=weightName, fontSize=h*1.5, fill=None, stroke=strokeC, strokeWidth=sw)
            tw, th = textSize(fs)
            text(fs, (w*3/4-tw/2-20, h/2-th/5-5))
       
def image2(w, h):
    newPage(w, h)
    r, g, b = TYPETR_BLUE
    fill(r, g, b)
    rect(0, 0, w, h)
    fs = FormattedString('')
    glyphs = (
        ('H', dict(smcp=False)),
        ('h', dict(smcp=True)),
        ('2', dict(smcp=False, sinf=True)),
        ('O', dict(smcp=False, sinf=False)),
        ('3', dict(smcp=False, sinf=False, sups=True)),
        ('J', dict(smcp=False, ss08=False, sups=False)),
        ('J', dict(smcp=False, ss08=True)), 
        ('g', dict(smcp=False, ss08=False, ss09=False)),
        ('g', dict(smcp=False, ss09=True)), 
    )
    for glyph, features in glyphs:
        fs += FormattedString(glyph, font='Upgrade-Regular', fontSize=h/2.2, fill=1,
            openTypeFeatures=features )
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-25))
         
def image3(w, h):
    newPage(w, h)
    fill(0)
    rect(0, 0, w, h)
    fs = FormattedString('')
    for masterWeight in masterWeights:
        fs += FormattedString('e', font=masterWeight, fontSize=h*2/3, fill=1)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, 20))
    fs = FormattedString('')
    for masterWeight in masterWeights:
        fs += FormattedString('e', font=masterWeight+'Italic', fontSize=h*2/3, fill=1)
    #tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+10))
        
def image4(w, h):
    newPage(w, h)
    fill(0.8)
    rect(0, 0, w, h)
    s = '€12 $340 ¥56,897'
    fs = FormattedString(s, font='Upgrade-Book', fontSize=h/3.7, fill=0)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, 130))
    s = '€12 $340 ¥56,897'
    fs = FormattedString(s, font='Upgrade-Book', fontSize=h/3.7, fill=0, openTypeFeatures=dict(onum=True))
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, 75))
    s = '$12,340 ¥56,897 11/23'
    fs = FormattedString(s, font='Upgrade-Book', fontSize=h/3.7, fill=0, openTypeFeatures=dict(smcp=True, onum=False, frac=True, zero=True))
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, 20))
        
def image5(w, h):
    newPage(w, h)
    fill(0.8, 0, 0.1)
    rect(0, 0, w, h)
    fs = FormattedString('Corporate', font='Upgrade-Thin', fontSize=h/3, fill=1,
    openTypeFeatures=dict(smcp=False, onum=False, frac=False, zero=False))
    tw, th = textSize(fs)
    y = 48
    text(fs, (w/2-tw/2, h-y))
    fs = FormattedString('Identity', font='Upgrade-Book', fontSize=h/3, fill=(1, 1, 1, 0.75),
    openTypeFeatures=dict(smcp=False, onum=False, frac=False, zero=False))
    tw, th = textSize(fs)
    y += 45
    text(fs, (w/2-tw/2, h-y))
    fs = FormattedString('Publications', font='Upgrade-Regular', fontSize=h/4, fill=1,
    openTypeFeatures=dict(smcp=False, onum=False, frac=False, zero=False))
    tw, th = textSize(fs)
    y += 40
    text(fs, (w/2-tw/2, h-y))
    fs = FormattedString('Online', font='Upgrade-UltraBlack', fontSize=h/2.5, fill=(1, 1, 1, 0.5),
    openTypeFeatures=dict(smcp=False, onum=False, frac=False, zero=False))
    tw, th = textSize(fs)
    y += 65
    text(fs, (w/2-tw/2, h-y))
    fs = FormattedString('Applications', font='Upgrade-Regular', fontSize=h/4, fill=1,
    openTypeFeatures=dict(smcp=False, onum=False, frac=False, zero=False))
    tw, th = textSize(fs)
    y += 35
    text(fs, (w/2-tw/2, h-y))
        
def image6(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#6', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image7(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#7', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image8(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#8', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image9(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('I#9', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image10(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#10', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image11(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#11', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image12(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#12', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image13(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#13', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image14(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#14', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image15(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#15', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def image16(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('#16', font=choice(upgradeFonts), fontSize=h*3/4, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th/2))
        
def slide01(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('TYPETR Upgrade', font=choice(upgradeFonts), fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide02(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('TYPETR Upgrade', font=choice(upgradeFonts), fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide03(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('TYPETR Upgrade', font=choice(upgradeFonts), fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide04(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('TYPETR Upgrade', font=choice(upgradeFonts), fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide05(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('TYPETR Upgrade', font=choice(upgradeFonts), fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide06(w, h):
    newPage(w, h)
    tc = random(),random(),random()
    fill(1-tc[0], 1-tc[1], 1-tc[2])
    rect(0, 0, w, h)
    fs = FormattedString('TYPETR Upgrade', font=choice(upgradeFonts), fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
        
         
IMAGES = (
    ('pic01.gif', 384, 182, image1),    ('pic03.svg', 384, 182, image3),    ('pic04.svg', 384, 182, image4),    ('pic05.svg', 282, 242, image5),    ('pic06.jpg', 102, 152, image6),    ('pic07.jpg', 102, 152, image7),    ('pic08.jpg', 102, 152, image8),    ('pic09.jpg', 102, 152, image9),    ('pic10.jpg', 102, 152, image10),    ('pic11.jpg', 102, 152, image11),    ('pic12.jpg', 78, 78, image12),    ('pic13.jpg', 78, 78, image13),    ('pic14.jpg', 78, 78, image14),    ('pic15.jpg', 78, 78, image15),    ('pic16.jpg', 78, 78, image16),    ('slide01.jpg', 1200, 440, slide01),    ('slide02.jpg', 1200, 440, slide02),    ('slide03.jpg', 1200, 440, slide03),
    ('slide04.jpg', 1200, 440, slide04),
    ('slide05.jpg', 1200, 440, slide05),
    ('slide06.jpg', 1200, 440, slide06),
    ('pic02.svg', 384, 182, image2),)        
      
for path, w, h, m in IMAGES:
    newDrawing()
    m(w, h)
    imagePath = 'docs/images/'+path
    saveImage(imagePath)
    print imagePath
    