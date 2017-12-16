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
from pagebot.toolbox.hyphenation import words
from pagebot.style import CENTER

TYPETR_BLUE = (0x25/255.0, 0x58/255.0, 0xAA/255.0)

WORDS = words() # Get English words

t = """*Design Design Space* is an online coaching environment to develop your design skills. Query your questions and improve your sketching. Acquire new techniques and research your way of presentating. In short, a space where you can design your design process. What kind of challenges do you experience in your daily work as a designer? Working closely together online with experienced designers and a group of other students, there is space to define your own study topics and challenges. In fact, such a selection and planning process is an integral part of the study itself. You tell us what you want, and together we’ll find a way to get there.

### Planning
By definition designers are bad planners. It seems to be fundamental to design. Too optimistic in the beginning – “There is still plenty of time”, a design is never finished – “The next one will always be better”. 

However, the fact that most designs are supposed to meet external requirements, the final deadline may have a much larger impact on the quality of the result, than the personal opinion of the designer. How do you make this apparent conflict work to your advantage?

### How much time do you need?
The core idea behind designing the design process, is that it doesn’t make a difference for how long you do it. A project of 1 hour, basically goes through the same stages (research – design – presentation) as a project of 1 year. Of course, it does matters how long you study something, for the level of details that can be addressed. But if you only have a day or a week for an assignment, then that is part of the requirements. The result can still be better than anything your customer would have done. 
How would you design such a design process better next time?

### 1 day • 1 week • 1 month • 1 season • 1 year
Study lengths range from 1 day, 1 week, 1 month, 1 season and possibly 1 year, whatever fits best to your plans, your practical possibilities and your financial situation.

### What does it cost?
* 1 day $150 (<a href="game.html">Design Game</a>, group of minimal 12)
* <a href="projects.html#oneWeek">1 week</a> $900 (7 days, group of 4 or more)
* <a href="projects.html#oneMonth">1 month</a> $1,900 (calendar month, individual or group)
* <a href="projects.html#oneSeason">1 season</a> $3,900 (3 calendar months, individual or group)
* <a href="projects.html#oneYear">1 year</a> $7,900 (individual or group)
Prices are per person. Discount or split payment for the month, season and year trainings can be discussed, depending on your personal situation. For corporate trainings, groups or customized requests, please <a href="mailto:info@designdesign.space?subject=Tell me more about Design Design Space">contact us</a>.
Students who whish to extend one training level into another, a 50% reduction is applied on previous payed tuition. E.g 1 day followed by 1 week: 1/2 $150 + $900 = $975. Or 1 week followed by 1 month: 1/2 $900 + $1,900 = $2,350. Or 1 week followed by 1 season: 1/2 $900 + $3,900 = $4,350

### What is the schedule & how to submit?
Every 6 months, in March and September, a new day-week-month-season-year sequence starts, most likely if there is enough participating students. 
Day-week sequences or single day Design Games can take place on other dates during the year, if the amount of participants makes it possible. Since working as a team of students a minimum amount of three is required, and also a mininum level of quality, motivation and experience.
Season and year-students are admitted after showing their portfolios and the result of a given assignment. Also they are asked to write a motivation and development plan.
Students that finish a training adequately, automatically get accepted for a next."""

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
UpgradeMiddleWeights = (    'Upgrade-Light',    'Upgrade-Book',    'Upgrade-Regular',    'Upgrade-Medium',    'Upgrade-Semibold',    'Upgrade-Bold',    'Upgrade-Black',    'Upgrade-LightItalic',    'Upgrade-BookItalic',    'Upgrade-RegularItalic',    'Upgrade-MediumItalic',    'Upgrade-SemiboldItalic',    'Upgrade-BoldItalic',    'Upgrade-BlackItalic',)

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
    path = 'docs/images/pic06page.png'
    iw, ih = imageSize(path)
    save()
    scale(0.35)
    image(path, (-65, -760))
    restore()
    
