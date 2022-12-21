# python opencv_flip.py

# Import Needed Packages
import argparse
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

# Flip Image Horizontally
print("[INFO] Flipping Image Horizonally...")
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey(0)

# Flip Image Vertically
print("[INFO] Flipping Image Vertically...")
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)
cv2.waitKey(0)

# Flip Along Both Axis
print("[INFO] Flipping Image Horizontally And Vertically...")
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)

# Perform Necessary Cleanup
cv2.destroyAllWindows()
