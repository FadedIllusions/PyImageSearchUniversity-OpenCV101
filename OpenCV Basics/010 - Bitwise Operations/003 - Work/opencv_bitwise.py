# python opencv_bitwise.py
# https://pyimagesearch.com/2021/01/19/opencv-bitwise-and-or-xor-and-not/


# Import Needed Packages
import numpy as np
import cv2


# Draw A Rectangle
# StartX:25, StartY:25, EndX:275, EndY:275, Color:255, Filled(-1)
rectangle = np.zeros((300,300), dtype="uint8")
cv2.rectangle(rectangle, (25,25), (275,275), 255, -1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)


# Draw A Circle
#  Center StartX:150, Center StartY:150, Radius:150Px, Color:255, Filled(-1)
circle = np.zeros((300,300), dtype="uint8")
cv2.circle(circle, (150,150), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)


# Bitwise Operation (AND)
# True (Logical HIGH/1) When Both Compared Inputs Have Value Of HIGH/1
# That Is, Input_1 AND Input_2 Are True/HIGH/1
# In This Case, We Are Comparing And Displaying Areas Of The 300x300
# Canvas To See Which Areas Contain Both The Drawn Rectangle AND Circle
# (True/HIGH/1 > 0)
bitwiseAND = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAND)
cv2.waitKey(0)

cv2.destroyAllWindows()
AND_concat = cv2.hconcat([rectangle, circle, bitwiseAND])
cv2.imshow("Comparison", AND_concat)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Bitwise Operation (OR)
# True (Logical HIGH/1) When Either Of Compared Inputs Have Value Of HIGH/1
# Input_1 OR Input_2 Are True/HIGH/1 ... Or BOTH
bitwiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Circle", circle)
cv2.imshow("OR", bitwiseOR)
cv2.waitKey(0)

cv2.destroyAllWindows()
OR_concat = cv2.hconcat([rectangle, circle, bitwiseOR])
cv2.imshow("Comparison", OR_concat)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Bitwise Operation (XOR)
# Bitwise XOR, Or Exclusive OR, Is True (Logical HIGH/1)
# True (Logical HIGH/1) When Either Of Compared Inputs Have Value Of HIGH/1
# That Is, Input_1 OR Input_2; But, Not Both
bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Circle", circle)
cv2.imshow("XOR", bitwiseXOR)
cv2.waitKey(0)

cv2.destroyAllWindows()
XOR_concat = cv2.hconcat([rectangle, circle, bitwiseXOR])
cv2.imshow("Comparison", XOR_concat)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Bitwise Operation (NOT)
# True (Logical HIGH/1) When Input Is NOT True/HIGH/1
bitwiseNOT = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNOT)
cv2.waitKey(0)
cv2.destroyAllWindows()

v_concat = cv2.vconcat([AND_concat, OR_concat, XOR_concat])
cv2.imshow("Comparison", v_concat)
cv2.waitKey(0)


# Perform Needed Cleanup
cv2.destroyAllWindows()