def image7(w, h):
    LIGHTS = (
        'Upgrade-Hairline',        'Upgrade-Thin',        'Upgrade-ExtraLight',        'Upgrade-Light',        'Upgrade-Book')
    LIGHTS2 = (
        'Upgrade-Thin',        'Upgrade-ExtraLight',        'Upgrade-Light',        'Upgrade-Book')
    newPage(w, h)
    r, g, b = 0.3*random(),0.3*random(),0.3*random()
    fill(r, g, b)
    rect(0, 0, w, h)
    fs = FormattedString('Q', font='Upgrade-Thin', fontSize=h*3/4, fill=(1,1,1,0.95))
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-36))
    fs = FormattedString('Typography', font=choice(LIGHTS2), fontSize=h/12, fill=(1,1,1,0.95))
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-2))
    fs = FormattedString('&', font=choice(LIGHTS2), fontSize=h/15, fill=(1,1,1,0.95))
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2-th-50))
    fs = FormattedString('Upgrade', font=choice(LIGHTS2), fontSize=h/15, fill=(1,1,1,0.95))
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h-18))
       
def image8(w, h):
    newPage(w, h)
    r, g, b = 0.1*random(),0.1*random(),0.5*random()
    fill(r, g, b)
    rect(0, 0, w, h)
    fs = FormattedString('Using\nUpgrade', font='Upgrade-RegularItalic', fontSize=22, fill=1, lineHeight=18)
    fs += FormattedString('\n\n\n     OK', font='Upgrade-Medium', fontSize=22, fill=1)
    tw, th = textSize(fs)
    text(fs, (12, h-30))
    fill(None)
    stroke(1)
    strokeWidth(1)
    rect(10, 18, w-20, 33)
        
def image9(w, h):
    REGULAR = (
        'Upgrade-Thin',        'Upgrade-ExtraLight',        'Upgrade-Light',        'Upgrade-Book',
        'Upgrade-Regular'
    )
    newPage(w, h)
    r, g, b = 0.1*random(),0.1*random(),0.1*random()
    fill(r, g, b)
    rect(0, 0, w, h)
    M = 8
    fs = FormattedString("""<html>\n<head>\n<style>\n   @font-face{\n      font-family:\n      'Upgrade-Regular';\n   }\n</style>\n</head>\n<body>""",
        font=choice(REGULAR), fontSize=14, fill=(0, 1, 0))
    tw, th = textSize(fs)
    textBox(fs, (M, -M, w*2, h))
        
def image10(w, h):
    newPage(w, h)
    fill(1)
    rect(0, 0, w, h)
    M = 14
    fs = FormattedString(t, font='Upgrade-Regular', fontSize=4, fill=0.2)
    tw, th = textSize(fs)
    textBox(fs, (M, M*1.5, w-2*M, h-2.5*M))
    fs = FormattedString('56', font='Upgrade-Regular', fontSize=4, fill=0.2)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, M*0.5))
        
