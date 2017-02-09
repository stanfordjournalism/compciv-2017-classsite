*********************************************
csv - reading and writing delimited text data
*********************************************

Comma-separated value data is likely the structured data format that we're all most familiar with, due to CSV being easily-consumed by spreadsheet applications. It's not a coincidence that CSV is easy to understand and inspect because *it is just text*, and a hugely popular format for data interchange.

That said, it is not as simple as its name would seem to promise. Assuming that each line of a CSV text file is a new row is hugely naive because of all the edge cases that arise in real-world dirty data. This is why we turn to Python's **csv** library for both the reading of CSV data, and the writing of CSV data.



Quick reference
===============


`Automate the Boring Stuff has a chapter titled: Working with CSV Files and JSON Data <https://automatetheboringstuff.com/chapter14/>`

You can read the official ``csv`` documentation here: https://docs.python.org/3/library/csv.html

If you need a referesher on how to invoke the various ``csv`` functions and classes, here's a quick cheatsheet:


Creating a csv.reader() object from a file object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pass a file object into csv.reader():

.. code-block:: python

    import csv
    datafile = open('data.csv', 'r')
    myreader = csv.reader(datafile)

    for row in myreader:
        print(row[0], row[1], row[2])




Creating a csv.reader() object from string
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Split the string into lines of text, then pass into ``csv.reader()``:


.. code-block:: python

    import csv

    rawdata = 'name,age\nDan,33\nBob,19\nSheri,42'
    myreader = csv.reader(rawdata.splitlines())
    for row in myreader:
        print(row[0], row[1])



Using the first line of a dataset as headers for each deserialized data object (dicts)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``csv.DictReader``:

.. code-block:: python

    import csv
    rawdata = 'name,age\nDan,33\nBob,19\nSheri,42'
    myreader = csv.DictReader(rawdata.splitlines())

    for row in myreader:
        print(row['name'], row['age'])



Given a list of lists, how to serialize the data as a CSV text file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``csv.writer`` and its ``writerow()`` method, which takes in a ``list`` as an argument:


.. code-block:: python

    data = [
        ['Dan', 42],
        ['Cordelia', 33],
        ['Sammy', 52]
    ]

    import csv
    with open('outputdata.csv', 'w') as outfile:
        mywriter = csv.writer(outfile)
        # manually add header

        mywriter.writerow(['name', 'age'])
        for d in data:
            mywriter.writerow(d)


Given a list of dicts, serialize the data as CSV
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``csv.DictWriter``:


.. code-block:: python

    import csv
    data = [
        {'name': 'Pat', 'age': 78},
        {'name': 'Nancy', 'age': 23},
    ]

    headers = ['name', 'age']

    with open('outputdata.csv', 'w') as outfile:
        mywriter = csv.DictWriter(outfile, fieldnames=headers)
        mywriter.writeheader()

        for d in data:
            mywriter.writerow(d)


Understanding CSV as just text values separated by commas
=========================================================

The name "comma-separated values" promises a data format with the easiest kind of parsing: use a comma to separate each data value.

For simple data, it seems self-evident where the columns will go:


.. code-block:: text

    id,name,age
    7,James Bond,42
    11,Dani West,19

Saving that as a text file and opening up in a spreadsheet would result in this simple table:


.. csv-table::
    :header: "id", "name", "age"

    7,James Bond,4
    11,Dani West,19


If we wanted to parse each row's age value, we could read the above text as one big string and split the string by lines:

.. code-block:: python


    rawtext = """id,name,age
    7,James Bond,42
    11,Dani West,19"""

    records = rawtext.splitlines()


Try the above snippet in the interactive shell, and test out what ``records`` actually is.


.. code-block:: python

    >>> type(records)
    list
    >>> len(records)
    3
    >>> records
    ['id,name,age', '7,James Bond,42', '11,Dani West,19']
    >>> records[1]
    '7,James Bond,42'



Let's pretend we wanted to print out the *age* "column" of each row, each row being a line of text, and ``records`` being a list of lines of text:


.. code-block:: python

    >>> row = records[1]
    >>> type(row)
    str
    >>> row
    '7,James Bond,42'

We could use a regular expression to extract the pattern that represents the age (a number at the end of the line). But we could also do something simpler: split the ``row`` string by *comma*, which gives us a list of strings. And then the age value is the last value in that list:


