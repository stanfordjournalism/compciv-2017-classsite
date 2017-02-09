***********************
Chicago Homicide Mapper
***********************

Write a program that "creates" a world map showing the 5 biggest earthquakes (in terms of magnitude) in the last month.

By "create", I mean, leverages the Google Static Maps API to create a specially-formatted URL that leads to an image file created on Google's servers.

As we've used in the past, USGS maintains several real-time feeds of earthquake activity:

http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php

For this exercise, I want you to use my copy of the "Significant Earthquakes - Past 30 Days", which can be found at this URL:

http://stash.compciv.org/2017/usgs_quakes_significant_month.csv

https://data.cityofchicago.org/Public-Safety/Chicago-Homicides/4hwa-ftgf

Rubric
======

Due date:
    1:00 PM, 2017-02-07

Points: 20

Requirements
------------

Send an email to me with this subject: ``compciv-2017::your_sunet_id::quake-mapper``


It should contain a single attachment named ``quake-mapper.py``

Your program will read this cached copy of USGS earthquake data:

http://stash.compciv.org/2017/usgs_quakes_significant_month.csv

The program should sort it by ``magnitude``, and also allow the user to specify how many of the top earthquakes should be mapped.


When I run your program from the command-line, like this:

.. code-block:: shell

    $ python quake-mapper.py 5

It should produce a URL to an image that shows the 5 largest earthquakes by magnitude on a Google map URL:


.. csv-table::
    :header: "Points", "Metric"
    :widths: 10, 90

    1,"Having a correct subject headline of ``compciv-2017::your_sunet_id::congress-bio-fun``"
    5,"Your email contains attachaments 1.py through 4.py"
    5,"All of your programs have the logic for bootstrapping data files"
    20,"Your scripts produce the expected output"




References
==========




http://www.compciv.org/guides/python/how-tos/creating-proper-url-query-strings/


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


The bottom line is that there are a lot of rules for what a URL needs to look like, and that's on top of Google's API rules.

So, we want to write a function that does the heavy lifting. That is, when a user wants to produce a Google Maps URL with a certain marker (or several), they just call a function we design:

.. code-block:: python

    make_map_url('450 Serra Blvd, Stanford, CA')

And our function, ``make_map_url``, takes care of the details of knowing Google's API and properly formatting the URL:



