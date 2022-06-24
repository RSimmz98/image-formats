    import cv2 as cv
    import sys 
    import numpy as np 

    #original image color bgr
    img = cv.imread("./me.jpg")

    # convert to RGB format
    img_rgb = img.copy()
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # convert to grayscale
    img_gry = img.copy()
    img_gry = cv.cvtColor(img_gry, cv.COLOR_BGR2GRAY)
    #back to BGR format so we can concatenate it back again
    img_gry = cv.cvtColor(img_gry, cv.COLOR_BGR2GRAY)

    #HLS format
    img_hls+
