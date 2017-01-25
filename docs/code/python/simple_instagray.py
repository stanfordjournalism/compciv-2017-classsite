from PIL import Image

src_filename = '/tmp/obama.jpg'
gray_filename = '/tmp/obama.gray.jpg'
bw_filename = '/tmp/obama.bw.jpg'

img = Image.open(src_filename)
# apparently this step removes everything but grayscale...
gray_img = img.convert('L')

# apparently converting image to grayscale is a
# intermediary step before going to stark black and white

# But I'm curious as to what the gray photo looks like
# so let's save it
gray_img.save(gray_filename)

# this step is just right from the StackOverflow answer
# except that I had to alter it to fit my variable names
bw_img = gray_img.point(lambda x: 0 if x < 128 else 255, '1')

# finally, save the bw file
bw_img.save(bw_filename)



# 2.
from io import BytesIO
img = Image.open(io.BytesIO(resp.content))

