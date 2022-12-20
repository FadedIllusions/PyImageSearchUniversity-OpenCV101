# python opencv_resizing.py

# Import Needed Packages
import argparse
import imutils
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/adrian.png",
				help="Path To Input Image")
args = vars(ap.parse_args())

# Load Image And Display
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Resize Image To Be 150 Px Wide
# Calculate Aspect Ratio To Prevent Distortion
r = 150.0/image.shape[1]
dim = (150, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)

# Resize Image To Have A Height  Of 50 Px
# Calculate Aspect Ratio
r = 50.0/image.shape[0]
dim = (int(image.shape[1] * r), 50)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

# Let's Use imutils So As We Don't Have To Constantly Calculate Aspect Ratio
resized = imutils.resize(image, width=100)
cv2.imshow("imutils Resize", resized)
cv2.waitKey(0)

# Let's Preemptively Cleanup A Bit
cv2.destroyAllWindows()


# Construct List Of Interpolation Methods In OpenCV
methods = [
	("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
	("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
	("cv2.INTER_AREA", cv2.INTER_AREA),
	("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
	("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

# Iterate Through Interpolation Methods
for (name, method) in methods:
	# Increase Size Of Image By 3x Using Current Inter Method
	print("[INFO] {}".format(name))
	resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
	cv2.imshow("Method: {}".format(name), resized)
	cv2.waitKey(0)
	
# It Is Easier To Decrease Resolution Than To Increase
# Being As You Have More Data To Work With, 
# Rather Than Creating New Data

# Perform Necessary Cleanup
cv2.destroyAllWindows()