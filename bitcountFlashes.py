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
#     bitcountFlashes.py
#
from pagebot.contexts import defaultContext as context

PATH = 'docs/images/bitcountFlashes.gif'

IMAGE_PATHS = (
    ('bitcountFlashes1.jpg', 4),    ('bitcountFlashes2.jpg', 2),    ('bitcountFlashes1.jpg', 1),    ('bitcountFlashes2.jpg', 2),    ('bitcountFlashes1.jpg', 1),    ('bitcountFlashes2.jpg', 1),
    ('bitcountFlashes3.jpg', 1),
    ('bitcountFlashes2.jpg', 1),
    ('bitcountFlashes3.jpg', 1),
    ('bitcountFlashes2.jpg', 1),
    ('bitcountFlashes3.jpg', 1),
    ('bitcountFlashes2.jpg', 1),
    ('bitcountFlashes3.jpg', 8),
    ('bitcountFlashes1.jpg', 1),
    ('bitcountFlashes2.jpg', 2),
    ('bitcountFlashes3.jpg', 14),
    ('bitcountFlashes2.jpg', 1),
    ('bitcountFlashes3.jpg', 20),
)
W, H = 1340/2, 560/2
M = 60
for imageName, duration in IMAGE_PATHS:
    for n in range(duration):
        context.newPage(W, H)
        context.frameDuration(0.1)
        context.image('docs/images/'+imageName, (-2*M-40, -M/2), w=W+2*M)
         
context.saveImage(PATH)
    