def image11(w, h):
    newPage(w, h)
    r, g, b = TYPETR_BLUE
    fill(r, g, b)
    rect(0, 0, w, h)
    save()
    rotate(90)
    fs = FormattedString('Logo', font='Upgrade-UltraBlack', fontSize=h/2, fill=(0,1,1,0.4), tracking=-5.9)
    tw, th = textSize(fs)
    text(fs, (w/2-58, -70))

    fs = FormattedString('Logo', font='Upgrade-Semibold', fontSize=h/2, fill=(1,1,1,0.95))
    tw, th = textSize(fs)
    text(fs, (w/2-60, -70))
    fs = FormattedString('Logo', font='Upgrade-MediumItalic', fontSize=h/2, fill=(0.2,0,0.5,0.5), tracking=0.95)
    tw, th = textSize(fs)
    text(fs, (w/2-56, -70.8))
    restore()
            
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
    tc = 0.5*random(),0.2*random(),0.5*random()
    for n in range(200):
        fs = FormattedString(choice(WORDS), font=choice(upgradeFonts), fontSize=h/3, fill=random()*0.3+0.7, openTypeFeatures=dict(smcp=False, onum=False, ss09=False, frac=False, zero=False))
        text(fs, (-w/2+random()*w*2, -h/2+random()*h*2))
    fontName = choice(upgradeFonts)
    fontNameLabel = fontName.replace('-', ' ').replace('Italic', '')
    fs = FormattedString(fontNameLabel, font=fontName, fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide02(w, h):
    newPage(w, h)
    tc = 0.5*random(),0.2*random(),0.5*random()
    for n in range(200):
        fs = FormattedString(choice(WORDS), font=choice(upgradeFonts), fontSize=h/3, fill=random()*0.3+0.7)
        text(fs, (-w/2+random()*w*2, -h/2+random()*h*2))
    fontName = choice(upgradeFonts)
    fontNameLabel = fontName.replace('-', ' ').replace('Italic', '')
    fs = FormattedString(fontNameLabel, font=fontName, fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide03(w, h):
    newPage(w, h)
    tc = 0.5*random(),0.2*random(),0.5*random()
    for n in range(200):
        fs = FormattedString(choice(WORDS), font=choice(upgradeFonts), fontSize=h/3, fill=random()*0.3+0.7)
        text(fs, (-w/2+random()*w*2, -h/2+random()*h*2))
    fontName = choice(UpgradeMiddleWeights)
    fontNameLabel = fontName.replace('-', ' ').replace('Italic', '')
    fs = FormattedString(fontNameLabel, font=fontName, fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide04(w, h):
    newPage(w, h)
    tc = 0.5*random(),0.2*random(),0.5*random()
    for n in range(200):
        fs = FormattedString(choice(WORDS), font=choice(upgradeFonts), fontSize=h/3, fill=random()*0.3+0.7)
        text(fs, (-w/2+random()*w*2, -h/2+random()*h*2))
    fontName = choice(UpgradeMiddleWeights)
    fontNameLabel = fontName.replace('-', ' ').replace('Italic', '')
    fs = FormattedString(fontNameLabel, font=fontName, fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide05(w, h):
    newPage(w, h)
    tc = 0.5*random(),0.2*random(),0.5*random()
    for n in range(200):
        fs = FormattedString(choice(WORDS), font=choice(upgradeFonts), fontSize=h/3, fill=random()*0.3+0.7)
        text(fs, (-w/2+random()*w*2, -h/2+random()*h*2))
    fontName = choice(UpgradeMiddleWeights)
    fontNameLabel = fontName.replace('-', ' ').replace('Italic', '')
    fs = FormattedString(fontNameLabel, font=fontName, fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def slide06(w, h):
    newPage(w, h)
    tc = 0.5*random(),0.2*random(),0.5*random()
    for n in range(200):
        fs = FormattedString(choice(WORDS), font=choice(upgradeFonts), fontSize=h/3, fill=random()*0.3+0.7)
        text(fs, (-w/2+random()*w*2, -h/2+random()*h*2))
    fontName = choice(UpgradeMiddleWeights)
    fontNameLabel = fontName.replace('-', ' ').replace('Italic', '')
    fs = FormattedString(fontNameLabel, font=fontName, fontSize=h/3, fill=tc)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h/2+50))
        
def weights(w, h):
    M = 40
    TRACKING = 0.4
    newPage(w, h)
    fill(0)
    rect(0, 0, w, h)
    fSize = 34
    leading = fSize*1.2
    UpgradeWeights2 = list(UpgradeWeights[:])
    UpgradeWeights2.reverse()
    fs = FormattedString('')
    for fontName in UpgradeWeights:
        fs += FormattedString('ø', font=fontName, fill=1, fontSize=fSize, lineHeight=leading, align=CENTER, tracking=TRACKING)
    for fontName in UpgradeWeights2:
        fs += FormattedString('ø', font=fontName+'Italic', fill=1, fontSize=fSize, lineHeight=leading, align=CENTER, tracking=TRACKING)
    fs += FormattedString('\n', font=fontName, fontSize=fSize, lineHeight=leading)
    for fontName in UpgradeWeights:
        fs += FormattedString('Ø', font=fontName, fill=1, fontSize=fSize, lineHeight=leading, align=CENTER)
    for fontName in UpgradeWeights2:
        fs += FormattedString('Ø', font=fontName+'Italic', fill=1, fontSize=fSize, lineHeight=leading, align=CENTER, tracking=TRACKING)
    fs += FormattedString('\n', font=fontName, fontSize=fSize, lineHeight=leading)
    for fontName in UpgradeWeights:
        fs += FormattedString('$', font=fontName, fill=1, fontSize=fSize, lineHeight=leading, align=CENTER, tracking=TRACKING)
    for fontName in UpgradeWeights2:
        fs += FormattedString('$', font=fontName+'Italic', fill=1, fontSize=fSize, lineHeight=leading, align=CENTER, tracking=TRACKING)
    fs += FormattedString('\n', font=fontName, fontSize=fSize, lineHeight=leading)
    for fontName in UpgradeWeights:
        fs += FormattedString('¢', font=fontName, fill=1, fontSize=fSize, lineHeight=leading, align=CENTER, tracking=TRACKING)
    for fontName in UpgradeWeights2:
        fs += FormattedString('¢', font=fontName+'Italic', fill=1, fontSize=fSize, lineHeight=leading, align=CENTER, tracking=TRACKING)
    fs += FormattedString('\n', font=fontName, fontSize=fSize, lineHeight=leading)
    for fontName in UpgradeWeights:
        fs += FormattedString('0', font=fontName, fill=1, fontSize=fSize, lineHeight=leading, openTypeFeatures=dict(zero=True), align=CENTER, tracking=TRACKING)
    for fontName in UpgradeWeights2:
        fs += FormattedString('0', font=fontName+'Italic', fill=1, fontSize=fSize, lineHeight=leading, openTypeFeatures=dict(zero=True), align=CENTER, tracking=TRACKING)
    fs += FormattedString('\n', font=fontName, fontSize=fSize, lineHeight=leading)
    for fontName in UpgradeWeights:
        fs += FormattedString('0', font=fontName, fill=1, fontSize=fSize, lineHeight=leading, openTypeFeatures=dict(zero=False), align=CENTER, tracking=TRACKING)
    for fontName in UpgradeWeights2:
        fs += FormattedString('0', font=fontName+'Italic', fill=1, fontSize=fSize, lineHeight=leading, openTypeFeatures=dict(zero=False), align=CENTER, tracking=TRACKING)
    fs += FormattedString('\n', font=fontName, fontSize=fSize, lineHeight=leading)
    for fontName in UpgradeWeights:
        fs += FormattedString('A', font=fontName, fill=1, fontSize=fSize, lineHeight=leading, openTypeFeatures=dict(zero=False), align=CENTER, tracking=TRACKING)
    for fontName in UpgradeWeights2:
        fs += FormattedString('A', font=fontName+'Italic', fill=1, fontSize=fSize, lineHeight=leading, openTypeFeatures=dict(zero=False), align=CENTER, tracking=TRACKING)
    fs += FormattedString('\n', font=fontName, fontSize=fSize, lineHeight=leading)
    for fontName in UpgradeWeights:
        fs += FormattedString('a', font=fontName, fill=1, fontSize=fSize, lineHeight=leading, openTypeFeatures=dict(zero=False), align=CENTER, tracking=TRACKING)
    for fontName in UpgradeWeights2:
        fs += FormattedString('a', font=fontName+'Italic', fill=1, fontSize=fSize, lineHeight=leading, openTypeFeatures=dict(zero=False), align=CENTER, tracking=TRACKING)
    fs += FormattedString('\n', font=fontName, fontSize=fSize, lineHeight=leading)
    for fontName in UpgradeWeights:
        fs += FormattedString('&', font=fontName, fill=1, fontSize=fSize, lineHeight=leading, openTypeFeatures=dict(zero=False), align=CENTER, tracking=TRACKING)
    for fontName in UpgradeWeights2:
        fs += FormattedString('&', font=fontName+'Italic', fill=1, fontSize=fSize, lineHeight=leading, openTypeFeatures=dict(zero=False), align=CENTER, tracking=TRACKING)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h-M))
     
def image45st5th(w, h):
    newPage(w, h)
    fill(1)
    rect(0, 0, w, h)
    fName = 'Upgrade-Regular'
    fSize = w/4.5
    leading = fSize*1.3
    fs = FormattedString('42', font=fName, fontSize=fSize, fill=0)
    fs +=  FormattedString('st', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(sups=True))
    fs +=  FormattedString(' 5', font=fName, fontSize=fSize, fill=0)
    fs +=  FormattedString('th\n', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(sups=True))
    fs +=  FormattedString('C', font=fName, fontSize=fSize, fill=0, lineHeight=leading)
    fs +=  FormattedString('12', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(sinf=True))
    fs +=  FormattedString('H', font=fName, fontSize=fSize, fill=0)
    fs +=  FormattedString('22', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(sinf=True))
    fs +=  FormattedString('O', font=fName, fontSize=fSize, fill=0)
    fs +=  FormattedString('11\n', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(sinf=True))

    fs +=  FormattedString('(x', font=fName, fontSize=fSize, fill=0, lineHeight =leading)
    fs +=  FormattedString('2', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(sinf=True))
    fs +=  FormattedString('–x', font=fName, fontSize=fSize, fill=0)
    fs +=  FormattedString('1', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(sinf=True))
    fs +=  FormattedString(')', font=fName, fontSize=fSize, fill=0)
    fs +=  FormattedString('2\n', font=fName, fontSize=fSize, fill=0, lineHeight=leading, openTypeFeatures=dict(sups=True))
    
    fs +=  FormattedString('x', font=fName, fontSize=fSize, fill=0, lineHeight=leading)
    fs +=  FormattedString('n', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(sups=True))
    fs +=  FormattedString('+y', font=fName, fontSize=fSize, fill=0)
    fs +=  FormattedString('n', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(sups=True))
    fs +=  FormattedString('=z', font=fName, fontSize=fSize, fill=0)
    fs +=  FormattedString('n\n', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(sups=True))

    fs +=  FormattedString('45.63cm', font=fName, fontSize=fSize, fill=0, lineHeight=leading, openTypeFeatures=dict(lnum=True))
    fs +=  FormattedString('3\n', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(sups=True))
    fs +=  FormattedString('$149', font=fName, fontSize=fSize, fill=0, lineHeight=leading)
    fs +=  FormattedString('99', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(sups=True))

    print listOpenTypeFeatures(fName)
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h-72))

