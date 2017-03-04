Local Quake Bot
===============

Inspired by the LA Times Quakebot, and the general idea of making programs that do all the mundane work in order to get to the interesting bits:

- How to Break News While You Sleep: https://source.opennews.org/articles/how-break-news-while-you-sleep/
- Quakebots and Pageview Quotas: Bot or Be Botted? https://source.opennews.org/articles/bot-or-be-botted/
- How a California Earthquake Becomes the News: An Extremely Precise Timeline https://www.theatlantic.com/technology/archive/2014/03/how-a-california-earthquake-becomes-the-news-an-extremely-precise-timeline/284506/


And very, very similar to a previous assignment: :doc:`/syllabus/assignments/homework/earthquake-mapper`

This assignment is a warm-up to making a "project-level" bot -- basically, a bot with more steps. Read the "Background and Discussion" section at the end of this very long walkthrough.


Rubric
======

Points: 20

Due date: 2017-03-07


Deliverable
-----------

Email dun@stanford.edu with the subject line:

``compciv-2017::your_sunet_id::local_quake_bot``

And attach a script named ``local_quake_bot.py``


Expected results
----------------

When I run ``local_quake_bot.py`` on my own machine and command-line, like so:

.. code-block:: shell

    $ python local_quake_bot.py "Des Moines, IA"

I should see results similar to:

.. code-block:: shell

    About 7.3 days ago, a M6.5 earthquake hit near 42km E of Padilla, Bolivia.

    Here is where Des Moines, IA is in relation to the earthquake:
    https://maps.googleapis.com/maps/api/staticmap?markers=color%3Apurple%7CDes+Moines%2C+IA&markers=color%3Ared%7C-19.2839%2C-63.899&size=600x400


Requirements
------------


Your script should be executable from the command-line, and should allow the user to specify a location, like "Stanford University, CA" or "Paris, France".

Your script should read from a remote data feed of earthquakes as recorded by the USGS:

http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php

An example direct link:

http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.csv

For the purposes of this exercise, to have a consistent answer, you can just read from this cached copy:

http://stash.compciv.org/2017/usgs/significant_month.csv

Your script should read from that URL and deserialize the data into a list of earthquake records.

It should then select the biggest earthquake by **magnitude**.

It should calculate how many fractional days (e.g. ``5.7`` days) from "now" (when the program is run) to when the biggest earthquake occurred.

It should produce some a descriptive sentence using data from the earthquake record, e.g. "A M6.2 earthquake 44 km near Sioux Falls, ND"

It should produce a Google Static Maps URL in which the user-specified location is denoted with a **purple** marker, and the location of the earthquake (using its latitude and longitude values) is specified with a **red** marker.








Walkthrough
===========


The following section walks you through the process in *phases*. Feel free to write the script how you like, but start here if you don't know where else to start:




The start
---------

Create a script named ``local_quake_bot.py`` with this bare minimum:


.. code-block:: python


    from sys import argv

    def main(location):
        txt = ""
        txt += "Here is where {loc} is in relation to the earthquake:".format(loc=location)
        txt += "\n"
        txt += "http://www.example.com"
        return txt

    if __name__ == '__main__':

        if len(argv) < 2:
            print("Need to pass in a name of a location as an argument")
        else:
            location = argv[1]
            story = main(location)
            print(story)



Run this from the command-line:

.. code-block:: shell

    $ python local_quake_bot.py 'Stanford University, CA'
    Here is where Stanford University, CA is in relation to the earthquake:
    http://www.example.com


Getting the quakes
------------------

Now we write the part of the code that fetches from a data source and deserializes the text data into data objects, i.e. "earthquake" records. Many ways to do this, but I suggest using ``requests.get()`` and ``csv.DictReader()``, because...we're fetching data from a remote source, and that data happens to be CSV formatted text.


First, download the given URL manually, and make sure you know what is in it. Open it in Excel if you must:

http://stash.compciv.org/2017/usgs/significant_month.csv


Jump into your interactive Python shell and try this out:


.. code-block:: python

    import csv
    import requests

    SRC_DATA_URL = 'http://stash.compciv.org/2017/usgs/significant_month.csv'

    resp = requests.get(SRC_DATA_URL)
    txt = resp.text
    lines = txt.splitlines()
    quakes = list(csv.DictReader(lines))


What is ``quakes``? If you don't know for sure, please type out the code above in your interactive shell and know what each line does.

That create a function named ``get_quakes()`` that returns a list of quake objects.

This is what your ``local_quake_bot.py`` script should look like (you fill in the blanks):


