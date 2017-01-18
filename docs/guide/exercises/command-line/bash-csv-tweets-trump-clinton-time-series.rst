***************************************************************
Finding tweet frequency of @realDonaldTrump and @HillaryClinton
***************************************************************

In this exercise, we see how text-pattern matching can get us 95% of the way in doing frequency analysis, which is most often visualized as a time-series.


The data
========

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


Note: This CSV data of tweets is simplified output produced by a program named `t by Erik Michaels-Ober <https://github.com/sferik/t>`_. The Twitter API actually outputs data in JSON format; see the `API docs for the statuses/user_timeline endpoint for more details <https://dev.twitter.com/rest/reference/get/statuses/user_timeline>`_.


Pre-visualizing
===============

As with almost all programming, we want to know exactly what the program's output should be. In this scenario, think about what the data needs to look like if we wanted to make a time-series (i.e. histogram) showing tweets-per-day. Or month, etc.


Grepping for timestamps
=======================

For the most part, we can assume that within the given data, the timestamp regex pattern -- :regexp:`\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}` -- only happens in the column, ``Posted at``. So for a warm-up, we'll treat this CSV data as unstructured text


.. code-block:: shell

    # print all lines that have a timestamp (i.e. all of the lines, basically)
    $ ack '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}' realdonaldtrump-tweets.csv

    # now isolate the matching pattern, i.e. just the timestamp portion
    $ ack -o '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}' realdonaldtrump-tweets.csv

    # now match just the date
    $ ack -o '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}' realdonaldtrump-tweets.csv |
        ack -o '\d{4}-\d{2}-\d{2}'

The output will look like this:

.. code-block:: text

    2017-01-01
    2017-01-01
    2017-01-01
    2017-01-01
    2017-01-01
    2017-01-01
    2016-12-31
    2016-12-31
    2016-12-31
    2016-12-30







    # sort the dates (should already be sorted, but whatever)
    $ ack -o '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}' realdonaldtrump-tweets.csv |
        ack -o '\d{4}-\d{2}-\d{2}' | sort

    # now count the uniques
    $ ack -o '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}' realdonaldtrump-tweets.csv |
        ack -o '\d{4}-\d{2}-\d{2}' | sort | uniq -c
