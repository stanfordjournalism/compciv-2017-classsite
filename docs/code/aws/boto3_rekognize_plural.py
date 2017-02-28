# https://boto3.readthedocs.io/en/latest/reference/services/rekognition.html#Rekognition.Client.detect_faces
import boto3
import requests
import json

SRC_IMAGE_BASE_URL = 'http://stash.compciv.org/2017/'
rekog = boto3.client('rekognition')


image_names = ['bush-2.jpg', 'clinton.jpg', 'obama.jpg', 'trump.jpg']


for iname in image_names:
    img_url = SRC_IMAGE_BASE_URL + iname
    img_bytes = requests.get(img_url).content
    rekog_response = rekog.detect_faces(Image={'Bytes': img_bytes},
                                Attributes=['ALL'])