def fractions(w, h):
    newPage(w, h)
    fill(1)
    rect(0, 0, w, h)
    fName = 'Upgrade-Regular'
    fSize = w/7
    leading = fSize*1.3
    fs = FormattedString('23/47 * 3/17 = 69/799', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(frac=True))
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h-40))
      
def smallcaps(w, h):
    newPage(w, h)
    fill(1)
    rect(0, 0, w, h)
    fName = 'Upgrade-Regular'
    fSize = w/7
    leading = fSize*1.3
    fs = FormattedString('Upgrade Caps\n', font=fName, fontSize=fSize, fill=0)
    fs += FormattedString('Upgrade Caps\n', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(smcp=True))
    fs += FormattedString('Upgrade Caps\n', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(c2sc=True))
    fs += FormattedString('Upgrade Caps', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(smcp=True, c2sc=True))
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h-40))
      
def tablefigures(w, h):
    newPage(w, h)
    fill(1)
    rect(0, 0, w, h)
    fName = 'Upgrade-Regular'
    fSize = w/7
    leading = fSize*1.3
    fs = FormattedString('€3.428,95\n', font=fName, fontSize=fSize, fill=0)
    fs += FormattedString('€3.428,95', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(tnum=True))
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h-40))
      
def zeroslash(w, h):
    newPage(w, h)
    fill(1)
    rect(0, 0, w, h)
    fName = 'Upgrade-Regular'
    fSize = w/7
    leading = fSize*1.3
    fs = FormattedString('€1.200.000,–\n', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(zero=False, case=True))
    fs += FormattedString('€1.200.000,–', font=fName, fontSize=fSize, fill=0, openTypeFeatures=dict(zero=True, case=True))
    tw, th = textSize(fs)
    text(fs, (w/2-tw/2, h-40))
      
