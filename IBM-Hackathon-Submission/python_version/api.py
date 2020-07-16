from watson_developer_cloud import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from os.path import abspath
import json

from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('Api-Key-Here')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

with open('opencv_frame.png', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file=images_file,
        threshold='0.6',
        owners=["me"]).get_result()
    
    json_string = json.dumps(classes, indent=2)
    json_dictionary = json.loads(json_string)
#    print("images", ":", json_dictionary['images'][0]['classifiers'][1]['classes'][0]['class'])
    models = json_dictionary['images'][0]['classifiers']
    matchme = "MaskModelTest3_989931536"
    for model in models:
        if model["classifier_id"] == matchme:
            print("FOUND MSTCH")
            print(model["classes"][0]["class"])
            print(model["classes"][0]["score"])
            if (model["classes"][0]["class"] == "With Mask"):
                print("Here we launch the servo moter on jetsen")
            	