.. code-block:: python

    import csv
    import requests
    from sys import argv

    SRC_DATA_URL = 'http://stash.compciv.org/2017/usgs/significant_month.csv'


    def get_quakes():
        # you fill this in
        return quakes


    def main(location):
        quakes = get_quakes()
        # assume first quake is the biggest
        thequake = quakes[0]

        txt = ""
        txt += "A M{mag} earthquake hit near {place}.".format(mag=thequake['mag'], place=thequake['place'])
        txt += "\n"
        txt += "Here is where {loc} is in relation to the earthquake:".format(loc=location)
        txt += "\n"
        txt += "TK map url showing location: http://www.example.com"

        return txt

    if __name__ == '__main__':

        if len(argv) < 2:
            print("Need to pass in a name of a location as an argument")
        else:
            location = argv[1]
            story = main(location)
            print(story)



Running the script from the command-line:

.. code-block:: python

    $ python local_quake_bot.py 'Stanford University, CA'
    A M4.09 earthquake hit near 14km W of Belfair, Washington.
    Here is where Stanford University, CA is in relation to the earthquake:
    TK map url showing location: http://www.example.com



Sorting the quakes
------------------

The requirements for this assignment is that it sorts the data for the biggest quake by magnitude. Currently, the script only picks the first record off of the list, which is according to how USGS puts out the data, the most *recent* quake.

So the only change needs to be made to the ``get_quakes()`` function. Instead of returning the quake data as is, return a sorted version of the data, sorted by the ``'mag'`` column.

We sorted earthquakes (and by magnitude) in this assignment:

:doc:`/syllabus/assignments/homework/earthquake-mapper`

More importantly, you should be comfortable with sorting in general, using the built-in ``sorted()`` method:

http://www.compciv.org/guides/python/fundamentals/sorting-collections-with-sorted/


If you need to, download the cached data file, open it in Excel, sort it by ``mag``, so you know what to expect:


http://stash.compciv.org/2017/usgs/significant_month.csv


When running the script, you should get output that looks like this:

.. code-block:: python

    $ python local_quake_bot.py 'Stanford University, CA'
    A M6.5 earthquake hit near 42km E of Padilla, Bolivia.
    Here is where Stanford University, CA is in relation to the earthquake:
    TK map url showing location: Stanford University, CA


Counting the days
-----------------

It's relatively easy to access the ``time`` value of each earthquake, which is a string that looks like this:

``2017-02-21T14:09:04.410Z``

But if you are an average human being, you look at that, and you have a hard time parsing what that date actually is, in human-readable terms, nevermind what that date means relative to **now**, i.e. how many days ago was the biggest earthquake?

So let's write a function that takes a datetime string and calculates and returns the number of fractional days, rounded to the nearest tenth of a day (e.g. ``3.8`` days).

We've done this before


The steps are:

- Figure out how to get **now** as a Python datetime object
- Convert this time string ``2017-02-21T14:09:04.410Z`` to a datetime object
- Subtract the **now** time from the converted datetime object to get difference in seconds
- Convert the difference of seconds into days, e.g. divide seconds by the number of seconds per day, which you can calculate with math.


We've actually done this before, including the hard part of converting a string into a datetime object using the ``datetime.strptime()`` method:

:doc:`/syllabus/assignments/homework/serials/chicago-homicides`

But...let's make things easy on us. If you're using Python Anaconda, you should have a library named **python-dateutil** installed: https://dateutil.readthedocs.io/en/stable/

If not, you can install it manually by running this from your command-line:

.. code-block:: shell

    $ pip install python-dateutil


The **python-dateutil** library has many useful modules, including a ``parser`` module that will try to smartly guess what a datetime string evaluates to, in terms of a datetime object. Try it out:


.. code-block:: python

    >>> from dateutil import parser as dateparser
    >>> dateparser.parse('2016-01-25')
    datetime.datetime(2016, 1, 25, 0, 0)
    >>> dateparser.parse('2017-02-21T14:09:04.410Z')
    datetime.datetime(2017, 2, 21, 14, 9, 4, 410000, tzinfo=tzutc())


OK, how do we get **now**? Python's standard datetime package has it:


.. code-block:: python

    >>> from datetime import datetime
    >>> xnow = datetime.now()

How do we subtract one ``datetime`` object from another? One way is to convert each object into the standard way that computers record time objects, which is known as Unix or POSIX time:

https://en.wikipedia.org/wiki/Unix_time

OK, the details aren't hugely important, though they can be hugely confusing. The upshot is that each ``datetime`` object has a ``timestamp`` method, which can be used to convert that object into a **float** value:


.. code-block:: python

    >>> oldtime = datetime.now()
    >>> oldtime
    datetime.datetime(2017, 2, 28, 9, 36, 47, 14422)
    >>> oldtime.timestamp()
    1488303407.014422
    # wait a few seconds...
    >>> newtime = datetime.now()
    >>> newtime.timestamp() - oldtime.timestamp()
    7.311198949813843


