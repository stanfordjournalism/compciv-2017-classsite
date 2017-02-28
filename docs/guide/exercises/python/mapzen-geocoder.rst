*********************
Geocoding with Mapzen
*********************



Objectives
==========


Main deliverable: geocoder.py and the geocode method
----------------------------------------------------

Create a Python script/module named ``geocoder.py`` with a method named ``geocode``.

The ``geocode`` method should take two parameters:

- ``api_key`` - a String representing the API key assigned by the Mapzen API to the developer
- ``location`` - a String that contains a human-readable description of the location to be geocoded, i.e. ``"Stanford University, CA"``


Example usage of the ``geocode`` method from the interactive shell:

.. code-block:: python

    >>> from geocoder import geocode
    >>> result = geocode('MY_MAPZEN_KEY', 'Stanford, University')
    >>> result



Milestones
----------

You're free to program to design the ``geocode`` method as you please. But I highly recommend that you break it up into at least 2 separate methods that can each be designed and tested in isolation:


make_url() method
^^^^^^^^^^^^^^^^^

Example usage of the ``make_url`` method from the interactive shell:

.. code-block:: python

    >>> from geocoder import geocode
    >>> m_url = make_url('MY_MAPZEN_KEY', 'Stanford, University')
    >>> print(m_url)
    TK



The make_url method
^^^^^^^^^^^^^^^^^^^






Milestones
----------

Making a successful geocoding request to the Mapzen Search API is a multi-step process. And each of these steps are complicated enough to deserve their own defined functions in the **geocoder.py** script.

Here's one way to think of the separate functions and their roles

1. ``make_url(api_key, location)`` -- this function handles the logic needed to create a proper URL formatted accordingly to the `Mapzen Search API specification <https://mapzen.com/documentation/search/search/>`_
2. ``download_and_parse_response(url)`` -- given a URL (whether it's a URL for an API, or to any regular file), we usually want to download it as a file and then parse its contents, e.g. with the ``json`` library for JSON-formatted data. This is something we've done plenty of times before, but it's worth keeping it as a separate step.
3.  ``get_best_geocoded_result(data)`` -- this method is in charge of all the logic and navigation needed to dig into the Mapzen data object and pull out the best geocoded location result. ``data`` is the data object that results from deserializing the raw Mapzen JSON text.


What does this mean for the ``geocode`` method that is supposed to be the main user-facing deliverable of this exercise? Well, the user doesn't care what is inside ``geocode`` -- whether the ``geocode`` method is 30 lines of raw code, or 3 lines of function calls. But you, the programmer, most definitely care about the cognitive difference.

So imagine that the ``geocode`` method definition could be as simple as this:


.. code-block:: python

    def geocode(api_key, location):
        mapzen_url = make_url(api_key, location)
        mapzen_data = download_and_parse_response(mapzen_url)
        result = get_best_geocoded_result(mapzen_data)

        return result


It's not just about making the ``geocode`` method simple to read and write -- but it's about making the entire programming process more sane. We can work on one function at a time. And we can test each function's results, one at a time. Among the many major benefits: we don't go insane trying to search for the cause of a bug somewhere in a massive Python script.

If you make a 3 line function, then you only have to worry about perfecting those 3 lines. By the time you get to making the function that uses all the other perfectly-wrapped up functions -- all your debugging has been done.



without having to worry that a mistake somewhere else in the Python script has any effect. We can also test each function separately.

And looking forward, as we try to design more complicated and interesting programs,


that are each complicated enough to deserve their own function in the **geocoder.py** script/module

The other way to think of it is: the ``geocode`` function involves so many steps that writing it all as one big function is a feat of difficult debugging and mental gymnastics.




Think of the ``geocode`` method as just a user-friendly wrapper around the separate steps needed to properly fetch data from the Mapzen API.

These separate steps should each be handled with their own separate helper functions. Separating functionality not only eases the development work, but it makes it easy to test each step independently. And oftentimes, as we developer more complicated programs, we find that we want to use those simple, standalone helper functions in a different way or combination.

So



In other words, the ``geocoder.py`` script should have several helper functions that each do their own thing. If we want, we can call those helper functions separately, especially for testing resons.

In the end, these separate functions are wrapped up in  ``geocoder.geocode``


The ``geocode`` method has to handle at least 2 domain-specific tasks:

Make a proper Mapzen Search URL string
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define a function named ``make_url()`` that, given a user-supplied API key and location name, returns a URL string that matches the specification of the Mapzen Search API, as documented here:


Sample usage:


.. code-block:: python

    >>> from geocoder import make_url
    >>> url = make_url('YOUR_MAPZEN_KEY', 'The White House, Washington D.C.')
    >>> print(url)
    https://search.mapzen.com/v1/search?text=The+White+House%2C+Washington+D.C.&api_key=YOUR_MAPZEN_KEY


Extract the most relevant geocoded result and its useful fields from the Mapzen result
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Mapzen Search API returns a detailed data object serialized as JSON:

http://stash.compciv.org/2017/mapzen-search-stanford-university-single.json

The data object's detail can be seen in its nested structure. As nice as the detail is, it's way more information than we need for the typical use case, which is to just get latitude and longitude for a human-readable address.


So define a function named ``get_best_geocoded_result``. This function takes a single argument -- the data object (e.g. a Python dict or list) that the Mapzen Search API returns -- and returns a single dictionary that represents the most relevant geocoded result from Mapzen, trimmed to its most useful attributes.

.. code-block:: python

    >>> from geocoder import make_url
    >>> url = make_url('YOUR_MAPZEN_KEY', 'The White House, Washington D.C.')
    >>> print(url)
    https://search.mapzen.com/v1/search?text=The+White+House%2C+Washington+D.C.&api_key=YOUR_MAPZEN_KEY








- Given a successful query of the Mapzen API, parse the data response and extract only the values needed from the results, e.g. the latitude and longitude values.

There is also, of course, the more general task of downloading from a URL (Mapzen API, or otherwise) and serializing the downloaded response -- but that's something we've done plenty of times with the Python Requests library.


Milestone: create a Map
^^^^^^^^^^^^^^^^^^^^^^^




The ``geocode`` method should be dependent



to specify their Mapzen Search API key and a





Creating the URL that the Mapzen Search API wants
=================================================



