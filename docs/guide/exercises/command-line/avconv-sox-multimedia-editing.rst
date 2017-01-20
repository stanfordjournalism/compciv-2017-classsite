**********************************************
Excerpting and editing audio/video with avconv
**********************************************


Getting video
=============

For the purposes of this exercise, we'll be using an excerpt from President-Elect Donald Trump's January 11, 2017 press conference, which is hosted on YouTube at this URL:

https://www.youtube.com/watch?v=aFMz-6Nn2kg

The Internet Archive has a mirror of this video at:

https://archive.org/details/trump-presser-2017-01-11-excerpt

You can use ``youtube-dl`` to download the video via the command-line at either URL.

The following invocation will download a video file named ``trump-presser-2017-01-11-excerpt.mp4``.

.. code-block:: shell

    $ youtube-dl --id https://archive.org/details/trump-presser-2017-01-11-excerpt


For the purposes of this exercise, let's rename that file to ``fullvideo.mp4``:

.. code-block:: shell

    $ mv trump-presser-2017-01-11-excerpt.mp4 fullvideo.mp4



Excerpting the video
--------------------

The target video file is 2 minutes long. Let's pick a `one-second clip that starts at 1:50 <https://youtu.be/aFMz-6Nn2kg?t=1m50s>`_:



.. code-block:: shell

    $ avconv -i fullvideo.mp4 \
        -ss 00:01:50 -t 1.05 \
        excerpt.mp4

Note that as we tweak exactly what we want to excerpt, which means re-runnign ``avconv`` and outputting to the same file name -- i.e. ``excerpt.mp4`` -- ``avconv`` will annoyingly ask if we really want to overwrite the output file. Adding the ``-y`` flag  -- "y" for "yes" -- will remove that prompt:


.. code-block:: shell

    $ avconv -y -i fullvideo.mp4 \
        -ss 00:01:50 -t 1.05 \
        excerpt.mp4

The result is a new movie file named ``excerpt.mp4`` that is 1.05 seconds long.


Useful reading: `How to Trim Videos with the Command Line Using AVConv <http://www.dototot.com/how-to-trim-videos-with-the-command-line-using-avconv/>`_


Slowing down the video
----------------------

1.05 seconds is such a short sound byte. Let's stretch out the video so we can savor the moment.


.. code-block:: shell

    $ avconv -y -i excerpt.mp4 -vf 'setpts=2.0*PTS' slowmoexcerpt.mp4



Unfortunately, slowing down the video doesn't *slow down the audio*. This is where things get slightly more complicated. A media file consists of separate audio and video tracks -- which is the case for movies in general, actually.

So if we want the audio to sync to the slowed-down video, we have to slow the audio down.


About ffmpeg
^^^^^^^^^^^^

A little trivia about command-line audio/video tools: ``libav`` (which includes the ``avconv`` library) is a fork of the long-living ``ffmpeg`` library. As far as I can tell, ``libav`` was meant to be a cleaned-up version of the ``ffmpeg`` code base and a drop-in replacement for all the situations where ``ffmpeg`` was used.

So if you do a search on how to use ``avconv``, you'll often end up on a page about ``ffmpeg``. Ideally, you could copy the code snippet of ``ffmpeg`` and just replace ``ffmpeg`` with ``avconv``. But ``avconv`` didn't quite match the featureset and interface of ``ffmpeg``. So a lot of code that should work with ``avconv`` just doesn't.

Case in point, if you're on a system with ``ffmpeg`` installed, slowing down a video file *and* its audio track can be done in a single command, according to the `ffmpeg guide on "How to speed up/slow down a video" <https://trac.ffmpeg.org/wiki/How%20to%20speed%20up%20/%20slow%20down%20a%20video>`_:


.. code-block:: shell

    $ ffmpeg -y -i input.mp4 \
        -af "atempo=0.5" \
        -vf "setpts=2.0*PTS" \
        -strict experimental \
        output.mp4

But ``avconv`` won't do that trick. Not going to lie, that's kind of annoying. However, let's roll with it and solve this problem the "Unix way".

The "Unix" way being: break things down into lots of extra steps.




Extracting separate audio and video tracks
------------------------------------------


http://unix.stackexchange.com/questions/140844/is-there-any-equivalent-to-the-atempo-ffmpeg-audio-filter-but-for-avconv-to-spee


Extract the audio and video:


avconv -y -i excerpt.mp4 -map 0:0 ex-video.mp4
avconv -y -i excerpt.mp4 -map 0:1 ex-audio.wav


Slow down the audio with sox:

sox ex-audio.wav slo-audio.wav tempo 0.5





Chipmunk
========


https://linux.die.net/man/1/sox

sox audio.wav fastaudio.wav tempo 2 pitch 400 contrast 20

avconv -y -i video.mp4 -vf 'setpts=0.5*PTS' fastvideo.mp4

avconv -i fast-video.mp4 -i fast-audio.wav fast.mp4


