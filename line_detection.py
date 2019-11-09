
# Line detection using a Hough transformation.

import cv2
import numpy as np

# Imports the image.
image = cv2.imread('#PLACEHODER', cv2.IMREAD_COLOR)

# Converts the stll frame to greyscale.
grey_imgae = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detects edges using canny.
edges = cv2.Canny(gray, 50, 200)

# Gets the points to form the lines.
lines = cv2.HoughLinesP(edges, 1, np.pi/180, max_slider, minLineLength=10, maxLineGap=250)

# Draws each line.
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)

# Shows the new image.
cv2.imshow("Result", image)