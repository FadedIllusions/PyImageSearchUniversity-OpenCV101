# python image_drawing.py
# https://pyimagesearch.com/2021/01/27/drawing-with-opencv/

# Import Needed Packages
import argparse
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/adrian.png",
	help="Path To Input Image")
args = vars(ap.parse_args())

# Load Image From Disk
image = cv2.imread(args["image"])

# Draw Circles Around Face, Two Filled Circles Covering Eyes,
# And A Rectangle Over Top Of Mouth
cv2.circle(image, (168,188), 90, (0,0,255), 2)
cv2.circle(image, (150,164), 10, (0,0,255), -1)
cv2.circle(image, (192,174), 10, (0,0,255), -1)
cv2.rectangle(image, (134,200), (186,218), (0,0,255), -1)

# Display Output Image
cv2.imshow("Output", image)
cv2.waitKey(0)

# Perform Necessary Cleanup
cv2.destroyAllWindows()
