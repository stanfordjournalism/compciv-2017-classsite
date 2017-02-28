from facefinder import detect_faces

logo_url = 'http://stash.compciv.org/2017/stanford-logo.png'
obama_url = 'http://stash.compciv.org/2017/obama.jpg'
family_url = 'http://stash.compciv.org/2017/stanford-family.jpg'

# explore results for photo with an obvious face
results = detect_faces(obama_url)

type(results)
results.keys()
results['OrientationCorrection']
results['ResponseMetadata']
results['FaceDetails']


# We know that this image has one face
fdetails = results['FaceDetails']
type(fdetails)
len(fdetails)

# Now test on logo
logo_results = detect_faces(logo_url)
len(logo_results['FaceDetails'])

# Now test on family
famresults = detect_faces(family_url)
len(famresults['FaceDetails'])



def has_faces_alpha(image_path):
    results = detect_faces(image_path)
    faces = results['FaceDetails']

    if len(faces) > 0:
        return True
    else:
        return False


def has_faces_beta(image_path):
    results = detect_faces(image_path)
    faces = results['FaceDetails']
    return len(faces) > 0


def count_faces(image_path):
    results = detect_faces(image_path)
    faces = results['FaceDetails']
    return len(faces)


def has_faces(image_path):
    return count_faces(image_path) > 0