.. code-block:: python


    >>> row = records[1]
    >>> vals = row.split(',')
    >>> type(vals)
    list
    >>> len(vals)
    3
    >>> vals[1]
    'James Bond'
    >>> vals[2]
    '42'



To print out the ages of each line using a for-loop:

.. code-block:: python

    for row in records:
        vals = row.split(',')
        age = vals[2]
        print("Age:", age)


.. code-block:: text

    The output:

    Age: age
    Age: 42
    Age: 19



When CSV is more than just commas
---------------------------------


Unfortunately, the CSV specification is not simply, "a comma means that there is a column". Take this example, in which the name isn't ``James Bond``, but ``James Bond, Jr.``.

This throws an obvious wrench in our data structure: the "James Bond" column now has 4 columns, if we go only by literal commas:


.. code-block:: text

    id,name,age
    7,James Bond, Jr.,42
    11,Dani West,19


How are commas that are part of a data field handled? In some situations by double quoting the field:


.. code-block:: text

    id,name,age
    7,"James Bond, Jr.",42
    11,Dani West,19

But what happens when a text field contains a comma *and* double quotes? Then you need to double-quote the field. But when we realize that there are many ways for text data to get messy -- including the inclusion of **newline characters** within a column, rather than just what we use to delimit rows -- then it becomes obvious the official `CSV specification is more or less considered a disaster <https://en.wikipedia.org/wiki/Comma-separated_values#Specification>`_.

Certainly, it is not possible to sanely extract data from CSV-formatted text using the string ``split()`` method and regular expressions alone. We need to use Python's build in ``csv`` library.


What is deserialization and serialization
=========================================

Before moving on to the specifics of CSV, it's important to see the big picture.

As I've said from the very beginning, virtually all of the important data we deal with comes as plain text, whether it is:

- Earthquake data from the USGS: https://github.com/helloworlddata/usgs-earthquakes
- FEC campaign finance: http://www.fec.gov/finance/disclosure/ftp_download.shtml
- NASA climate data: https://data.giss.nasa.gov/
- Tweets from politicans: https://dev.twitter.com/streaming/overview
- Congressional voting records: https://propublica.github.io/congress-api-docs/
- Crime data: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2/data

However, it's not just raw text that we want. It needs to be **structured** text -- text without structure is just noise. But when there *is* structure, then we can turn text into data objects -- particularly, lists and dictionaries -- that we can use in our programs.

The **csv** library is Python's built-in, no-fuss way of turning raw text into a list of lists, or list of dicts. If you can open a text file for reading, you can convert it into data via ``csv``'s methods. Conversely, if you have lists and dicts in Python, you can *serialize* them to be stored as text, which means you can port your data objects in such a way that someone else can deserialize and import them for their own programs.


Basically, all of what we learn here are the steps needed to turn raw text into data objects, and as far as we're concerned, it's just more libraries and functions to remember.



The curious complexity of the ``csv`` library
---------------------------------------------

I'll be honest: if you thought reading and writing files was complicated, then I have to warn you that the ``csv`` library throws in extra layer of "is-this-thing-a-file-or-what-is-it??" confusion. Or at least it did for me -- not until very late in my Python programming experience did it make sense to me why all the steps for converting raw text into data objects via csv were needed.

But I'll try to present the library as a list of useful recipes. You might not get all of the steps, but if you just follow, and repeat them, you'll eventually understand the nuance of turning text into data, and vice versa.

The important thing is, just by doing these steps, you'll be able to turn text into data. And virtually all of the important data we deal with is text from someone else that we need to import into our program.



Deserializing CSV text files with the ``csv.reader``
====================================================

First, to bring the ``csv`` library into our programs, we have to import it. Include this at the beginning of your work:

.. code-block:: python

    import csv



Reading the raw text data
-------------------------

For this lesson, let's use a trivial data file. You can view it at this URL:

http://stash.compciv.org/2017/simple-people.csv


The contents are simply this:


.. code-block:: text

    name,age
    Alice,24
    Bob,19
    Charles,42

And let's have an end goal to our data work: we want to calculate the total age of each person in this data list


.. rubric:: Loading the data

You can do this however you like. You can copy/paste the simple bit of text and load it in as a string, and then invoke ``splitlines()`` so that the ``records`` variable is a list of text lines:

