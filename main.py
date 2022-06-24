import cv2 as cv
import sys 
import numpy as np 

 #original image color bgr
img = cv.imread("./rc-car.jpg")

 # convert to RGB format
img_rgb = img.copy()
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # convert to grayscale
img_gry = img.copy()
img_gry = cv.cvtColor(img_gry, cv.COLOR_BGR2GRAY)
#back to BGR format so we can concatenate it back again
img_gry = cv.cvtColor(img_gry, cv.COLOR_GRAY2BGR)

#HLS format
img_hls = img.copy()
img_hls = cv.cvtColor(img_hls, cv.COLOR_BGR2HLS_FULL)

#annotate--adding text or notes to the images 
cv.putText(img,"BGR format", (100,780), cv.FONT_HERSHEY_COMPLEX, 1.5, (255,255,255), 2)
cv.putText(img_rgb,"BGR format", (100,780), cv.FONT_HERSHEY_COMPLEX, 1.5, (255,255,255), 2)
cv.putText(img_gry,"BGR format", (100,780), cv.FONT_HERSHEY_COMPLEX, 1.5, (255,255,255), 2)
cv.putText(img_hls,"HLS format", (100,780), cv.FONT_HERSHEY_COMPLEX, 1.5, (255,255,255), 2)

# need to display image side by side inform of a grid
# will now use numpy - 
# both images must be the same size and the same format as well to use concatenate
# axis=0 to display the stack vertically, axis=1 to display the axis horizontally
    
row1 = np.concatenate((img, img_rgb), axis = 1 )
row2 = np.concatenate((img_hls, img_gry), axis = 1 )
final_img = np.concatenate((row1, row2), axis = 0 )
cv.imshow("RC CAR", final_img)