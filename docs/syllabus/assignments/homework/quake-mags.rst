*************************************************
Command Line Earthquake Magnitude Frequency Count
*************************************************


An example real-world data wrangling problem that can be solved by chaining together Unix text-processing tools using the Unix pipe.

Also, there's some practice with trying to do things from a remote computer, i.e. Stanford Farmshare.


.. contents:: :local:


Rubric
======

Due date:
    1:00 PM, :doc:`/syllabus/agendas/2017-01-19`

.. csv-table::
    :header: "Points", "Metric"
    :widths: 10, 90

    1,Having a correct subject headline
    1,Your email contains an attachment named answer.sh
    1,Running your ``answer.sh`` script produces the correct output





.. note::

    To do this assignment, and assuming you don't want to go through the work of customizing your own personal laptop at the moment -- you'll need to use either the McClatchy Lab iMacs. Or, the Stanford Farmshare computers:

    :doc:`/guide/topics/command-line/stanford-ssh`

    If you're feeling like you don't know where to start, that's OK: you're being thrown into a real-world data problem, with the hope that just doing the work will make the Unix/shell/command-line concepts clearer than just reading about them.

    Here's a short ad-hoc guide (including a section on how to create a "Bash script"):

    :doc:`/guide/topics/command-line/abridged-bash`

    The rest of the instructions on how to do this problem is covered in a walkthrough at the end of this page. Read on!






Delivery format
===============

Send an email to dun@stanford.edu with the subject:

``compciv-2017::your_sunet_id::quake-mags``

Where ``your_sunet_id`` is your Stanford student ID, all-lowercase.

The **body** of the email should have a single line of text:

    Hello Mutt!

And the email should contain an attachment named ``answers.zip``

And you should use the program **Mutt**, which is described later in this section







The Work
========


The data and expected output
----------------------------

The USGS has a list of real-time data feeds:

http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php

For this assignment, I want you to summarize the very big month-long earthquakes data file (8000+ quakes) into a group count of earthquakes by magnitude, truncated to the integer;  i.e. an earthquake of M5.8 is in the "5" group.


Given this :download:`sample feed file, which you can download </stash/data/usgs/usgs_earthquake_feed_all_month.csv>` -- write a script of commands that downloads the data and processes it to produce output that looks like this:

.. code-block:: text

    mag,count
    1,3863
    2,924
    3,160
    4,408
    5,116
    6,7
    7,2


This problem can be solved with these tools:


- ack
- sort
- uniq
- csvcut
- curl



Name the script ``answer.sh`` and mail it to me as an attachment using **mutt**.


You should produce a script named ``answer.sh`` which, when I run it on my own computer, does the downloading of data and the processing of it.



How to make a Bash/shell script
-------------------------------

See further reading here: :doc:`/guide/topics/command-line/abridged-bash`

But what is a "Bash/shell script"? It's a sequence of commands that, instead of running one-by-one manually, you list in a text file (the "script") so that you can execute the commands in a nice, automated batch.

If you named your shell script, ``myfunscript.sh``, here's how you would run it:


.. code-block:: shell

    $ bash myfunscript.sh


What does that do? It depends what is in ``myfunscript.sh``.


For example, if it contains these commands:

.. code-block:: shell

    echo 'hello'
    echo 'world'


Running the script produces this output:


.. code-block:: text

    hello
    world


For this assignment, one of the requirements in the output is that the first line is, literally, this text:


.. code-block:: text

    mag,count



So, create a script file (again, just a plaintext file) and name it ``answer.sh``.

Then include this command as the first line:

.. code-block:: text

    echo 'mag,count'

The walkthrough at the end of this page describes the steps you'll want to include...




Remote operation: sending email via mutt
----------------------------------------



Let's pretend you finish ``answer.sh`` and you're ready to send it to me as an attachment.

This section contains the details of how to send an email from the command line, with an attachment. Yes, I know you know how to use an email client. Bear with me on learning how to do it from the command-line.


Use mutt to send the email
^^^^^^^^^^^^^^^^^^^^^^^^^^

I want you to use the ``mutt`` program, which is available on Stanford Farmshare (corn and cardinal machines). And, ``mutt`` can be operated like a standard Unix tool.


This StackOverflow question has the gist of things: `How do I send a file as an email attachment using Linux command line? <http://stackoverflow.com/a/9524359/160863>`_


To send an email that says ``Hello`` in the subject, ``Que?`` in the body, to an email address (replace YOUR_ID@stanford.edu with your own Stanford email address for now):

.. code-block:: shell

    $ echo 'Que?' | mutt -s 'Hello'  YOUR_ID@stanford.edu


To send a file:

.. code-block:: shell

    $ echo 'A file is attached to this email' |  mutt -s 'Test 2' -a filename.etc -- YOUR_ID@stanford.edu

Note the double-hyphens which separate the name of the attached file from the recipient. (I dunno why ``mutt`` uses that convention)

If you don't have a file on Farmshare to send, let's download one (the URL shown below goes to a copy of a `kitten photo originally posted on Wikipedia <https://en.wikipedia.org/wiki/Kitten#/media/File:Kitten_in_Rizal_Park,_Manila.jpg>`_):

.. code-block:: shell

    $ curl http://i.imgur.com/8Jr7bLX.jpg > kitten.jpg

    $ echo 'This email does not contain a dog' | mutt -s 'Do you like dogs?' -a kitten.jpg -- YOUR_ID@stanford.edu


Do NOT do this for this assignment, but if you wanted to send this same email to multiple people...

(the code snippet below uses the **backslash** convention to split up a long command into multiple lines)

.. code-block:: shell

    $ echo 'This email does not contain a dog' \
        | mutt -s 'Do you like dogs?' -a kitten.jpg \
        -- person1@email.com person2@email.com




