**************************************************
Solid Serialization of: Multiple User Tweets (CSV)
**************************************************

.. contents::


This assignment is part of: :doc:`/syllabus/assignments/homework/solid-serialization-skills`

It's basically the same as this exercise, except done at **scale** (i.e. with loops):

:doc:`/syllabus/assignments/homework/serials/just-trump-tweets-csv`



Deliverables
============

You are expected to deliver a script named: ``multiple_user_tweets_csv.py``

The data files to use are:

http://stash.compciv.org/2017/realdonaldtrump-tweets.csv

http://stash.compciv.org/2017/hillaryclinton-tweets.csv

http://stash.compciv.org/2017/jk_rowling-tweets.csv

http://stash.compciv.org/2017/darrellissa-tweets.csv



This script has **5** prompts, which means at the very least, your script will contain 5 separate function definitions, from ``foo_1`` to ``foo_5``.



When I run your script from the command line, I expect to see something like this:


.. code-block:: shell

    $ python multiple_user_tweets_csv.py
    Done running assertions!


And I expect your script to have this code at the bottom:

.. code-block:: python


    def foo_assertions():
        assert type(foo_1()) == int
        assert foo_1() == 12800

        assert type(foo_2()) == dict
        assert len(foo_2().items()) == 4
        assert foo_2()['jk_rowling'] == 1162

        assert type(foo_3()) == dict
        assert type(foo_3()['darrellissa']) == dict
        assert foo_3()['hillaryclinton'] ==  {'after': 25, 'before': 256}

        assert type(foo_4()) == list
        assert type(foo_4()[0]) == tuple
        assert foo_4()[0] == ('month', 'count')
        assert foo_4()[1] == ('2014-05', 73)
        assert foo_4()[-1] == ('2017-02', 274)


        assert type(foo_5()) == list
        assert type(foo_5()[0]) == tuple
        assert foo_5()[0] == ('screen_name', 'month', 'count')
        assert foo_5()[1] == ('darrellissa', '2014-05', 73)
        assert foo_5()[-1] == ('realdonaldtrump','2017-02', 87)


    if __name__ == '__main__':
        foo_assertions()
        print("Done running assertions!")




Prompts
=======


1. Find the number of tweets represented in the combined data files
-------------------------------------------------------------------

Basically, just deserialize each of the CSVs return a total count of the objects.


Expected result:

.. code-block:: python

    12800


2. Find the number of tweets per user per post-Election Day
-----------------------------------------------------------

Election 2016 was on November 8, 2016, i.e. ``'2016-11-08'``

Instead of just returning a count, return a dictionary with a single item, in which the key is the screen name of ``'realdonaldtrump'``, and the value is the number of tweets that match the criteria of post-Election day.

Each screen name should have its own key, e.g. ``'realdonaldtrump'`` and ``'jk_rowling'``


Expected result:

.. code-block:: python

    {'darrellissa': 210,
     'hillaryclinton': 45,
     'jk_rowling': 1162,
     'realdonaldtrump': 529}



3. Find the number of tweets for the week before and the week after Election Day, per user
------------------------------------------------------------------------------------------

The week before Election day includes Nov. 1, 2016 through Nov. 8, 2016.

The week after Election Day includes Nov. 9, 2016 through Nov. 16, 2016.

Return a dictionary of dictionaries. The sub-dictionary contains two keys, 'before' and 'after', with the values being the number of tweets that match the respective criteria.

Expected result:

.. code-block:: python

    {'darrellissa': {'after': 6, 'before': 12},
     'hillaryclinton': {'after': 25, 'before': 256},
     'jk_rowling': {'after': 185, 'before': 89},
     'realdonaldtrump': {'after': 20, 'before': 83}}



4. Count the total number of tweets per year-month
--------------------------------------------------


Do a group count by the year-month string, e.g. ``'2017-01'`` from ``'2017-01-12 12:01:43'``, for total tweets among all the given tweet data sets.

Return a list of __tuples__, sorted by the year-month string. Also, the first tuple should contain the headers, i.e.

.. code-block:: python

    ('month', 'count')




Expected result:

