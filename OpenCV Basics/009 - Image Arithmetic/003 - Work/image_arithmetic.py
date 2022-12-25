# python image_arithmetic.py
# https://pyimagesearch.com/2021/01/19/image-arithmetic-opencv/


# Import Needed Packages
import numpy as np
import argparse
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/grand_canyon.png",
				help="Path To Input Image")
args = vars(ap.parse_args())

# Images Are Numpy Arrays Stored As Unsigned 8-Bit Integers (uint8)
# With Values In The Range [0, 255]. When Using The Add/Subtract
# Functions In OpenCV, These Values Will Be "Clipped" To This Range,
# Even If They Fall Outside Of The Range After Applying The Operation.

added = cv2.add(np.uint8([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))

print("Max Of 255: {}".format(added))
print("Min Of 0: {}".format(subtracted))

# Load And Display Image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Increase Px Intensities In Input Image By 100
# (Use Array Of Same Size As Image)
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Lighter", added)
cv2.waitKey(0)

# Darken Px Intensities By 50
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Darker", subtracted)
cv2.waitKey(0)


# Perform Needed Cleanup
cv2.destroyAllWindows()
