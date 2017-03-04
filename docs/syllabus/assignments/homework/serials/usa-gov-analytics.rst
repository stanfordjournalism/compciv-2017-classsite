*****************************************
Solid Serialization of: USA Gov Analytics
*****************************************

.. contents::


This assignment is part of: :doc`/syllabus/assignments/homework/solid-serialization-skills`


Deliverables
============

You are expected to deliver a script named: ``usa_gov_analytics.py``

This script has **5** prompts, which means at the very least, your script will contain 5 separate function definitions, from `foo_1` to `foo_5`.


When I run your script from the command line, I expect to see something like this:



.. code-block:: shell

    $ python usa_gov_analytics.py
    Done running assertions!


And I expect your script to have this code at the bottom:

.. code-block:: python

    def foo_assertions():
        assert foo_1() == 725573027, "Expect foo_1() to return integer value equal to exactly 725573027"

        r = foo_2()
        assert type(r) == dict, 'Expect foo_2() to return a dictionary'
        assert r['source_count'] == 20, "Expect 'source_count' to be 20"
        assert r['total_pageviews'] == 1864771726, "Expect 'total_pageviews' to be 1864771726"

        r = foo_3()
        assert r['search'] == 355065438, "Expect 'search' sources to have 355065438 visits"
        assert r['social'] == 11994983, "Expect 'social' sources to have 11994983 visits"

        r = foo_4()
        assert r['search_pct'] == 48.9, "Expect 'search' sources to make 48.9 percent of total visits"

        r = foo_5()
        assert type(r) is list, 'Expect foo_5() to return a list'
        assert r[0] == ['source', 'pct_of_total_visits', 'pageviews_per_visit'], 'Expect header rows to have specified keys and order'
        assert r[1][0] == 'google', "Expect first row, first col to equal 'google'"
        assert r[1][1] == 43.38, "Expect first row, 2nd col to equal 43.38"
        assert r[10] == ['login.usajobs.gov', 1.54, 5.37], 'Expect 10th row to contain data for login.usajobs.gov source'


    if __name__ == '__main__':

        foo_assertions()
        print("Done running assertions!")



That script should have a ``if __name__ == '__main__'`` conditional block, in which a function named ``foo_assertions()`` is executed.






Prompts
=======


The CSV data file for "Visits to and traffic sources for all participating agencies: Top traffic sources (30 days)"  has been mirrored here:

http://stash.compciv.org/2017/analytics.usa.gov-top-traffic-sources-30-days.csv

Download (and cache) that file, then parse/deserialize the text data, then write the ``foo_`` functions to satisfy the following prompts:

1. Sum the total visits among the top referrers in the dataset
--------------------------------------------------------------

Every row in the given dataset has a ``visits`` column. Your ``foo_1()`` function should merely sum that value up for every row and produce this result (an integer):


Expected result:

.. code-block:: python

    725573027

Remember that when deserializing CSV data, values that are *number characters* are not converted to numbers automatically...


2. Create an aggregation of total visits, page views, and count of sources
--------------------------------------------------------------------------

Basically, your function should  create and return a dictionary with these keys and values:

Expected result:

.. code-block:: python


    {'source_count': 20, 'total_pageviews': 1864771726, 'total_visits': 725573027}



3. An aggregated sum of visits by traffic sources, classified as "social", "search", and "direct"
------------------------------------------------------------------------------------------------


Return a dictionary that lists number of total visits with these keys:
    'social', 'direct', 'search', 'total'

Expected answer:

.. code-block:: python

    {'direct': 208516971,
     'search': 355065438,
     'social': 11994983,
     'total': 725573027}

Classifying each source as ``social`` or ``direct`` is obvious enough. But for ``search``, we make up our own criteria for what counts as a search engine. Because there are generally so few major search engines, we can come up with a simple heuristic:

    For a given row, if the ``source`` value is in the list ``['google', 'bing', 'yahoo']``, then that source should be considered "search" referral.


