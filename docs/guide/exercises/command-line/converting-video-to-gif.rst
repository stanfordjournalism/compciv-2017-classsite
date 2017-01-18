**************************************
Creating a GIF from video using avconv
**************************************


Create images from video
========================

Since even before Disney animation, the core concept of movies (i.e. "moving pictures") is creating the illusion of movement by rapidly flipping through images.

So even if you're unfamiliar with digital media formats, you can at least intuit that a digital movie can be split up into separate digital image files.

With that in mind, we use the ``avconv`` command-line tool to do the splitting.

Useful reading: `StackExchange: How to convert video to images? <http://superuser.com/a/729351>`_










Converting video to images

http://superuser.com/a/729351

mkdir frames
avconv -i myexcerpt.mp4 -r 5 frames/myframe_%02d.png


convert pngs to gif:


http://askubuntu.com/questions/573712/convert-thousands-of-pngs-to-animated-gif-convert-uses-too-much-memory




Rescaling images

http://askubuntu.com/a/144102


 convert mygif.gif -geometry x300 output.gif






ffmpeg -y -i  myexcerpt.mp4 -r 10  mygif.gif


avconv -y -i  myexcerpt.mp4 -r 10  -pix_fmt rgb24 mygif.gif


Converting to GIF
-----------------

ffmpeg -y -i myexcerpt.mp4 mygif.gif

avconv -y -i myexcerpt.mp4 -vf 'format=rgb8,format=rgb24' -r 10 mygif.gif




Slowing down that GIF
^^^^^^^^^^^^^^^^^^^^^



avconv -y -i myexcerpt.mp4 -vf 'format=rgb8,format=rgb24,setpts=2.0*PTS' -r 10 mygif.gif

ffmpeg -y -i myexcerpt.mp4 -vf 'setpts=2.0*PTS' -r 10 mygif.gif










ffmpeg -y -i  failingpileofgarbage.mp4  -r 10 -vf crop=300:200:500:120 failingpileofgarbage.gif


# http://stackoverflow.com/questions/6195872/applying-multiple-filters-at-once-with-ffmpeg

ffmpeg -y -i  failingpileofgarbage.mp4  -r 10 -vf "crop=300:200:500:120, scale=1200:-1" failingpileofgarbage.gif



ffmpeg -y -i  failingpileofgarbage.mp4  -r 5 -vf "crop=300:200:500:120, scale=1200:-1" -pix_fmt gray failingpileofgarbage.gif
