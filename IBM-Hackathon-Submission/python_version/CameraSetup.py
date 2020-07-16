import cv2
import os

from os.path import abspath
import json

from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('Api-Key-Here')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        # Make an API call use img_name as the img_src

        with open('opencv_frame.png', 'rb') as images_file:
            classes = visual_recognition.classify(
                images_file=images_file,
                threshold='0.6',
                owners=["me"]).get_result()
            
            json_string = json.dumps(classes, indent=2)
            json_dictionary = json.loads(json_string)
            print("images", ":", json_dictionary['images'][0]['classifiers'][1]['classes'][0]['class'])
            models = json_dictionary['images'][0]['classifiers']
            matchme = "MaskModelTest3_989931536"
            for model in models:
                if model["classifier_id"] == matchme:
                    print("FOUND MSTCH")
                    print(model["classes"][0]["class"])
                    print(model["classes"][0]["score"])
                    if (model["classes"][0]["class"] == "WithMask"):
                        print("Here we launch the servo moter on jetsen")
                        os.system("/opt/nvidia/jetson-gpio/samples/run_sample.sh test2.py")
                        continue
            	

        
        
cam.release()
cv2.destroyAllWindows()