.. code-block:: python

    [('month', 'count'),
     ('2014-05', 73),
     ('2014-06', 235),
     ('2014-07', 295),
     ('2014-08', 141),
     ('2014-09', 669),
     ('2014-10', 120),
     ('2014-11', 305),
     ('2014-12', 90),
     ('2015-01', 73),
     ('2015-02', 62),
     ('2015-03', 83),
     ('2015-04', 29),
     ('2015-05', 24),
     ('2015-06', 50),
     ('2015-07', 42),
     ('2015-08', 21),
     ('2015-09', 18),
     ('2015-10', 29),
     ('2015-11', 11),
     ('2015-12', 18),
     ('2016-01', 69),
     ('2016-02', 42),
     ('2016-03', 244),
     ('2016-04', 370),
     ('2016-05', 405),
     ('2016-06', 922),
     ('2016-07', 1085),
     ('2016-08', 1238),
     ('2016-09', 1532),
     ('2016-10', 2023),
     ('2016-11', 1072),
     ('2016-12', 415),
     ('2017-01', 721),
     ('2017-02', 274)]



5. Count the number of tweets per yearmonth per screen name
-----------------------------------------------------------

This is exactly like the previous prompt, except I want you to include a column for the screen name of the user who tweeted. In this case, every tweet is by "realdonaldtrump". This will make more sense in the next exercise when you're aggregating tweets from multiple users.


The list should have the header-tuple of: ``('screen_name', 'month', 'count')``

It should be sorted by ``screen_name``, then ``month``:

Expected result:

.. code-block:: python

    [['screen_name', 'month', 'count'],
     ['darrellissa', '2014-05', 73],
     ['darrellissa', '2014-06', 235],
     ['darrellissa', '2014-07', 295],
     ['darrellissa', '2014-08', 141],
     ['darrellissa', '2014-09', 669],
     ['darrellissa', '2014-10', 120],
     ['darrellissa', '2014-11', 305],
     ['darrellissa', '2014-12', 90],
     ['darrellissa', '2015-01', 73],
     ['darrellissa', '2015-02', 62],
     ['darrellissa', '2015-03', 83],
     ['darrellissa', '2015-04', 29],
     ['darrellissa', '2015-05', 24],
     ['darrellissa', '2015-06', 50],
     ['darrellissa', '2015-07', 42],
     ['darrellissa', '2015-08', 21],
     ['darrellissa', '2015-09', 18],
     ['darrellissa', '2015-10', 29],
     ['darrellissa', '2015-11', 11],
     ['darrellissa', '2015-12', 18],
     ['darrellissa', '2016-01', 69],
     ['darrellissa', '2016-02', 42],
     ['darrellissa', '2016-03', 77],
     ['darrellissa', '2016-04', 87],
     ['darrellissa', '2016-05', 55],
     ['darrellissa', '2016-06', 59],
     ['darrellissa', '2016-07', 51],
     ['darrellissa', '2016-08', 62],
     ['darrellissa', '2016-09', 50],
     ['darrellissa', '2016-10', 38],
     ['darrellissa', '2016-11', 46],
     ['darrellissa', '2016-12', 35],
     ['darrellissa', '2017-01', 90],
     ['darrellissa', '2017-02', 51],
     ['hillaryclinton', '2016-07', 572],
     ['hillaryclinton', '2016-08', 518],
     ['hillaryclinton', '2016-09', 782],
     ['hillaryclinton', '2016-10', 960],
     ['hillaryclinton', '2016-11', 352],
     ['hillaryclinton', '2016-12', 1],
     ['hillaryclinton', '2017-01', 10],
     ['hillaryclinton', '2017-02', 5],
     ['jk_rowling', '2016-06', 560],
     ['jk_rowling', '2016-07', 104],
     ['jk_rowling', '2016-08', 375],
     ['jk_rowling', '2016-09', 404],
     ['jk_rowling', '2016-10', 494],
     ['jk_rowling', '2016-11', 481],
     ['jk_rowling', '2016-12', 242],
     ['jk_rowling', '2017-01', 409],
     ['jk_rowling', '2017-02', 131],
     ['realdonaldtrump', '2016-03', 167],
     ['realdonaldtrump', '2016-04', 283],
     ['realdonaldtrump', '2016-05', 350],
     ['realdonaldtrump', '2016-06', 303],
     ['realdonaldtrump', '2016-07', 358],
     ['realdonaldtrump', '2016-08', 283],
     ['realdonaldtrump', '2016-09', 296],
     ['realdonaldtrump', '2016-10', 531],
     ['realdonaldtrump', '2016-11', 193],
     ['realdonaldtrump', '2016-12', 137],
     ['realdonaldtrump', '2017-01', 212],
     ['realdonaldtrump', '2017-02', 87]]


Hints
^^^^^

How do you sort by two factors, i.e. the first element of each tuple, then the second?


