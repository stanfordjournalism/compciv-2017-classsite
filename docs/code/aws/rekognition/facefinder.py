import boto3
import requests
from urllib.parse import urlparse


def get_api_client():
    session = boto3.Session(profile_name='default')
    return session.client('rekognition')


def is_this_a_url(pathstring):
    urlobj = urlparse(pathstring)
    if urlobj.netloc:
        return True
    else:
        return False

def get_image_bytes(path):
    if is_this_a_url(path):
        # if URL, then we use requests
        resp = requests.get(path)
        imgbytes = resp.content
    else:
        # assume it's a local file
        f = open(path, 'rb')
        imgbytes = f.read()
        f.close()
    return imgbytes


def detect_faces(path):
    """
    Arguments:
        path (string): a URL or filepath to an image you want to detect faces in.

    Returns:
        a dictionary of face-detection data results
    """

    rek = get_api_client()
    imgbytes = get_image_bytes(path)

    results = rek.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])

    return results
