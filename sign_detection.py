'''
This program uses the MobileNet-SSD v2 (a machine learning model good for Tensorflow-Object
Detecion Lite) and OpenCV DNN (Deep Neural Networks, for live data processing/object detection)
to determine what an object is. It can detect many basic objects, most of which could be
encourtered by the car. The program stops the car at stop signs.
'''
import cv2
import picamera
from time import sleep

# Pretrained classes in the model
classNames = {0: 'background',
              1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
              7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
              13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
              18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
              24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
              32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
              37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
              41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
              46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
              51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
              56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
              61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
              67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
              75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
              80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
              86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}


def id_class_name(class_id, classes):
    for key, value in classes.items():
        if class_id == key:
            return value


# Loading model
#please download these files from here: https://github.com/rdeepc/ExploreOpencvDnn/tree/master/models
#the program will not work without them
model = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb',
                                      'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')
#PiCamera setup
camera = PiCamera()
camera.rotation = 180

while running:
    #Use PiCamera to take a picture for analysis and loop this when done analyzing
    #if not using PiCamera, can change directory 
    camera.capture("/home/pi/Desktop/analyze.jpg")
    image = cv2.imread("/home/pi/Desktop/analyze.jpg")

    image_height, image_width, _ = image.shape

    model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))
    output = model.forward()

    #determine type of object
    for detection in output[0, 0, :, :]:
        confidence = detection[2]
        if confidence > .5:
            class_id = detection[1]
            class_name=id_class_name(class_id,classNames)
            print(str(str(class_id) + " " + str(detection[2])  + " " + class_name))
            #if you want to see a visual example of the objects detected, uncomment the following code (and lines 80 and 83-4):
            '''box_x = detection[3] * image_width
            box_y = detection[4] * image_height
            box_width = detection[5] * image_width
            box_height = detection[6] * image_height
            cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=1)
            cv2.putText(image,class_name ,(int(box_x), int(box_y+.05*image_height)),cv2.FONT_HERSHEY_SIMPLEX,(.005*image_width),(0, 0, 255))
            '''
    #if this is a stop sign, stop for 3 seconds, then resume
    if class_name=="stop sign":
        print("this is a stop sign")
        e.ChangeDutyCycle(7.5)
        sleep(3)
        e.ChangeDutyCycle(8)


    #cv2.imshow('image', image)
    # cv2.imwrite("image_box_text.jpg",image)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
