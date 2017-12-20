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
#     ScalingImages.py
#
#     How to scale an image (without being an element) in plain DrawBot?
#     Since the core DrawBot does not support w/h attrbiutes for images, 
#     it needs to be done by using the scale() function.
#
#     Unfortunately this also changes to x/y position scale, so when
#     drawing an image on the canvas, the position must be scaled the
#     other way around. In this example it doesn't matter, because the
#     scaled image is positioned at (0, 0).
#
from pagebot.contexts import defaultContext as context
import os # Import module that communicates with the file system.

if __name__ == '__main__':
    # Let's say we want to scale it to 50%. The 0.5 is the multiplication factor.
    newScale = 0.5
    # Define the path where to find the example image.
    path = 'docs/sources/'
    dstPath = 'docs/images/'
    for fileName in os.listdir(path):
        if fileName.startswith('.'):
                continue
        imagePath = path + fileName
        # Use the standard DrawBot function to get the width/height of the image from the file.
        w, h = context.imageSize(imagePath)


        # Make a page with the size of the scaled image, rounded to whole pixels.
        context.newDrawing()
        context.newPage(int(w*newScale), int(h*newScale))

        # Save the “graphics state“, just in case the script is extended later, where other 
        # operation need to work in 100%.
        context.save()
        context.scale(newScale) # Make all drawing scale to 50%
        context.image(imagePath, (0, 0)) # Draw the scaled image at the bottom-left corner. It fills the whole page.
        # Restore the graphics state, so DrawBot scaling is back to 100% after this.
        context.restore()
        # Note that resulting images may look sharper, by has 4.5x the size of the .jpg.
        dstImagePath = dstPath + fileName.replace('.','-%d.' % (newScale*100))
        print fileName, '-->', dstImagePath
        context.saveImage(dstImagePath)
	print 'Done'