To put everything together, let's convert the date strings of ``'2017-01-03 07:00'`` and ``'2016-12-25 22:00'`` into datetime objects. Then convert them into **float** values with their ``timestamp`` methods, and subtract the two float values to get the difference in seconds:


.. code-block:: python


    >>> from dateutil import parser as dateparser
    >>> dy = dateparser.parse('2017-01-03 07:00')
    >>> dx = dateparser.parse('2016-12-25 22:00')
    >>> z = dy.timestamp() - dx.timestamp()
    >>> z
    723600.0


How do we convert that gigantic number of seconds into a fractional day number?

How many seconds are in a day?

- 60 seconds in a minute
- 60 minutes in an hour
- 24 hours in a day

Ergo:

.. code-block:: python

    >>> 723600 / (60 * 60 * 24)
    >>> 8.375

Using what we've just gone over, write a function named ``days_from_timestring_until_now`` that returns a float (rounded to the nearest tenth) representing the days since a given timestring and whatever "now" is (i.e. when the function is called). I'll get you started:


.. code-block:: python

    from dateutil import parser as dateparser
    from datetime import datetime

    def days_from_timestring_until_now(timestring):
        # do something with timestring and dateparser.parse()
        now = datetime.now()
        diff = now.timestamp() - parsed_timestring.timestamp()
        seconds_per_day = 60 * 60 * 24
        fractional_days = diff / seconds_per_day
        return round(fractional_days, 1)



Counting the days -- and some code reorg
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Whew, handling time always takes longer than we want. Anyway, here's a more fleshed out version of ``local_quake_bot.py``, which not only includes the new ``days_from_timestring_until_now`` function, but reorganizes the ``main`` function.

Instead of having that ugly text-making process in ``main``, we make a new function called ``make_story`` that does that ugliness (and we also make it into one big string that we run ``.format``). Anyway, you can do what you like, but this is how I like to keep things neat:


.. code-block:: python


    import csv
    from dateutil import parser as dateparser
    from datetime import datetime
    import requests
    from sys import argv

    SRC_DATA_URL = 'http://stash.compciv.org/2017/usgs/significant_month.csv'

    def get_quakes():
        resp = requests.get(SRC_DATA_URL)
        # you fill this in
        # turn text into a list
        # sort that list
        # return that list of "quakes"
        return quakes

    def days_from_timestring_until_now(timestring):
        now = datetime.now()
        # do something with timestring and dateparser.parse()
        # hint: what does dateparser.parse('2016-12-01') return?
        # parsed_timestring = ????

        # then turn parsed_timestring and now into seconds, and subtract
        diff = now.timestamp() - parsed_timestring.timestamp()
        seconds_per_day = 60 * 60 * 24
        fractional_days = diff / seconds_per_day

        return round(fractional_days, 1)


    def make_story(user_location, quake):
        """
        `user_location` is a human-readable string representing some location
         in the world, e.g. "Stanford University, CA"

        `quake` is a dictionary, purportedly a USGS earthquake record

        Returns: a string
        """


        story_template = """
        About {daysago} days ago, a M{mag} earthquake hit near {place}.

        Here is where {loc} is in relation to the earthquake:
        {url}
        """

        diffdays = days_from_timestring_until_now(quake['time'])

        story = story_template.format(
            daysago=diffdays,
            mag=quake['mag'],
            place=quake['place'],
            loc=user_location,
            url='http://www.example.com'
        )

        return story

    def main(location):
        # get the data
        quakes = get_quakes()
        # get the biggest earthquake
        thequake = quakes[0]

        # create the "story"
        storytext = make_story(location, thequake)

        return storytext


    if __name__ == '__main__':


        if len(argv) < 2:
            print("Need to pass in a name of a location as an argument")
        else:
            location = argv[1]
            story = main(location)
            print(story)




Make a locator map
------------------


OK, once again, we were acquainted with putting points on a Google Map by studying the Google Static Maps API:

:doc:`/syllabus/assignments/homework/earthquake-mapper`

A `quick primer on Google Static Maps API`_



However, the difference is that we want to make the "starting point" a **purple** marker, and the earthquake point a **red** marker.

I'll let you try to figure out the official documentation on customizing markers:

https://developers.google.com/maps/documentation/static-maps/intro#Markers

But the gist of it is, to add a marker for "Stanford University":


https://maps.googleapis.com/maps/api/staticmap?size=600x400&markers=Stanford+University

To make that marker **purple**, we specify the *style* (i.e. color) before the marker's location. Like so:


``&markers=color:purple|Stanford+University``


However, pipe characters are not allowed in URLs, so the "correct" URL involves encoding pipe characters as ``%7C``:

https://maps.googleapis.com/maps/api/staticmap?size=600x400&markers=color:purple%7CStanford+University

