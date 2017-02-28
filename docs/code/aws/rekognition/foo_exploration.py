#  https://boto3.readthedocs.io/en/latest/reference/services/rekognition.html#Rekognition.Client.detect_faces
import boto3
import requests

# Set up the client
session = boto3.Session(profile_name='default')
rek = session.client('rekognition')

# Download an image file
resp = requests.get('http://stash.compciv.org/2017/obama.jpg')

# get at its "bytes"
imgbytes = resp.content
rek_results = rek.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])

##################

import requests
resp = requests.get('http://stash.compciv.org/2017/trump-inaug.jpg')
img_filename = 'family-photo.jpg'
imgfile = open(img_filename, 'wb')
imgfile.write(resp.content)
imgfile.close()


##################
# reading from a file on your computer

import boto3

# Set up the client
session = boto3.Session(profile_name='default')
rek = session.client('rekognition')

# Open an image file on your computer
img_filename = 'family-photo.jpg'
imgfile = open(img_filename, 'rb')
imgbytes = imgfile.read()
imgfile.close()


rek_results = rek.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])


####################
# Let's try a file that has no faces at all
import requests
img_url = 'http://stash.compciv.org/2017/stanford-logo.png'
resp = requests.get(img_url)
imgbytes = resp.content
rek_results = rek.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])



#### Batch
import boto3
import json
from os.path import basename
import requests
from urllib.parse import urljoin

BASE_URL = 'http://stash.compciv.org/2017/'

# Set up the client
session = boto3.Session(profile_name='default')
rek = session.client('rekognition')

for fn in ['obama.jpg', 'trump.jpg', 'trump-inaug.jpg', 'stanford-family.jpg', 'stanford-logo.png']:
    url = urljoin(BASE_URL, fn)
    resp = requests.get(url)

    # get at its "bytes"
    imgbytes = resp.content
    rekres = rek.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])

    fname = basename(url) + '.json'

    with open(fname, 'w') as f:
        print("Writing to:", fname)
        txtdata = json.dumps(rekres, indent=2)
        f.write(txtdata)