The answer
==========

.. note:: Note

    In the original description of the problem, the expected output excluded earthquakes of ``0`` magnitude; the example answers here don't filter those out.


Many ways to go about this, but here's what I have:


.. code-block:: shell


    curl http://2017.compciv.org/_downloads/usgs_earthquake_feed_all_month.csv \
        > quakes.csv


    echo 'mag,count'
    csvcut -c 5 quakes.csv \
        | ack -o '\d+\.' \
        | ack -o '\d+'    \
        | sort | uniq -c \
        | ack '(\d+)\s+(\d+)' --output '$2,$1'




There are ways to be slicker about it and do it in fewer steps. The following example skips the saving of the data to an intermediary ``quakes.csv`` and just feeds the output of ``curl`` right into ``csvcut``. I also use a lookahead in the regex just to be fancy:

.. code-block:: shell

    echo 'mag,count'

    curl -s http://2017.compciv.org/_downloads/usgs_earthquake_feed_all_month.csv \
        | csvcut -c 5 \
        | ack -o '\d+(?=\.)' \
        | sort | uniq -c \
        | ack '(\d+)\s+(\d+)' --output '$2,$1'



Sample problem: doing a time-series of Trump/Clinton tweets
===========================================================

Let's do a problem that is nearly the same thing, just different dataset: Let's do a count of Trump and/or Clinton tweets by day, month, and hour.




The data
--------

.. note:: Downloads


    - :download:`CSV snapshot of @realDonaldTrump tweets, as of January 1, 2017 </stash/data/twitter/realdonaldtrump-tweets.csv>`
    - :download:`CSV snapshot of @HillaryClinton tweets, as of January 1, 2017 </stash/data/twitter/hillaryclinton-tweets.csv>`




The data layout has 4 columns. The first 3 are the metadata of each tweet:


    .. csv-table::
        :header: ID,Posted at,Screen name

        815449933453127681,2017-01-01 06:49:49 +0000,realDonaldTrump
        815449868739211265,2017-01-01 06:49:33 +0000,realDonaldTrump
        815433444591304704,2017-01-01 05:44:17 +0000,realDonaldTrump
        815433217595547648,2017-01-01 05:43:23 +0000,realDonaldTrump
        815432169464197121,2017-01-01 05:39:13 +0000,realDonaldTrump


The fourth column, ``Text``, is the actual text of the tweet (which can include emoji):

    .. csv-table::
        :header: Text

        "RT @IvankaTrump: 2016 has been one of the most eventful and exciting years of my life. I wish you peace, joy, love and laughter. Hap… https://t.co/A1I3tvTySZ"
        RT @DonaldJTrumpJr: Happy new year everyone. #newyear #family #vacation #familytime https://t.co/u9fJIKNoZq
        RT @EricTrump: 2016 was such an incredible year for our entire family! My beautiful wife @LaraLeaTrump made it even better! 🇺🇸🇺🇸 https://t.co/M0SuRGn0il
        RT @Reince: Happy New Year + God's blessings to you all.  Looking forward to incredible things in 2017!  @realDonaldTrump will Make America Great Again!
        "RT @DanScavino: On behalf of our next #POTUS & @TeamTrump-

        #HappyNewYear AMERICA🇺🇸
        "


Note: To do a time-series analysis, we don't really care about the ``Text`` column.




Walkthrough
-----------

Note: these steps should be done from either the McClatchy iMacs. Or from Stanford Farmshare.


Step 1. Download the file
^^^^^^^^^^^^^^^^^^^^^^^^^

Let's just do Trump for now. The direct URL to download his Trump data is:

https://2017.compciv.org/_downloads/realdonaldtrump-tweets.csv

You should already know how to download that data with the browser. Here's how to do it via the command-line:


.. code-block:: shell

    $ curl https://2017.compciv.org/_downloads/realdonaldtrump-tweets.csv




Step 2. Actually save the data to a local file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


That should have dumped a bunch of text onto your screen, i.e. "standard out". We don't want that. We would rather save the contents of that URL into a local text file.

Let's call it ``trumptweets.csv``


.. code-block:: shell


    $ curl https://2017.compciv.org/_downloads/realdonaldtrump-tweets.csv > trumptweets.csv


What's in that file? If you downloaded it to your own computer, try opening it in Excel.

Or, if you want to print the first 10 lines to standard output (i.e. your screen), try this:


.. code-block:: shell

    $ head -n 10 trumptweets.csv


Step 3. Use csvcut to filter the data file by a single column
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I apologize for not having a thorough writeup on the ``csvcut`` tool, though it is pretty easy to figure out (which we will do in class). But here's a nice example from `dataquest.io <https://www.dataquest.io/blog/data-cleaning-command-line/>`_.

Here are the 2 options we want to try:


.. code-block:: shell

    $ csvcut -n trumptweets.csv


And then:

.. code-block:: shell

    $ csvcut -c 'Posted at' trumptweets.csv



Step 4. Filter for patterns
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, use ``ack`` to apply regex filtering.

Guide: :doc:`/guide/topics/command-line/nonstandard-commands/ack`


Think of the pattern needed to match the "year-month" of the timestamp. Or, just the hour.


Step 5. Do a group count
^^^^^^^^^^^^^^^^^^^^^^^^

Guide: :doc:`/guide/topics/command-line/standard-commands/sort`





How does this apply to the homework. Here's what the shell script for counting Trump tweets per day might look like:



.. code-block:: shell

    echo 'day,tweet_count'
    curl https://2017.compciv.org/_downloads/realdonaldtrump-tweets.csv > trumptweets.csv
    csvcut -c 'Posted at' trumptweets.csv \
        | ack -o '\d{4}-\d{2}-\d{2}' \
        | sort \
        | uniq -c \
        | sort -rn

