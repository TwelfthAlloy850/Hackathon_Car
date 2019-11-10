# Hackathon Car
This is the code we used to make our car for the LI Teen Hacks hackathon.  We are team #13.  We mainly used Python and OpenCV.

To detect lines in the images, see line_detection.py.  The file name and file path must be changed to select the input photo.  Line_detection.py takes the image, filters for the color selected, and draws the two "strongest" lines.  The code creates a new image with the lines drawn in red over the original image.

To detect various objects in images, see sign_detection.py. This program uses OpenCV DNN (Deep Neural Network, for live image processing) and MobileNet-SSD v2 (a lightweight machine learning model) to detect objects detected by the raspberry pi's camera. If the camera detects a stop sign, the raspberry pi will tell the car to stop moving for several seconds and then resume moving.
