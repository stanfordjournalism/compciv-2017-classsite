from facefinder import detect_faces
import json


source_path = 'http://stash.compciv.org/2017/obama.jpg'

results = detect_faces(source_path)

faces = results['FaceDetails']
src_face = faces[0]

flatface = {}
flatface['source'] = source_path
flatface['face_confidence'] = round(src_face['Confidence'], 3)

# gender attributes
flatface['gender'] = src_face['Gender']['Value']
flatface['gender_confidence'] = round(src_face['Gender']['Confidence'], 3)

# get the coordinates
bbox = src_face['BoundingBox']
flatface['left'] = bbox['Left']
flatface['top'] = bbox['Top']
flatface['width'] = bbox['Width']
flatface['height'] = bbox['Height']





# image quality
flatface['brightness'] = round(src_face['Quality']['Brightness'], 3)
flatface['sharpness'] = round(src_face['Quality']['Sharpness'], 3)



# get the pose data

# flatface['pitch'] = round(src_face['Pose']['Pitch'], 3)
# flatface['roll'] = round(src_face['Pose']['Roll'], 3)
# flatface['yaw'] = round(src_face['Pose']['Yaw'], 3)

# simplified
for k, v in src_face['Pose'].items():
    flatface[k.lower()] = round(v, 3)
