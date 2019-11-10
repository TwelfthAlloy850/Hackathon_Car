
# Line detection using opencv.
# Helpful resource = https://pysource.com/2018/03/07/lines-detection-with-hough-transform-opencv-3-4-with-python-3-tutorial-21/
# Another helpful resource = https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/
# Detecting edges = https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html

################################################

import cv2
import numpy as np

################################################

# User input.

# Image to be analyzed:
image_name = 'test_image.png'
folder_path = '/Users/Lex/Library/Mobile Documents/com~apple~CloudDocs/Coding/Python/Hackathon/'

# For edge detection:
# Blue
lower_color_bound = np.array([30, 100, 60])
upper_color_bound = np.array([255, 255, 255])

################################################

image_path = folder_path + image_name
original_image = cv2.imread(image_path, 1)



### Detects edges ###
blurred_image = cv2.GaussianBlur(original_image, (5, 5), 0)

HSV_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)
masked_image = cv2.inRange(HSV_image, lower_color_bound, upper_color_bound)

edges = cv2.Canny(mask, 350, 450, apertureSize = 3)

# Draws the edges in an image
cv2.imwrite('edge.jpg', edges)



### Finds the lines based on the image ###

# This returns an array of r and theta values 
lines = cv2.HoughLines(edges,1,np.pi/180, 60)



### Draws the lines on the image ###

# The below for loop runs till r and theta values  
# are in the range of the 2d array
for i in range(len(lines)):
    for r,theta in lines[i]:

        # Stores the value of cos(theta) in a 
        a = np.cos(theta) 

        # Stores the value of sin(theta) in b 
        b = np.sin(theta) 

        # x0 stores the value rcos(theta) 
        x0 = a*r 

        # y0 stores the value rsin(theta) 
        y0 = b*r 

        # x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
        x1 = int(x0 + 1000*(-b)) 

        # y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
        y1 = int(y0 + 1000*(a)) 

        # x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
        x2 = int(x0 - 1000*(-b)) 

        # y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
        y2 = int(y0 - 1000*(a)) 

        # cv2.line draws a line in img from the point(x1,y1) to (x2,y2). 
        # (0,0,255) denotes the colour of the line to be  
        #drawn. In this case, it is red.  
        cv2.line(image,(x1,y1), (x2,y2), (0,0,255),2)

cv2.imwrite('linesDetected.jpg', image)



### Finds the key lines ###
sortedLines = sorted(lines, key = lambda lines: lines[0][1])

twoLines = []
twoLines.append(sortedLines[0][0].tolist())
twoLines.append(sortedLines[-1][0].tolist())



### Creates an image with the key lines ###
for i in range(len(twoLines)):
    for r,theta in twoLines:

        # Stores the value of cos(theta) in a 
        a = np.cos(theta) 

        # Stores the value of sin(theta) in b 
        b = np.sin(theta) 

        # x0 stores the value rcos(theta) 
        x0 = a*r 

        # y0 stores the value rsin(theta) 
        y0 = b*r 

        # x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
        x1 = int(x0 + 1000*(-b)) 

        # y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
        y1 = int(y0 + 1000*(a)) 

        # x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
        x2 = int(x0 - 1000*(-b)) 

        # y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
        y2 = int(y0 - 1000*(a)) 

        # cv2.line draws a line in img from the point(x1,y1) to (x2,y2). 
        # (0,0,255) denotes the colour of the line to be  
        #drawn. In this case, it is red.  
        two_lines_image = cv2.line(original_image,(x1,y1), (x2,y2), (0,0,255),2)

cv2.imwrite('twoLines.jpg', two_lines_image)

### Find the equation of each line ###
# (m, b)
two_line_eq = []
for i in range(len(twoLines)):

    # Stores the value of cos(theta) in a 
    a = np.cos(twoLines[i][1]) 

    # Stores the value of sin(theta) in b 
    b = np.sin(twoLines[i][1]) 

    # x0 stores the value rcos(theta) 
    x0 = a*r 

    # y0 stores the value rsin(theta) 
    y0 = b*r 

    # x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
    x1 = int(x0 + 1000*(-b)) 

    # y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
    y1 = int(y0 + 1000*(a)) 

    # x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
    x2 = int(x0 - 1000*(-b)) 

    # y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
    y2 = int(y0 - 1000*(a)) 

    # cv2.line draws a line in img from the point(x1,y1) to (x2,y2). 
    # (0,0,255) denotes the colour of the line to be  
    #drawn. In this case, it is red.

    m = (y2-y1)/(x2-x1)
    b = y1 - m*x1

    eq = [m,b]

    two_line_eq.append(eq)
        
print(two_line_eq)

# m1 - m2 = b2 - b1
# x = (b2 - b1)/(m1 - m2)

## Find the point of intersection? ###
# Does polar measure the angle of a line perpendicular to the actual line?
# x_intersect = ((two_line_eq[1][1] - two_line_eq[0][1]) / (two_line_eq[0][0] - two_line_eq[1][0]))
# print(x_intersect)

# # m1*x_intersect + b1
# y_intersect = ((two_line_eq[0][0] * x_intersect) + two_line_eq[0][1])
# print(y_intersect)

# intersection = cv2.line(original_image, (0,-48), (100,-194), (0,0,255),2)
# cv2.imwrite('intersection.jpg', intersection)

r1 = two_line_eq[0][0]
r2 = two_line_eq[1][0]
th1 = two_line_eq[0][1]
th2 = two_line_eq[1][1]

# x = ((r2 / sin(th2)) - (r1 / sin(th1))) / ((-cos(th1) / sin(th1)) + (cos(th2) / sin(th2)))
# numerator = ((two_line_eq[1][0] / np.sin(two_line_eq[1][1])) - (two_line_eq[0][0] / np.sin(two_line_eq[0][1])))
# denominator = ((-1*np.cos(two_line_eq[0][1]) / np.sin(two_line_eq[0][1]) + (np.cos(two_line_eq[1][1] / np.sin(two_line_eq[1][1])))))
# x = numerator / denominator

num = ((r2 / np.sin(th2)) - (r1 / np.sin(th1)))
denom = ((np.cos(th2) / np.sin(th2)) - (np.cos(th1) / np.sin(th1)))
x = num / denom

print(num, denom)
print(x)