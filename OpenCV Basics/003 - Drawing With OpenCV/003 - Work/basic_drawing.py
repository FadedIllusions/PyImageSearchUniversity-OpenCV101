# python basic_drawing.py
# https://pyimagesearch.com/2021/01/27/drawing-with-opencv/

# Import Needed Packages
import numpy as np
import cv2

# Init Our Canvas As A 300x300 Px Image With 3 Channels
# (Red, Green, Blue) With A Black Background
canvas = np.zeros((300, 300, 3), dtype="uint8")
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw Greeb Line From TL Corner To BR
green = (0, 255, 0)
cv2.line(canvas, (0,0), (300,300), green)
cv2.imshow("Canvas Green Line", canvas)
cv2.waitKey(0)

# Draw 3 Px Thick Line From TR Corner To BL
red = (0, 0, 255)
cv2.line(canvas, (300,0), (0,300), red, 3)
cv2.imshow("Canvas Red Line", canvas)
cv2.waitKey(0)

# Draw Green 50x50 Px Square, Starting At 10,10 And Ending At 60,60
cv2.rectangle(canvas, (10,10), (60,60), green)
cv2.imshow("Canvas Green Rectangle", canvas)
cv2.waitKey(0)

# Draw Another Rectangle, Red With 5 PX Thickness
cv2.rectangle(canvas, (50,200), (200,225), red, 5)
cv2.imshow("Canvas Red Rectangle", canvas)
cv2.waitKey(0)

# Draw Final, Filled-In Blue Rectangle
blue = (255, 0, 0)
cv2.rectangle(canvas, (200,50), (225,125), blue, -1)
cv2.imshow("Canvas Filled Blue Rectangle", canvas)
cv2.waitKey(0)

# Reinit Canvas As Empty Array, Compute Center Coords
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX,centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
white = (255,255,255)

# Loop Over Increasing Radii, From 25 Px To 150 Px In 25 Px Increments
for r in range(0,175,25):
	# Draw White Circle With Current Radius Size
	cv2.circle(canvas, (centerX,centerY), r, white)
	
# Display
cv2.imshow("New Canvas", canvas)
cv2.waitKey(0)

# Reinit Canvas Again
canvas = np.zeros((300, 300, 3), dtype="uint8")

# Draw 25 Random Circles
for i in range(0,25):
	# Randomly Generate A Radius Size Between 5 And 200
	# Generate Random Color
	# Pick Random Point To Draw Circle
	radius = np.random.randint(5, high=200)
	color = np.random.randint(0, high=256, size=(3,)).tolist()
	pt = np.random.randint(0, high=300, size=(2,))
	
	# Draw Circle To Canvas
	cv2.circle(canvas, tuple(pt), radius, color, -1)
	
# Display To Screen
cv2.imshow("Random Circles", canvas)
cv2.waitKey(0)

# Perform Necessary Cleanup
cv2.destroyAllWindows()
