*****************
Earthquake Mapper
*****************

**Due date:** 1:00 PM, 2017-02-07

**Points:** 20


Write a program that "creates" a world map showing the 5 biggest earthquakes (in terms of magnitude) in the last month.

By "create", I mean, leverages the Google Static Maps API to create a specially-formatted URL that leads to an image file created on Google's servers. In other words, your program is a easy-to-use "wrapper" for the kind of confusing API from Google.

As we've used in past examples, USGS maintains several real-time feeds of earthquake activity:

http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php

For this exercise, I want you to use my copy of the "Significant Earthquakes - Past 30 Days", which can be found at this URL:

http://stash.compciv.org/2017/usgs_quakes_significant_month.csv


When I run your program from the command-line, like this:

.. code-block:: shell

    $ python quake-mapper.py 5

It should produce a URL to an image that shows the 5 largest earthquakes by magnitude on a Google map URL:


https://maps.googleapis.com/maps/api/staticmap?markers=-6.2137%2C155.1224&markers=4.4634%2C122.575&markers=-19.3542%2C176.058&markers=-10.3433%2C161.318&markers=-10.1328%2C161.0275&size=800x500


.. raw:: html

    <img src="https://maps.googleapis.com/maps/api/staticmap?markers=-6.2137%2C155.1224&markers=4.4634%2C122.575&markers=-19.3542%2C176.058&markers=-10.3433%2C161.318&markers=-10.1328%2C161.0275&size=800x500">



Requirements
------------

Send an email to me with this subject: ``compciv-2017::your_sunet_id::quake-mapper``


It should contain a single attachment named ``quake-mapper.py``

Your program will read this cached copy of USGS earthquake data:

http://stash.compciv.org/2017/usgs_quakes_significant_month.csv

The program should sort the data  by ``magnitude``.

The program should have a command-line interface in which the user provides a single argument: the number of earthquakes to map.


Relevant readings
=================

- :doc:`/guide/topics/python-standard-library/csv`
- `Creating URL query strings in Python <http://www.compciv.org/guides/python/how-tos/creating-proper-url-query-strings/>`_ has more context on what a URL is, but also contains a lot of not-pertinent info. What we're doing for this exercise is *much* simpler.
- `Sorting Python collections with the sorted method <http://www.compciv.org/guides/python/fundamentals/sorting-collections-with-sorted/>`_ - an overly-long writeup about how to sort things in Python and why it's so overly complicated.
- `Official Google tutorial on Static Maps API <https://developers.google.com/maps/documentation/static-maps/intro>`_


Using Requests to prepare a URL
===============================

One of the main concepts of this exercise is writing a program that "wraps" complicated details in an easy interface. The most complicated detail here is taking a list of location strings (e.g. "Stanford, University", or, a list of longitude/latitudes) and creating a URL just the way Google Maps wants it.

We'll be using an advanced feature in the Requests library -- if you want to see more technical detail, you can see the documentation here: http://docs.python-requests.org/en/master/user/advanced/

Or you could read my convoluted guide on all the ways there are to properly format a URL string: http://www.compciv.org/guides/python/how-tos/creating-proper-url-query-strings/

But this is all you need to grok:


.. code-block:: python

    import requests
    BASIC_URL = 'http://www.example.com'
    my_request = requests.PreparedRequest()
    my_params = {'name': 'dan', 'status': 'awesome', 'foo': [1, 2, 3]}
    my_request.prepare_url(BASIC_URL, my_params)

    the_url = my_request.url
    print(the_url)
    # http://www.example.com/?name=dan&status=awesome&foo=1&foo=2&foo=3


Basically, we delegate all of the work of making a parameterized URL to the **Requests** library. We aren't using Requests to download from a URL, but to prepare a URL string that we can use later.



About the Google Static Maps API
================================

Here's an example of the API in action:

https://maps.googleapis.com/maps/api/staticmap?size=600x400

The URL above, according to Google's specifications, will lead to an image file of a map that is **600** pixels wide by **400** pixels high.

Here's what that image URL looks like when embedded on a webpage:

.. raw:: html

    <img src="https://maps.googleapis.com/maps/api/staticmap?size=600x400">

If I want to change the *zoom*, I specify the ``zoom`` parameter in the URL:

https://maps.googleapis.com/maps/api/staticmap?size=600x400&zoom=3

.. raw:: html

    <img src="https://maps.googleapis.com/maps/api/staticmap?size=600x400&zoom=3">


We usually don't care just to see a map of the world. We want to see where things are on a map of the world, i.e. placemarks.

