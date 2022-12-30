# python opencv_masking.py
# https://pyimagesearch.com/2021/01/19/image-masking-with-opencv/

# Import Needed Packages
import numpy as np
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/adrian.png",
				help="Path To Input Image")
args = vars(ap.parse_args())


# Load Image From Disk And Display
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# A Mask Is The Same Size As The Image We Wish To Mask
# Having Only Pixels Values Of 0 And 255,
# With 0 Being Ignored And 255 Being Kept
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (0,90), (290,450), 255, -1)
cv2.imshow("Rectangular Mask", mask)
cv2.waitKey(0)

# Apply Mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied To Image", masked)
cv2.waitKey(0)

# Create Circular Mask With Rad 100 Px
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (145,200), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Circular Mask", masked)
cv2.waitKey(0)

# Perform Needed Cleanup
cv2.destroyAllWindows()