IMAGES_2 = (
    ('pic01.gif', 384, 182, image1),    ('pic02.png', 384, 182, image2),    ('pic03.png', 384, 182, image3),    ('pic04.png', 384, 182, image4),    ('pic05.png', 282, 290, image5),    ('pic06.png', 102, 152, image6),    ('pic07.jpg', 102, 152, image7),    ('pic08.jpg', 102, 152, image8),    ('pic09.jpg', 102, 152, image9),    ('pic10.jpg', 102, 152, image10),    ('pic11.jpg', 102, 152, image11),    ('pic12.jpg', 78, 78, image12),    ('pic13.jpg', 78, 78, image13),    ('pic14.jpg', 78, 78, image14),    ('pic15.jpg', 78, 78, image15),    ('pic16.jpg', 78, 78, image16),    ('slide01.jpg', 1200, 440, slide01),    ('slide02.jpg', 1200, 440, slide02),    ('slide03.jpg', 1200, 440, slide03),
    ('slide04.jpg', 1200, 440, slide04),
    ('slide05.jpg', 1200, 440, slide05),
    ('slide06.jpg', 1200, 440, slide06),
    ('glyphsbyweights.png', 700, 400, weights),
)
IMAGES = (
    ('45st5th.png', 275, 500, image45st5th),
    ('fraction.png', 275, 55, fractions),
    ('smallcaps.png', 275, 200, smallcaps),
    ('tablefigures.png', 275, 100, tablefigures),
    ('zeroslash.png', 275, 100, zeroslash),
)        
      
for path, w, h, m in IMAGES:
    newDrawing()
    m(w, h)
    imagePath = 'docs/images/'+path
    saveImage(imagePath)
    print imagePath
    