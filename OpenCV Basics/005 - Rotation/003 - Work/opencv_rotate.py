# python opencv_rotate.py

# Import Needed Packages
import argparse
import imutils
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/opencv_logo.png",
				help="Path To Input Image")
args = vars(ap.parse_args())

# Load Image And Display
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Get Dimensions Of Image And Calculate Center
# Typically, Rotations Are Done About The Center Of An Image;
# However, Rotations Can Be Done About Any Arbitrary Point
(h,w) = image.shape[:2]
(cX,cY) = (w//2,h//2)

# Rotate Image -45 Deg (CW) Around Center (Scale 1.0)
M = cv2.getRotationMatrix2D((cX,cY), -45, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated 45 Degs CW", rotated)
cv2.waitKey(0)

# Rotate Image 90 Deg (CCW) Around Center
M = cv2.getRotationMatrix2D((cX,cY), 90, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated 90 Degs CCW", rotated)
cv2.waitKey(0)

# Use imutils To Rotate Image 180 Degs
rotated = imutils.rotate(image, 180)
cv2.imshow("Imutils 180 Degs", rotated)
cv2.waitKey(0)

# Rotate Image 33 Degs CCW
# Ensuring Entire Image Still Views In Viewing Area
rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated Without Cropping", rotated)
cv2.waitKey(0)

# Perform Necessary Cleanup
cv2.destroyAllWindows()