.. code-block:: python

    rawtext = """name,age
    Alice,24
    Bob,19
    Charles,42"""

    records = rawtext.splitlines()


Or you could download the contents of the URL as text and save yourself the copy-pasting of that data:


.. code-block:: python

    import requests
    url = 'http://stash.compciv.org/2017/simple-people.csv'
    rawtext = requests.get('url').text
    records = rawtext.splitlines()


Or you could do the full steps, from downloading the data, to saving a local copy, to then reading text from a file object:


.. code-block:: python

    import requests
    url = 'http://stash.compciv.org/2017/simple-people.csv'
    rawtext = requests.get('url').text
    destname = 'simple-people.csv'
    with open(destname, 'w') as wf:
        wf.write(rawtext)


    with open(destname, 'r') as rf:
        rawtext = rf.read().splitlines()




You can save those 4 lines of text in a text file named ``rawdata.csv``.

Or you can store it in a string, with the variable name of ``rawtext``.

I'll assume that for the remainder of this exercise, you have a variable named ``records`` which is the result of either of these data loading steps:




Reading the raw text data with csv.reader() function
----------------------------------------------------

The ``csv.reader()`` function accepts either a file object, or a list of CSV-formmated text strings. So either of these setups would work in instantiating the ``myreader`` object:


If you managed to turn the raw text data into a file, which you then opened as a file-object, then this would work:

.. code-block:: python

    import csv
    f = open('simple-people.csv', 'r')
    myreader = csv.reader(f)



Or, just pass in a list of CSV-formatted text strings:

.. code-block:: python

    import csv

    rawtext = """name,age
    Alice,24
    Bob,19
    Charles,42"""

    records = rawtext.splitlines()
    myreader = csv.reader(records)



What is ``myreader``. Using ``type()`` reveals that it is a ``_csv.reader`` type-object with apparently no useful methods, such as ``read()`` or ``give_me_data()``.

In fact, we're not meant to have any kind of special interaction with ``myreader``. It should be treated as a collection-type object to iterate through. For example, this is how to print each ``age`` value for each line:



.. code-block:: python

    for row in myreader:
        print('Age is:', row[1])

The resulting output:

.. code-block:: text

    Age is: age
    Age is: 24
    Age is: 19
    Age is: 42



Each ``row`` in the iterator is a ``list`` object. Index ``0`` is the *name* value, and ``1`` is the *age* value.



Using ``list()`` to get past laziness
-------------------------------------

As with all file operations, once we've iterated through a file object/stream, in this case, the stream that ``myreader`` has wrapped around, re-running our loop from above will return nothing, because ``myreader`` is exhausted of data. We have to re-load it with data, i.e. re-open and re-consume the text stream:


.. code-block:: python

    myreader = csv.reader(rawtext.splitlines())


However, we don't have to interact with ``myreader`` via a for-loop. We can pass ``myreader`` into the ``list`` function, which converts ``myreader`` into a list of lists:

.. code-block:: python

    myreader = csv.reader(rawtext.splitlines())
    records = list(myreader)

    for row in records:
        print("The age is:", row[0])




Forcing the ``myreader`` object to turn into a list is basically the same thing as creating an empty list, and looping through ``myreader`` and appending each object of the iteration to the empty list:


.. code-block:: python

    records = []
    myreader = csv.reader(rawtext.splitlines())
    for row in myreader:
        records.append(row)



Either way, if you're doing this in the shell, you can inspect the ``records`` data structure as you please:


.. code-block:: python

    >>> type(records)
    list
    >>> len(records)
    4
    >>> records
    [['name', 'age'], ['Alice', '24'], ['Bob', '19'], ['Charles', '42']]
    >>> records[0]
    ['name', 'age']
    >>> type(records[0])
    list
    >>> len(records[0])
    2
    >>> records[1]
    ['Alice', '24']
    >>> age = records[1][1]
    >>> age
    '24'
    >>> type(age)
    str



Numbers in text files are treated like strings
----------------------------------------------

Take a look at the last line of this interactive output. That is, what does the ``age`` value *look* like to us humans and what do we *want* it to mean, versus, what does the Python interpreter think it is?

Most humans associate "age" with anumber, so, Alice's age is the number ``24``. However, in a plaintext import, numbers are always treated as text -- the ``csv.reader() does not do any processing other than figuring the structure of the data based on the use of commas.

