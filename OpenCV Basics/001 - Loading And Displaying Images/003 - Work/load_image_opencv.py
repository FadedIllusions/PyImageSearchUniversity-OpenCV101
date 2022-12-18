# python load_image_opencv.py -- image 30th_birthday.png

# Import Needed Packages
import argparse
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Input Image")
args = vars(ap.parse_args())

# Load Image From Disk, Grab Spacial Dimensions (Height, Width, Number Of Channels)
image = cv2.imread(args["image"])
(h,w,c) = image.shape[:3]

# Display Image Width, Height, Channels
print("Width: {} Pixels".format(w))
print("Height: {} Pixels".format(h))
print("Channels: {}".format(c))

# Display Image And Await Keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

# Save Image To Disk, Converting Filetype
cv2.imwrite("images/NewImage.jpg", image)

# Close All Windows And Cleanup
cv2.destroyAllWindows()