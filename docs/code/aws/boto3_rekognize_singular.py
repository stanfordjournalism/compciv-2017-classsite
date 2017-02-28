# https://boto3.readthedocs.io/en/latest/reference/services/rekognition.html#Rekognition.Client.detect_faces
import boto3
import requests
rekog = boto3.client('rekognition')

# download the image bytes
img_resp = requests.get('http://stash.compciv.org/2017/trump.jpg')

img_bytes = img_resp.content

img = {'Bytes': img_bytes}
attlist = ['ALL']

# call the Rekognition API
rekog_response = rekog.detect_faces(Image=img, Attributes=attlist)
