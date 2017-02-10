*****************************************
Solid Serialization of: Chicago Homicides
*****************************************

.. contents::


This assignment is part of: :doc`/syllabus/assignments/homework/solid-serialization-skills`


Deliverables
============

You are expected to deliver a script named: ``chicago_homicides.py``

This script has **5** prompts, which means at the very least, your script will contain 5 separate function definitions, from `foo_1` to `foo_5`.


When I run your script from the command line, I expect to see something like this:



.. code-block:: shell

    $ python chicago_homicides.py
    Done running assertions!


And I expect your script to have this code at the bottom:

.. code-block:: python

    def foo_assertions():
        r = foo_1()
        assert type(r) is int, 'Assert foo_1() returns an integer'
        assert r == 8282, 'Expect total number of homicides in foo_1() to be equal to 8282'

        r = foo_2()
        assert type(r) is dict, 'Assert foo_2() returns dictionary'
        assert r['true'] == 3998, 'Assert foo_2() shows 3,998 arrests made in homicide cases'
        assert r['false'] == 4284, 'Assert foo_2() shows arrests not made in 4284 homicide cases'
        assert r['rate'] == 48.3, 'Assert foo_2() is equal to homicide arrest rate to be 48.3'


        r = foo_3()
        assert type(r) is list, 'Assert foo_3() returns list'
        assert r[0] == ['year', 'count'], 'Expect first row of foo_3() to be two column list: year, count'
        assert len(r[1:]) == 17, 'Expect total number of records (i.e. not the header row) to be 17'
        assert r[1][0] == '2001', "Expect earliest year to be '2001'"
        assert r[-1] == ['2017', 53], "Expect last row to be for year '2017' with a partial count of homicides"


        r = foo_4()
        assert type(r) is dict, 'Assert foo_4() returns dict'
        assert sorted(r.keys()) == ['fall', 'spring', 'summer', 'winter'], 'Expect four seasons, fall, spring, summer, winter'
        assert r['fall'] == 2168 , 'Expect fall to have had 2,168 homicides'
        assert r['summer'] > r['fall'], 'Expect summer to have more homicides than the fall'


        r = foo_5()
        assert type(r) is dict, 'Assert foo_5() returns dict'
        assert len(r.keys()) == 7, 'Assert 7 days in the week'
        # list of obj, sorted by most homicides per day
        mostdeaths = sorted(r.items(), key=lambda x: x[-1], reverse=True)
        print(mostdeaths[0])
        assert mostdeaths[0] == ('Saturday', 1461), 'Assert that most homicides are reported on Saturday'


    if __name__ == '__main__':
        foo_assertions()
        print("Done with assertions!")




That script should have a ``if __name__ == '__main__'`` conditional block, in which a function named ``assertions_foo()`` is executed.



Prompts
=======


The CSV data file for "Visits to and traffic sources for all participating agencies: Top traffic sources (30 days)"  has been mirrored here:

http://stash.compciv.org/2017/analytics.usa.gov-top-traffic-sources-30-days.csv

Download (and cache) that file, then parse/deserialize the text data, then write the ``foo_`` functions to satisfy the following prompts:

1. Count the total number of Chicago homicides
----------------------------------------------

Every row in this dataset corresponds to a homicide, so a simple counting of the rows will do what we need.

Expected result:

.. code-block:: python

    8282


Remember that when deserializing CSV data, values that are *number characters* are not converted to numbers automatically...


2. Count how many homicides have resulted in an arrest, as well as the arrest rate overall
------------------------------------------------------------------------------------------

The dataset includes a column titled ``Arrest``, which is either ``'true'`` or ``'false'``

Return a dictionary with these keys: ``'true'`` (i.e., an arrest was made), ``'false'``, and ``'rate'`` which is the percentage of homicides with an arrest.


Expected result:

.. code-block:: python


    return {'false': 4284, 'true': 3998, 'rate': 48.3}



3. List the number of homicides by year
---------------------------------------

Return a 2-column list in which the headers are `'year'` and `'count'`:

Expected answer:

.. code-block:: python

    [['year', 'count'],
     ['2001', 667],
     ['2002', 657],
     ['2003', 604],
     ['2004', 454],
     ['2005', 453],
     ['2006', 477],
     ['2007', 448],
     ['2008', 513],
     ['2009', 460],
     ['2010', 438],
     ['2011', 437],
     ['2012', 503],
     ['2013', 422],
     ['2014', 424],
     ['2015', 497],
     ['2016', 775],
     ['2017', 53]]


Hints
^^^^^

This one might be a little bit tricky, depending on how you think of things. In general, don't worry too much about what the final result looks like, because that can distract you from using a dictionary to do the counting:


.. code-block:: python

    mydict = {}
    for row in records:
        year = row['Year']
        if mydict.get(year):
            mydict[year] += 1
        else:
            mydict[year] = 1



After the counting is done, you can do whatever sorting, typecasting is needed to make a list of lists.

If you are tired of the same old loops and basic syntax and want to do things in a more Pythonic way, you can take this approach:

