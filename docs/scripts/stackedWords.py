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
#     stackedWords.py
#
from random import shuffle

from pagebot.contexts import defaultContext as context
from pagebot.fonttoolbox.objects.font import getFontByName
from pagebot.style import A4, CENTER, DISPLAY_BLOCK, RIGHT, LEFT
from pagebot import Gradient, Shadow
from pagebot.toolbox.dating import now
# Find english words from the hyphenation list
from pagebot.toolbox.hyphenation import words
 
shadow = Shadow(offset=(6, -6), blur=10, color=(0.2, 0.2, 0.2, 0.5))

TYPOGRAPHIC_WORDS_S = """anti-aliasing, transparent, pixels, edges, letterform, outlines, sans-serif,  
typeface, design, style, aperture, counter shape, points, letterform, stroke, curves,
leading, straight, stem, stroke, connect, ascender, lowercase, letters, vertical, extends, 
x-height, marking, height, font, axis, stress, baseline, bowl, bracket, cap height, headline,
subhead, footnote, reference, component, accent, robofont, scripting, exhibition, photography,
identity, application, trafic, logo, logotype, line, baseline, baseline-J, TYPETR Upgrade,
crossbar, Italic, glyph, character, number, letter, mark, symbol, grotesk, hairline, typography,
lightest, font, family, weight, thinnest, stroke, hinting, hook, ink trap, joint, juncture,
kerning, space, pairs of letters, linespacing, ligature, loop, lobe, hanging figures, projection,
overshoot, point size, em size, roman, typography, shoulder, stacked, page, column, margin,
small caps, spine, transition, terminal, tail, tittle, tracking, vertex, weight, rounds, app,
optical size, width, variable, braces, superiors, inferiors, features, spacing, text, scripted,
magazine, newspaper, website, communication, TYPETR Upgrade, TYPETR Upgrade, Upgrade, Upgrade,
Upgrade, Hairline, ExtraLight, Thin, Book, Light, Regular, Medium, Semibold, Bold, Black, ExtraBlack, Ultrablack
"""
TYPOGRAPHIC_WORDS = []
for word in TYPOGRAPHIC_WORDS_S.split(','):
    if word:
        TYPOGRAPHIC_WORDS.append(word.strip())
shuffle(TYPOGRAPHIC_WORDS)

ROMAN_NAMES = []
ITALIC_NAMES = []
for fName in context.installedFonts():
    if fName.startswith('Upgrade'):
        if 'Italic' in fName:
            ITALIC_NAMES.append(fName)
        else:
            ROMAN_NAMES.append(fName)
shuffle(ROMAN_NAMES)       
shuffle(ITALIC_NAMES)

  
W, H = 600, 900
M = 20
MAX_WORD_LENGTH = 8
MIN_WORD_LENGTH = 4
LEADING = 3
FRAME_DURATION = 3

def buildStackedWords1(w, h, numPages):
    for pn in range(numPages):
        if random() < 0.8: 
            fontNames = ROMAN_NAMES
        else:
            fontNames = ITALIC_NAMES
        shuffle(fontNames)
        shuffle(TYPOGRAPHIC_WORDS)

        context.newPage(w, h)
        context.frameDuration(FRAME_DURATION)
        context.fill(1)
        context.rect(0, 0, w, h)
        
        y = h - M
        i = 0
        while y > M:
            features = dict(ss08=True)
            word = TYPOGRAPHIC_WORDS[i]
            if word[0].upper() != word[0] or word[-1].upper() != word[-1]: # Keep words in caps, if already in caps.
                word = word.capitalize()
            word += ' ' + TYPOGRAPHIC_WORDS[i+1]
            if len(word) < 16 or random() < 0.4:
                word = word.upper()
                features['case'] = True # Hyphens on cap level.
            bs = context.newString(word, style=dict(font=fontNames[-i],textFill=0, rLeading=1,
                openTypeFeatures=features), w=w-2*M)
            bx, by, bw, bh = bs.bounds()
            if y - bh + by < M:
                break
                    
            context.text(bs, ((w-bw-bx)/2, y-bh))
        
            #stroke(1,0, 0)
            #fill(None)
            #rect((w-bw-bx)/2, y-bh+by, bw+bx, bh-by)

            y -= bh-by+LEADING
            i += 2
            if i >= len(fontNames):
                i = 0
                shuffle(fontNames)
                shuffle(TYPOGRAPHIC_WORDS)
        
        
IMAGES = (
    ('../../docs/documents/stackedTypePages.pdf', W, H, 8, buildStackedWords1),    ('../../docs/images/stackedTypePages.png', W, H, 8, buildStackedWords1),    ('../../docs/images/stackedTypePages.gif', W, H, 8, buildStackedWords1),    ('../../docs/images/stackedTypePagesSmall.png', 400, 600, 6, buildStackedWords1),    ('../../docs/images/stackedTypePagesSmall.gif', 400, 600, 6, buildStackedWords1),    #('../../docs/documents/habitCoverPages1.pdf', W, H, now().year+1, buildCoverPages1),    #('../../docs/images/habitCoverPages1.png', W*3/4, H*3/4, now().year+1, buildCoverPages1),)        
      
for path, w, h, numPages, m in IMAGES:
    newDrawing()
    m(w, h, numPages)
    saveImage(path, multipage=True)
    print path
    