The resulting image:

.. raw::html

    <img src="https://maps.googleapis.com/maps/api/staticmap?size=600x400&markers=color:purple%7CStanford+University" alt="https://maps.googleapis.com/maps/api/staticmap?size=600x400&markers=color:purple%7CStanford+University">


So let's define a function named ``make_locator_map`` that takes in a ``starting_location`` and a ``ending_location`` string. The function returns a URL that points to a Google Static Map, in which the ``starting_location`` location is marked with a **purple** marker and the ``ending_location`` a **red** marker.

Hence, if the **starting_point** is a human-readable location like "New York City", and the **ending_point** is latitude/longitude pair encoded as a string, e.g. "-42.2,80.8", this is what the URL would look like:

https://maps.googleapis.com/maps/api/staticmap?size=600x400&markers=color:purple%7CNew+York+City&markers=color:red%7C-42.2,80.8

.. raw::html

    <img src="https://maps.googleapis.com/maps/api/staticmap?size=600x400&markers=color:purple%7CNew+York+City&markers=color:red%7C-42.2,80.8">


Again, review the previous assignment to see how to use the Requests library's ``PreparedRequest`` class.

But just to make things easy for you, I'll give you a solution:


.. code-block:: python

    import requests

    def make_locator_map(starting_location, ending_location):
        base_endpoint = 'https://maps.googleapis.com/maps/api/staticmap'
        myparams = {}
        myparams['size'] =  '600x400'
        # basically, a list of 2 markers; we could add more if we wanted...
        myparams['markers'] = []
        myparams['markers'].append('color:purple|' + starting_location)
        myparams['markers'].append('color:red|' + ending_location)

        preq = requests.PreparedRequest()
        preq.prepare_url(base_endpoint, myparams)

        return preq.url



All together
------------

Below is one way of finishing this script, with a few parts for you to fill out on your own:

.. code-block:: python


    import csv
    from dateutil import parser as dateparser
    from datetime import datetime
    import requests
    from sys import argv

    SRC_DATA_URL = 'http://stash.compciv.org/2017/usgs/significant_month.csv'

    def get_quakes():
        resp = requests.get(SRC_DATA_URL)
        # you fill this in
        # turn text into a list
        # sort that list
        # return that list of "quakes"
        return quakes

    def days_from_timestring_until_now(timestring):
        now = datetime.now()
        # do something with timestring and dateparser.parse()
        # hint: what does dateparser.parse('2016-12-01') return?
        # parsed_timestring = ????

        # then turn parsed_timestring and now into seconds, and subtract
        diff = now.timestamp() - parsed_timestring.timestamp()
        seconds_per_day = 60 * 60 * 24
        fractional_days = diff / seconds_per_day

        return round(fractional_days, 1)


    def make_locator_map(starting_location, ending_location):
        base_endpoint = 'https://maps.googleapis.com/maps/api/staticmap'
        myparams = {}
        myparams['size'] =  '600x400'
        # basically, a list of 2 markers; we could add more if we wanted...
        myparams['markers'] = []
        myparams['markers'].append('color:purple|' + starting_location)
        myparams['markers'].append('color:red|' + ending_location)

        preq = requests.PreparedRequest()
        preq.prepare_url(base_endpoint, myparams)

        return preq.url


    def make_story(user_location, quake):
        storytemplate = """
        About {daysago} days ago, a M{mag} earthquake hit near {place}.

        Here is where {loc} is in relation to the earthquake:
        {url}
        """

        diffdays = days_from_timestring_until_now(quake['time'])

        # turn lat/lng into a coordinate-pair fit for Google Maps
        quake_coords = quake['latitude'] + ',' + quake['longitude']
        google_map_url = make_locator_map(user_location, quake_coords)

        story = storytemplate.format(
            daysago=diffdays,
            mag=quake['mag'],
            place=quake['place'],
            loc=user_location,
            url=google_map_url)


        return story

    def main(location):
        quakes = get_quakes()
        thequake = quakes[0]

        storytext = make_story(location, thequake)

        return storytext


    if __name__ == '__main__':

        if len(argv) < 2:
            print("Need to pass in a name of a location as an argument")
        else:
            location = argv[1]
            story = main(location)
            print(story)




Running the successful script from the command-line, and assuming it is still pointing to my cached quakes data file, you should see a result similar to this:


.. code-block:: shell


    $ python local_quake_bot.py "Stanford University, CA"
    About 4.0 days ago, a M6.9 earthquake hit near 287km S of Ndoi Island, Fiji.

    Here is where Stanford University, CA is in relation to the earthquake:
    https://maps.googleapis.com/maps/api/staticmap?size=600x400&markers=color%3Apurple%7CStanford+University%2C+CA&markers=color%3Ared%7C-23.2448%2C-178.8345