That means our original goal of adding up ages will not work with simple, naive addition of values:


.. code-block:: python

    >>> '24' + '19' + '42'
    '241942'


If you're coming here from R and its `convenient ``read.csv`` functionality <http://stackoverflow.com/questions/13265153/how-do-i-import-a-csv-file-in-r>`_, you'll have to go to a high-level library like `Pandas <http://pandas.pydata.org/>`_ to get the same convenience in Python.

We will be using ``pandas`` for serious data-crunching. but as always, I recommend you think of the low-level ways of solving this problem, so you don't mistake ``pandas`` for magic.

What can we use to convert a text string of numbers into actual numbers? The ``int()`` function:


.. code-block:: python

    >>> int('24') + int('19') + int('42')
    85



Tracking a total sum
--------------------

Let's put it all together, from the code deserialziing raw text into Python data structures, to using a loop to read each *age* value, to writing the logic necessary to track the total age:


Note that I add a couple of lines of boilerplate:

- I initialize a ``total_age`` variable with which I use to track the sum of ages.
- I assign ``records[0]`` to ``headers``. as the first row of the text data is just the column names.

We don't really need the column names to do the summation of ages, it just makes clearer why I skip the first row of ``records`` in the for loop:

.. code-block:: python

    headers = records[0]
    for row in records[1:]:
        age = int(row[1])


OK, all together:

.. code-block:: python

    import csv
    import requests

    url = 'http://stash.compciv.org/2017/simple-people.csv'
    rawtext = requests.get(url).text
    myreader = csv.reader(rawtext.splitlines())
    records = list(myreader)

    total_age = 0
    headers = records[0]
    for row in records[1:]:
        age = int(row[1])
        total_age += age

    print("The total age is:", total_age)


The output:

.. code-block:: text

    The total age is: 85


Variations
^^^^^^^^^^

Of course there are variations depending on how much you like brevity. Here's a variation that doesn't waste time turning ``csv.reader()`` into a list, when we can iterate through the reader object as if it were a list:

.. code-block:: python

    import csv
    import requests

    url = 'http://stash.compciv.org/2017/simple-people.csv'

    total_age = 0
    textlines = requests.get(url).text.splitlines()
    for row in csv.reader(textlines[1:]):
        total_age += int(row[1])

    print("The total age is:", total_age)



And this is why we learn list comprehensions, a beautiful bit of Python syntax sugar:



.. code-block:: python

    import csv
    import requests

    url = 'http://stash.compciv.org/2017/simple-people.csv'

    textlines = requests.get(url).text.splitlines()
    records = csv.reader(textlines[1:])
    ages = [int(row[1]) for row in records]
    print("The total age is:", sum(ages))




Creating a list of cits with ``csv.DictReader()``
=================================================


Let's use the same simple data set found here:

http://stash.compciv.org/2017/simple-people.csv


But this time, let's parse the data using the ``csv.DictReader`` class, which you can read about in the `official documentation <https://docs.python.org/3/library/csv.html#csv.DictReader>`_.

Basically, ``csv.DictReader`` works just like ``csv.reader``, except instead of giving us a list of lists, we get a list of dictionaries:


.. code-block:: python

    import csv
    import requests
    url = 'http://stash.compciv.org/2017/simple-people.csv'
    textlines = requests.get(url).text.splitlines()

    r_lists = list(csv.reader(textlines))
    r_dicts = list(csv.DictReader(textlines))



Using the interactive shell to inspect the ``r_lists`` and ``r_dicts`` objects:

.. code-block:: python

    >>> type(r_lists)
    list
    >>> type(r_dicts)
    list
    >>> len(r_lists)
    4
    >>> len(r_dicts)
    3
    >>> x = r_lists[0]
    >>> type(x)
    list
    >>> x
    ['name', 'age']
    >>> y = r_dicts[0]
    >>> type(y)
    dict
    >>> y
    {'age': '24', 'name': 'Alice'}
    >>> y['age']
    '24'


Initializing the  ``csv.DictReader`` class is the same process as ``csv.reader()``, but the two methods differ in they process the lines of text. The ``DictReader()`` method assumes that the first line is the column headers, and thus are not meant to be actual data. That's why the ``DictReader`` version produced only 3 rows, compared to the 4 rows produced by ``csv.reader``, due to the header/column-heads being counted as a data row.

