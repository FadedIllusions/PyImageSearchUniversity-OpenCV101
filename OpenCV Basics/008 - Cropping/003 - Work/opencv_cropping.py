# python opencv_cropping.py
# https://pyimagesearch.com/2021/01/19/crop-image-with-opencv/


# Import Needed Packages
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/adrian.png",
				help="Path To Input Image")
args = vars(ap.parse_args())

# Load And Display Image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Image Cropping Is Accomplished Using Numpy Array Slicing
# startY:endY, startX:endX
face = image[98:253, 102:225]
cv2.imshow("Face", face)
cv2.waitKey(0)

# Perform Necessary Cleanup
cv2.destroyAllWindows()