Design a sorting function to return a list/tuple of two values. Python's ``sorted()`` function knows how to compare a list against another list, when the values of those lists are directly comparable:

.. code-block:: python

    def sortfoo(el):
        return (el[0], el[1])

    mylist = [[42, 'c'], [6, 'x'], [6, 'a']]
    sorted(mylist, key=sortfoo)


    # result
    [[6, 'a'], [6, 'x'], [42, 'c']]




Background
==========

Same as previous exercise:

:doc:`/syllabus/assignments/homework/serials/just-trump-tweets-csv`


But in general, when we want to do something interesting, we want to do it across many, many users, or facets. And why not, when we can throw things into a loop?



General Hints
=============


You can use a lot of the same code from the previous exercise. For example, the helper functions for downloading the data and saving it to some predictable filename is the same, as is the function to deserialize a dataset of tweets given just a screenname, i.e. ``'realdonaldtrump'``


.. code-block:: python

    import csv
    import requests
    from os.path import basename, exists, join
    from os import makedirs
    SRC_URL_BASE = 'http://stash.compciv.org/2017/{}-tweets.csv'
    DATA_DIR = 'data-files'


    def make_url(xname):
        return SRC_URL_BASE.format(xname)


    def make_filename_from_url(url):
        fname = basename(url)
        return join(DATA_DIR, fname)


    def fetch_tweets(tname):
        makedirs(DATA_DIR, exist_ok=True)
        url = make_url(tname)
        destname = make_filename_from_url(url)

        if not exists(destname):
            resp = requests.get(url)
            with open(destname, 'wb') as f:
                f.write(resp.content)


    def read_tweets(tname):
        """
        returns a list of dicts of tweets for a given twitter name
        """
        fetch_tweets(tname)
        fname = make_filename_from_url(make_url(tname))
        with open(fname, 'r') as f:
            tweets = list(csv.DictReader(f))
            return tweets




Even though there are 4 different data files, they all follow the same convention, so this should work:



.. code-block:: python

    trump_tweets = read_tweets('realdonaldtrump')
    clinton_tweets = read_tweets('hillaryclinton')

    totalcount = len(trump_tweets) + len(clinton_tweets)



Which means ``foo_1`` can be defined like so:



.. code-block:: python

    def foo_1():
        total = 0
        total += len(read_tweets('realdonaldtrump'))
        total += len(read_tweets('jk_rowling'))
        total += len(read_tweets('hillaryclinton'))
        total += len(read_tweets('darrellissa'))
        return total



But this is where you need to see that there is a **pattern**, and that a loop should be used:




.. code-block:: python

    def foo_1():
        total = 0
        for n in ['realdonaldtrump', 'jk_rowling', 'hillary_clinton', 'darrellissa']:
            total += len(read_tweets(n))

        return total


That's pretty good. And then if you want, realize that that list of names is a constant throughout the script. So why not put this variable up at the top of the code:


.. code-block:: python

    TWITTER_NAMES = ['realdonaldtrump', 'jk_rowling', 'hillaryclinton', 'darrellissa']


And then each function is a little cleaner:

.. code-block:: python

    def foo_1():
        total = 0
        for n in TWITTER_NAMES:
            total += len(read_tweets(n))

        return total


Basically, the challenge of this assignment is to recognize how to turn your one-off code into something repeatable.

If your Trump-only ``foo_2`` function from the previous assignment looked like this:


.. code-block:: python

    def foo_2():
        d = {}
        tcount = 0
        tweets = read_tweets('realdonaldtrump')
        for t in tweets:
            if t['Posted at'] >= '2016-11-09':
                tcount += 1

        d['realdonaldtrump'] = tcount
        return d


Abstract out the most obvious repetition, in this case, the hard-coded string that tells us what file to open:


.. code-block:: python

    def foo_2():
        screenname = 'realdonaldtrump'
        d = {}
        tcount = 0

        tweets = read_tweets(screenname)
        for t in tweets:
            if t['Posted at'] >= '2016-11-09':
                tcount += 1

        d[screenname] = tcount
        return d



And then the logic of where the loop should go becomes a little clearer:


.. code-block:: python

    def foo_2():
        d = {}
        # start off with an empty dictionary...

        # then, for every screenname, add a new key-value pair to the dictionary
        for screenname in TWITTER_NAMES:
            tcount = 0

            tweets = read_tweets(screenname)
            for t in tweets:
                if t['Posted at'] >= '2016-11-09':
                    tcount += 1

            d[screenname] = tcount

        # return a dictionary at the end
        return d


