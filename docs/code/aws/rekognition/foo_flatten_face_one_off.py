from facefinder import detect_faces
import json

source_path = 'http://stash.compciv.org/2017/obama.jpg'
results = detect_faces(source_path)
faces = results['FaceDetails']
src_face = faces[0]




flatface = {}
flatface['source'] = source_path
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



# let's see what it all looks like
# try printing it out as a string
txt = json.dumps(flatface, indent=2)