The API defines a ``markers`` parameter, which, in its simplest form, looks like this if we want to mark Stanford University:

https://maps.googleapis.com/maps/api/staticmap?size=600x400&markers=Stanford,CA


.. raw:: html

    <img src="https://maps.googleapis.com/maps/api/staticmap?size=600x400&markers=Stanford,CA">


And what if we want **two** placemarks? Such as Stanford and, say, the Mountain View In-N-Out-Burger?

https://maps.googleapis.com/maps/api/staticmap?size=600x400&markers=Stanford,CA&markers=In-N-Out+Burger+Mountain+View+CA

.. raw:: html

    <img src="https://maps.googleapis.com/maps/api/staticmap?size=600x400&markers=Stanford,CA&markers=In-N-Out+Burger+Mountain+View+CA">


That ``markers`` parameter also takes longitude and latitude pairs. If you look in the sample `usgs_quakes_significant_month.csv datafile <>`_

usgs_quakes_significant_month.csv


About the URL specification
===========================

URLs are just text, of course. Why do the above invocations work as they do? Because that's the way Google defined it. But all URLs have a specification they must follow -- a mini-syntax if you will. This syntax defines ``?``, ``&``, ``=`` to be special characters. And certain characters, such as whitespace, are not allowed (though most modern browsers are forgiving).

In the "In-N-Out Burger Mountain View CA" example, you'll notice in the URL that it's written as:

``In-N-Out+Burger+Mountain+View+CA``


The bottom line is that there are a lot of rules for what a URL needs to look like, and that's on top of Google's API rules. So that's why we're writing a "wrapper" program to abstract all the details away.

In one sense, it's just fancy string formatting, i.e. substituting values into a known URL pattern. But don't do that -- the URL specification is too complex for a simple find and replace.




Writing a program with a command-line interface
===============================================


Lots of ways to do this, I'm just going to introduce you to the most straightforward way.

Create a test script named ``funtest.py`` with this code:


.. code-block:: python

    from sys import argv

    if __name__ == '__main__':
        arg0 = argv[0]
        print("Hello world, the 0th argument is:", arg0)


Running it from the command-line:

.. code-block:: shell

    $ python funtest.py

Should produce this output:

.. code-block:: text

    Hello world, the 0th argument is: funtest.py



Now change the script to this:

.. code-block:: python

    from sys import argv

    if __name__ == '__main__':
        arg0 = argv[0]
        arg1 = argv[1]
        print("Hello world, the 0th argument is:", arg0)
        print("And the first argument is:", arg1)


Now running this will produce an error:

.. code-block:: shell

    $ python funtest.py

.. code-block:: text

    Traceback (most recent call last):
      File "funtest.py", line 5, in <module>
        arg1 = argv[1]
    IndexError: list index out of range


But pass in an *argument*, like so:

.. code-block:: shell

    $ python funtest.py 5

And you get this:

.. code-block:: text

    Hello world, the 0th argument is: funtest.py
    And the first argument is: 5

Congrats, you've made the kind of primitive command-line program that will work for this assignment. Keep in mind, though, that arguments are read in as **string** values...i.e. that ``5`` is not really a ``5``, but a ``"5"``.

Don't worry about what that ``__name__ == '__main__'`` thing is, that's just a convention in Python that we just learn to follow. Everything in that conditional block is executed when the script is run from the command-line.



Getting started
===============


You can start with this skeleton script:


.. code-block:: python

    import requests
    import csv
    from sys import argv

    MAP_SIZE = '800x400'
    BASE_MAP_URL = BASE_MAP_URL = 'https://maps.googleapis.com/maps/api/staticmap'

    def make_map_url(markers):
        # do something with markers and BASE_MAP_URL
        # ...
        # ...

        # and return a URL as a string.
        # the following is just a placeholder
        return 'https://maps.googleapis.com/maps/api/staticmap?size=800x400&markers=Stanford'


    def fetch_quake_data():
        resp = requests.get(DATA_URL)
        return 'something'


    def sort_quakes(records, numlimit):
        """ records should be a list of deserialized quake objects
            numlimit is how many top-quakes-by-magnitude should be returned
        """
        return [] # obviously this is just a placeholder



    if __name__ == '__main__':
        if len(argv) < 2:
            print("You must supply an argument specifying number of quakes to map")
        else:
            numquakes = argv[1] # remember that this is just a string...

            print('hello user, you want this many quakes:', numquakes)
            # get the quake data
            # sort it
            quakes = []  # dummy code; replace with real code
            url = make_map_url(quakes)
            print(url)



