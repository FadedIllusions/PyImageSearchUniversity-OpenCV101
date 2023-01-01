# python opencv_channels.py
# https://pyimagesearch.com/2021/01/23/splitting-and-merging-channels-with-opencv/

# Import Needed Packages
import numpy as np
import argparse
import cv2


# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/opencv_logo.png",
				help="Path To Input Image")
args = vars(ap.parse_args())


# Load Image And Grab Channels (BGR)
image = cv2.imread(args["image"])
(B,G,R) = cv2.split(image)

# Display Each Channel, Individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

# Visualize Each Channel In Color
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

# Merge Image And Display
merged = cv2.merge([B,G,R])
cv2.imshow("Merged Image", merged)
cv2.waitKey(0)


# Perform Needed Cleanup
cv2.destroyAllWindows()