1. Create a new list from the homicides data that solely consists of the year for each homicide.
2. Use `collections.Counter <https://docs.python.org/3/library/collections.html>`_ to do the counting by value for you:



.. code-block:: python

    from collections import Counter
    yearcounts = Counter(r['Year'] for r in records)



4. Count homicides by season
--------------------------------

Create a dictionary with keys for ``'summer'``, ``'spring'``, ``'fall'``, ``'winter'``, in which the values correspond to how many homicides occurred during the given season.

Expected result:

.. code-block:: python

    {'fall': 2168, 'spring': 1931, 'summer': 2591, 'winter': 1592}


Hints
^^^^^

There is no "season" field in the dataset, but this is something we can come up with for ourselves.

Each data row has a ``'Date'`` column, which for our purposes, is just a string in this format:


    ``MM/YY/DD HH:MM:SS AM/PM``


I guess we could use the official starting dates for the seasons. But I'm going to simplify things by treating seasons as **quarters** -- i.e. the season of "summer" encompasses June, July, and August.

In the ``'Date'`` column, we don't have ``'July'`` and ``'June'``, but we do have ``'07'`` and ``'08'``, which can be converted into integers.

Proof of concept:

.. code-block:: python

    >>> datestr = '07/12/2016 09:18:00 PM'
    >>> datestr[0:2]
    '07'
    >>> int(datestr[0:2])
    7


Throw in a conditional expression as you iterate through each row, and you're in business:


.. code-block:: python

    records = get_and_parse_data()
    seasons_count = {'fall': 0, 'winter': 0, 'summer': 0, 'spring': 0}

    for r in records:
        mth = int(r['Date'][0:2])
        if mth in [9, 10, 11]:
            season = 'fall'
        elif mth in [12, 1, 2]:
            season = 'winter'
        elif mth in [3, 4, 5]:
            season = 'spring'
        elif mth in [6, 7, 8]:
            season = 'summer'

        seasons_count[season] += 1



5. Count homicides by day of week
---------------------------------

Using the ``'Date'`` value for each homicide record, use the ``datetime.strptime()`` function to convert the date string value into a proper Python date. Then use ``strftime()`` to extract the human-readable name of the day of the week, e.g. ``'Sunday'``.

Expected results:

.. code-block:: python

       {'Friday': 1091,
         'Monday': 1115,
         'Saturday': 1461,
         'Sunday': 1457,
         'Thursday': 1083,
         'Tuesday': 1044,
         'Wednesday': 1031})




Hints
^^^^^

Word of warning: dealing with the concept of time as a programmer is easily one of the most infuriating and painful parts of programming, when you discover that the notion of "now" is not at all what you thought it was.

Here's a fun read on Hacker News: https://news.ycombinator.com/item?id=4128208

So this exercise is not meant to expose you to the full pain of time-handling. It's just enough to know a few things:

- a date string is still a text string, and your Python program needs to be told in very explicit terms how to convert it to a proper datetime object.
- Computers just don't mark time the way we do. Come to think of it, what do humans use as a universal reference point in time?
- Converting what the computer considers to be a datetime object into something human-readable requires a mini-syntax of its own.


For our purposes, we need to bring in the ``datetime`` module, which has a ``datetime`` class.

And we need two methods from ``datetime``:

- ``strptime()`` - takes a date string as the first argument, and a pattern string as the second argument. Returns a DateTime object.
- ``strftime()`` - takes a pattern string as an argument and produces a human-readabble string of the formatted date.

You can read about both methods, and the pattern mini-language here:

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior



.. code-block:: python

    >>> from datetime import datetime
    >>> date_text = '03/27/1905'
    >>> date_obj = datetime.strptime(date_text, '%m/%d/%Y')
    >>> type(date_obj)
    datetime.datetime
    >>> date_obj
    datetime.datetime(1905, 3, 27, 0, 0)
    >>> date_obj.strftime('%Y-%m-%d')
    '1905-03-27'



Background
==========

The data for this exercise was downloaded from Chicago's Socrata data portal, from a view specifically filtered for crimes with a primary classification of ``'HOMICIDE'``:

https://data.cityofchicago.org/Public-Safety/Homicides/iyvd-p5ga/data

The full Chicago crime dataset can be found at this URL, and is one of the most comprehensive and detailed crime data resources available to the public:

https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2/data



The city of Chicago has long been a leader in publishing its crime data. Likewise, the Chicago Tribune has been a pioneer in news applications, ever since its excellent and still-running Crime in Chicagoland app:


http://crime.chicagotribune.com/



As you can see in the year-by-year compilation of the data, Chicago has shown a sharp jump in homicides even as the crime rate nationwide declines:


.. code-block:: text

     ['2011', 437],
     ['2012', 503],
     ['2013', 422],
     ['2014', 424],
     ['2015', 497],
     ['2016', 775],

I think it's a bit trite to think that data analysis and tools alone can find a magical solution to Chicago's headline-making homicide rate. On the other hand, Chicago's data is unusually detailed, allowing an opportunity to at least understand and examine trends beyond the general body count.

