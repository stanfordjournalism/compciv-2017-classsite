**********************************************
Web-scraping the Texas Executed Offenders List
**********************************************

**Due date:** 1:00 PM, 2017-02-09

**Points:** 20


A web-scraping exercise using a mirror of the Texas Department of Criminal Justice's executed offenders page:

http://wgetsnaps.github.io/tdcj-executed-offenders/death_row/dr_executed_offenders.html

The relevant reading about web-scraping in Python is here:

:doc:`/guide/topics/python-nonstandard-libraries/beautifulsoup`

This homework revisits the data that we used in: :doc:`/syllabus/assignments/homework/contrived-cli-data-crunching`


Although this is just an exercise in web-scraping, here are some examples of what has been done with scraping death penalty related data:

- Marshall Project's Next to Die: https://www.themarshallproject.org/next-to-die
- Goodbye Warden: http://www.goodbyewarden.com/


Requirements
============




Send an email to me with this subject: ``compciv-2017::your_sunet_id::texas-executed-scrape``

It should contain 3 scripts as attachments (details are described below):

- when-who.py
- young-old.py
- religious-last-words.py

Use this mirror of the Texas executed offenders page:

http://wgetsnaps.github.io/tdcj-executed-offenders/death_row/dr_executed_offenders.html



1. when-who.py: Print out date and race of executions
-----------------------------------------------------

When I run your Python script like this:


.. code-block:: shell

    $ python when-who.py


It should parse the Executed Offenders HTML table and print out 2-column CSV output of the date and the race of each executed offender. You can leave date in its plaintext format as found on the HTML page.

Thus, the first five lines of output should look like this:


.. code-block:: text

    race,date
    Black,11/18/2015
    Hispanic,10/14/2015
    Hispanic,10/6/2015
    Hispanic,08/12/2015


The last 5 lines should look like this:

.. code-block:: text

    White,01/16/1985
    White,10/30/1984
    White,03/31/1984
    White,03/14/1984
    Black,12/07/1982


.. warning:: Look at the whitespace

    Note the exact expected output, including the white space.

    Specifically, your first 5 lines should NOT look like this:

    .. code-block:: text

        race,date
        Black,11/18/2015
        Hispanic,10/14/2015
        Hispanic ,10/6/2015
        Hispanic,08/12/2015

    (use the string object's ``strip()`` method to remove trailing whitespace)



2. young-old.py: Oldest and youngest executed offenders
-------------------------------------------------------

When I run your Python script like this:

.. code-block:: shell

    $ python young-old.py


I expect to see this output:

.. code-block:: text

    Youngest offender to be executed was 24-year-old Toronto Patterson from Dallas County, on 08/28/2002
    Oldest offender to be executed was 67-year-old Lester Bower from Grayson county, on 06/03/2015


Note that this is a lesson about **sorting**, which we did in the last assignment.

Relevant reading: - `Sorting Python collections with the sorted method <http://www.compciv.org/guides/python/fundamentals/sorting-collections-with-sorted/>`_


For each BeautifulSoup row element, you need to tell the ``sorted`` function what to sort them by. The first row, then, will be the row element that belongs to the youngest executed offender (by age). The last row element is the offender with the highest age.


For example, if I wanted to sort inmates by last name, and just print out their full name, I might start out like this (again):

.. code-block:: python

    from bs4 import BeautifulSoup
    import requests
    url = 'http://wgetsnaps.github.io/tdcj-executed-offenders/death_row/dr_executed_offenders.html'
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    rows = soup.select('tr')[1:]


Then I would think of how to write a one-line function that would express how I want each "row" to be represented when doing a comparison:

.. code-block:: python

    def xfoo(thing):
        cols = thing.select('td')
        return cols[3].text


And then I would use the ``sorted()`` function and specify that the ``key`` function be ``xfoo``:

.. code-block:: python

    sortedrows = sorted(rows, key=xfoo)

And then loop through each element of ``sortedrows`` and print out the relevant columns:

.. code-block:: python

    for row in sortedrows:
        cols = row.select('td')
        lastname = cols[3].text
        firstname = cols[4].text
        print(firstname, lastname)



3. religious-last-words.py
--------------------------

When I run your Python script like this:

.. code-block:: shell

    $ python religious-last-words.py

I expect to see a comma-delimited list of first name, last name, and absolute URL of each inmate who mentioned a religious word in their last words, e.g. "God" or "Lord". I leave it to you to decide what those words are.


The output should look something like this:


.. code-block:: text

    Ricky,Green,http://wgetsnaps.github.io/tdcj-executed-offenders/death_row/dr_info/greenrickylast.html
    Marvin,Wilson,http://wgetsnaps.github.io/tdcj-executed-offenders/death_row/dr_info/wilsonmarvinlast.html


Hints
=====

In the past text-crunching assignment: :doc:`/syllabus/assignments/homework/contrived-cli-data-crunching`

Re-read the problem "State of Texas executions by year", and remember how you extracted a list of executions by year by treating the webpage as just text patterns to be parsed.

To get the count of executions by year, we had to extract the date pattern, which looks like this:


.. code-block:: shell

    $ curl -s http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html \
        |  ack -o '\d{2}/\d{2}/\d{4}'



Now that we know that HTML is something that can be parsed with Python's BeautifulSoup, let's do this date extraction the "proper" way.

Import the libraries:

.. code-block:: python


    from bs4 import BeautifulSoup
    import requests

    SRC_URL = 'http://wgetsnaps.github.io/tdcj-executed-offenders/death_row/
    dr_executed_offenders.html'


Download the page, and parse it as a BeautifulSoup object:


.. code-block:: python

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')


At this point, I encourage you to visit the executed offenders webpage in your browser and to **view the source**. I give one example of how to select the desired rows, but it is based on an assumption that every table row (``<tr>``) contains what we want, except for the very first table row, which is the header row:



.. code-block:: python

    rows = soup.select('tr')[1:]


How do we just print the date of each execution? Look at the webpage, and figure out which child element of each row (i.e. ``<td>``) contains the date of each execution. By my count, it is the **8th** column:


.. code-block:: python

    for row in rows:
        cols = row.select('td')
        datecol = cols[7]
        print(datecol.text)



Absolute versus relative URLs
-----------------------------

For the exercise in which you have to visit each "Last statement" page, you'll notice that each ``href`` value is something like this:

    dr_info/lopezdaniellast.html

However, your browser resolves that relative address to an absolute one:

    http://wgetsnaps.github.io/tdcj-executed-offenders/death_row/dr_info/lopezdaniellast.html


Python, nor BeautifulSoup, does this automatically for you. What you need to use is the built-in ``urllib.parse`` library:

https://docs.python.org/3/library/urllib.parse.html

Which has a ``urljoin()`` function:

https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin

An example of usage:

.. code-block:: python

    >>> from urllib.parse import urljoin
    >>> base_url = 'http://www.example.com'
    >>> full_url = urljoin(base_url, 'dan/cat.jpg')
    http://www.example.com/dan/cat.jpg


Please test this out for yourself and make sure you know what type of objects are being slung around. **Do not** do this in your program:

.. code-block:: python

    base_url = 'http://www.example.com'
    some_relative_href = 'dan/cat.jpg'
    full_url = base_url + some_relative_href


(because manually constructing URLs is menial work that should be delegated to a library!)