4. Aggregate visit counts by type of referrer, calculate percentage of total traffic by referrer type
-----------------------------------------------------------------------------------------------------

Basically the same as the previous exercise, except we want the aggregation to be calculated with respect to the total number of visits in this dataset, which is a number we've calculated in a previous exercise.


Round to the nearest tenth percentage point.

Expected answer:

.. code-block:: python

    {'direct_pct': 28.7,
     'search_pct': 48.9,
     'social_pct': 1.7,
     'total_visits': 725573027}


5. Create a list of 3-column rows with source name, pageviews per visit, and pct_of_total_visits
------------------------------------------------------------------------------------------------

Just another aggregation, but instead of returning a list of dictionaries, return a list of lists. The first list should be the headers in this order:

- 'source'
- 'pct_of_total_visits'
- 'pageviews_per_visit'


Each list in this data should correspond to a datarow in the fetched/parsed data -- think of it as a slimming transformation: our new list has fewer fields overall, while taking a different opinion on what fields are important.

Case in point, the ``pct_of_total_visits`` field/column, for each row is meant to show how big that source was in terms of visits, relative to the all the other top referrers. Calculating that first involves calculating the ``total_visits`` number for the data, which we did in the very first exercise.


Then, for each row in the data set, we divide its number of ``visits`` by the calculated total visits to get ``pct_of_total_visits``.

To get ``pageviews_per_visit``, you could be an idiot like me and divide ``pageviews`` by ``visits``. Or you could just look at the dataset and see that ``pageviews_per_session`` already does that calculation for us.

Expected results:

.. code-block:: python

    [['source', 'pct_of_total_visits', 'pageviews_per_visit'],
     ['google', 43.38, 2.41],
     ['(direct)', 28.74, 2.78],
     ['usps.com', 4.45, 2.5],
     ['bing', 3.77, 3.4],
     ['weather.gov', 2.69, 2.12],
     ['irs.gov', 2.37, 3.5],
     ['yahoo', 1.79, 2.59],
     ['forecast.weather.gov', 1.77, 1.99],
     ['reg.usps.com', 1.56, 2.05],
     ['login.usajobs.gov', 1.54, 5.37],
     ['usajobs.gov', 1.27, 1.78],
     ['m.facebook.com', 1.15, 1.54],
     ['checkout.shopify.com', 0.86, 1.32],
     ['noaa.gov', 0.83, 1.51],
     ['find.irs.gov', 0.77, 2.57],
     ['cns.usps.com', 0.76, 1.66],
     ['sa.www4.irs.gov', 0.65, 2.77],
     ['tools.usps.com', 0.63, 2.24],
     ['my.usps.com', 0.51, 2.23],
     ['t.co', 0.5, 1.92]]



Background
==========


The federal government  built itself an analytics dashboard to showcase the amount and type of visits to federal websites:

https://analytics.usa.gov/

Here's a great writeup by 18F: How we built analytics.usa.gov https://18f.gsa.gov/2015/03/19/how-we-built-analytics-usa-gov/

And all of its code is open-source and easy to download via Github: https://github.com/18F/analytics.usa.gov


I like the site because it's a nice example of how to use the Network Panel to see how individual data files are used by a webpage. The front page for analytics.usa.gov has visualizations that are fed by JSON-serialized data, which you can see (and access) bu opening the Network Panel of your browser's dev tools:

http://www.compjour.org/tutorials/watching-traffic-network-panel/


But it's also an example of how web-scraping should be a last-resort -- in this case, the data we want is all available in easy-to-download files on analytics.usa.gov's data page:


https://analytics.usa.gov/data

For instance, the live version of "Visits to and traffic sources for all participating agencies: Top traffic sources (30 days)" can be found here:

As CSV:

https://analytics.usa.gov/data/live/top-traffic-sources-30-days.csv

As JSON:

https://analytics.usa.gov/data/live/top-traffic-sources-30-days.json



Answers
=======


..  literalinclude:: /code/answers/python/usa_gov_analytics_nicer.py