Not much changes beyond that. To count up the ages using a list of dicts looks like this, but note how I don't have to skip the first row in ``records`` because I know it isn't simply a header row:


.. code-block:: python

        total_age = 0
        records = list(csv.DictReader(textlines))
        for row in records:
            age = int(row['age'])
            total_age += age

        print("The total age is:", total_age)


Note the column accessor is, depending on how you think of things, easier to grok because it uses a human-readable reference:


.. code-block:: python

            age = int(row['age'])

Whereas with the list created by csv.reader, we have to remember that index 1 contains the age value in the dataset. Simple enough in a simple dataset, but not reasonabe in certain real-world scenarios.




When to use csv.DictReader vs csv.reader?
-----------------------------------------

``DictReader`` for all the situations when the ``dict`` data structure is better than a list. In particular, when datasets have a lot of columns, it is pretty much impossible to refer to columns by their numerical order.

Take, for example, the NYPD Stop and Frisk Data (`landing page <http://www.nyc.gov/html/nypd/html/analysis_and_planning/stop_question_and_frisk_report.shtml>`_).

You can download the 2015 data here:

http://stash.compciv.org/2017/nypd-stop-and-frisk-2015.csv

The first thing you'll notice is that there are a huge number of columns, more than a 100+. If we want to do a count of how many blacks were stopped and frisked in 2015, then we need to find the ``race`` column, which might require reading the data documentation to find that it is column 82 (81 with a 0 index):


.. code-block:: python

    import requests
    import csv
    url = 'http://stash.compciv.org/2017/nypd-stop-and-frisk-2015.csv'
    RACE_COL_INDEX = 81

    # this is a fairly hefty download
    resp = requests.get(url)
    lines = resp.text.splitlines()

    bcount = 0
    tcount = 0
    for cols in csv.reader(lines[1:]):
        tcount += 1
        if cols[RACE_COL_INDEX] == 'B':
            bcount += 1

    print(bcount, 'blacks were stopped, out of', tcount, 'total stops in 2015')


However, with dictionaries, we just have to know that there is a column named ``race``:


.. code-block:: python

    import requests
    import csv
    url = 'http://stash.compciv.org/2017/nypd-stop-and-frisk-2015.csv'

    # this is a fairly hefty download
    resp = requests.get(url)
    lines = resp.text.splitlines()

    bcount = 0
    tcount = 0
    for cols in csv.reader(lines):
        tcount += 1
        if cols['race'] == 'B':
            bcount += 1

    print(bcount, 'blacks were stopped, out of', tcount, 'total stops in 2015')




However, there are some datasets in which you don't need that kind of dictionary key access. For example, a 2-column dataset. Or a dataset that has no headers.






Serializing Python data objects as CSV
======================================


Writeup TK: But it's pretty straightforawrd:


Writing a CSV-formatted text-file, row-by-row, with csv.writer()
----------------------------------------------------------------


Use the ``csv.writer`` class, and pass in a file object that is set for writing:


.. code-block:: python


    import csv

    destname = 'outdata.csv'
    destfile = open(destname, 'w')

    mywriter = csv.writer(destfile)
    mywriter.writerow(['name', 'age'])
    mywriter.writerow(['Dan', 42])
    mywriter.writerow(['Alice', 37])


    destfile.close()


Writing a CSV-formatted text file using dictionaries
----------------------------------------------------

Use the ``csv.DictReader`` class. However, initializing the DictReader object requires passing in a ``fieldnames`` argument, a list of the exact column headers you intend to include, as well as their exact order. ``DictReader`` can't infer from individual dict objects alone what the CSV structure should be like:


.. code-block:: python


    import csv

    destname = 'outdata.csv'
    destfile = open(destname, 'w')

    mywriter = csv.DictWriter(destfile, fieldnames=['party', 'name', 'age'])
    # this is how we add the header to the text file
    mywriter.writeheader()

    mywriter.writerow({
        'name': 'Bob',
        'party': 'R',
        'age': 25
    })
    mywriter.writerow({
        'age': 67,
        'name': 'Cordelia',
        'party': 'D',
    })


    destfile.close()


Notice how the key/value pairs for the dictionaries can be in any order -- ``DictWriter`` takes care of ordering them in the output text file:


.. code-block:: text

    party,name,age
    R,Bob,25
    D,Cordelia,67

