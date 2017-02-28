"""
In this stage, all we're doing is wrapping up the logic that we need to
simplify the Rekognize API data. There's no need to actually call the API
over and over when we can use these cached data files:

http://stash.compciv.org/2017/obama.jpg.json
http://stash.compciv.org/2017/trump.jpg.json
http://stash.compciv.org/2017/trump-inaug.jpg.json
http://stash.compciv.org/2017/stanford-family.jpg.json
"""

resp = requests.get('http://stash.compciv.org/2017/obama.jpg.json')
results = json.loads(resp.text)
faces = results['FaceDetails']

def flatten_details(src_face):
    """
    Arguments:
        src_face is a dictionary of the kind returned by AWS Rekognize

    Returns:
        A simplified dictionary with just the interesting points
    """

    flatface = {}
    # can't add the 'source' attribute here because each face object
    # flatface['source'] = source_path
    flatface['face_confidence'] = round(src_face['Confidence'], 3)


# get the coordinates
bbox = src_face['BoundingBox']
flatface['left'] = round(bbox['Left'], 3)
flatface['top'] = round(bbox['Top'], 3)
flatface['width'] = round(bbox['Width'], 3)
flatface['height'] = round(bbox['Height'], 3)

# gender attributes
gender = src_face['Gender']
flatface['gender'] = gender['Value']
flatface['gender_confidence'] = round(gender['Confidence'], 3)

# add top emotion
emotions = src_face['Emotions']
if len(emotions) > 0: # at least one
    emot = emotions[0]
    flatface['main_emotion'] = emot['Type']
    flatface['main_emotion_confidence'] = round(emot['Confidence'])


# add smile confidence...
# not sure if 'Smile' is always in images
smile = src_face.get('Smile')
if smile:
    sval = smile['Confidence']
    # instead of having two columns for 'smile' and 'smile_confidence'
    # let's just have a 'smile' column to hold the 'Confidence' level
    # and set it to negative if smile['Value'] is False
    # ...what does False mean anyway?
    if smile['Value'] == False:
        flatface['is_smiling'] = -sval
    else:
        flatface['is_smiling'] = sval

# add has_facial_hair
beard = src_face['Beard']
mustache = src_face['Mustache']

if ((beard['Value'] == True and beard['Confidence'] > 75)
    or (mustache['Value'] == True and mustache['Confidence'] > 75)):

    flatface['has_hairy_face'] = True



def simplify_faces(source_path):
    """
    Convenient wrapper around
    """

    srcfaces = extract_faces(source_path)
    newfaces = []
    for f in srcfaces:
        fface = flatten_details(face)
        # have to add 'source' attribute, i.e. where the file came from
        # here because the flatten_details function has no
        # reference/knowledge of "source_path"
        fface['source'] = source_path

        newfaces.append(fface)

    return newfaces
