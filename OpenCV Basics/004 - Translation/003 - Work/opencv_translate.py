# python opencv_translate.py

# Import Needed Packages
import numpy as np
import argparse
import imutils
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/opencv_logo.png", 
				help="Path To Input Image")
args = vars(ap.parse_args())

# Load And Display Image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Translating (Shifting) An Image Is Given By A NumPy Matrix In Form:
# [
#   [1,0,shiftX]
#   [0,1,shiftY]
# ]

# Shift Image 25 Pxs To Right And 50 Pxs Down
M = np.float32([[1,0,25], [0,1,50]])
shifted = cv2.warpAffine(image, M, (image.shape[1],image.shape[0]))
cv2.imshow("Shifted Down And Right", shifted)
cv2.waitKey(0)

# Shift 50 Pxs Left, 90 Pxs Up By Specifying Negative Values For
# X And Y Directions, Respectively
M = np.float32([[1,0,-50], [0,1,-90]])
shifted = cv2.warpAffine(image, M, (image.shape[1],image.shape[0]))
cv2.imshow("Shifted Up And Left", shifted)
cv2.waitKey(0)

# Use imutils Helper Function To Translate Image
# 100 Pxs Down In A Single Function Call
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

# Perform Needed Cleanup
cv2.destroyAllWindows()
