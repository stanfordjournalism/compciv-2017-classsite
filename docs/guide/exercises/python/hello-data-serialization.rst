*********************************************
Hello Data De-Serialization with JSON and CSV
*********************************************


Just in case you need more practice with the concept of converting a string of text into Python data objects such as dictionaries and lists, here are 16 exercises involving a very trivial, nonsensical dataset that has been serialized into JSON and CSV.

http://stash.compciv.org/2017/helloworld.json

http://stash.compciv.org/2017/helloworld.csv


Note: in order to make it so both text files conveyed roughly the same information, I deliberately made the CSV file, well, not a CSV file by throwing in unstructured text at the top of the file. This is actually something you'll see in real-world datasets, where a dataset owner will insert text meant as metadata, such as a copyright notice or contact address, which will cause CSV-parsing programs such as Excel to think that the actual "data" is messed up.

So how to get around this? Remember that a CSV text file, when opened and read, is just a plain Python string. Are there parts of that string that are irrelevant to what you want to send to the CSV parser, i.e. ``csv.reader()``? Then don't send those parts of the string.

What you should know
====================

You should be familiar enough with the **csv** and **json** built-in libraries and methods for serializing text strings into data objects:


.. code-block:: python

    import csv
    import json

    data = csv.reader(csvtext.splitlines())
    # or...
    data = csv.DictReader(csvtext.splitlines())

    # or...
    data = json.loads(jsontext)

    # or...
    data = json.load(jsonfilename)



And you should know how to tell the difference between a Python **list** and a Python **dict**, and how to get around the internals of their respective structures.

Particularly:

- That lists are "zero-indexed"
- What ``KeyError`` and ``IndexError`` mean.
- The difference between ``mydict['somekey']`` and ``mydict.get('somekey')`` (assuming ``mydict`` is a dictionary)
- The very important difference between ``mydict[5]`` and ``mydict['5']``.
- The difference between ``mydict.keys()``, ``mydict.values()``, and ``mydict.items()``
- The difference between ``mylist.append(5)`` and ``mylist.append([5])``, assuming ``mylist`` is a list
- The difference between ``mylist.append([5])`` and ``mylist.extend([5])``, assuming ``mylist`` is a list

And, of course, how to create a sorted copy of a dictionary or list, sorted by any key/field you want.


Relevant readings
^^^^^^^^^^^^^^^^^

- "Automate" chapter on Lists: https://automatetheboringstuff.com/chapter4/
- "Automate" chapter on Dictionaries and Structuring DatA: https://automatetheboringstuff.com/chapter5/
- "Automate" chapter on Working with CSV files and JSON data: https://automatetheboringstuff.com/chapter14/
- An introduction to data serialization and Python Requests http://www.compjour.org/tutorials/intro-to-python-requests-and-json/
- A quiz on dicts and lists: http://www.compjour.org/homework/json-quiz-part-1/
- :doc:`/guide/topics/python-standard-library/csv`
- Python's documentation for the csv library: https://docs.python.org/3/library/csv.html
- Python's documentation for the json library: https://docs.python.org/3/library/json.html
- Sorting in Python with the sorted method(): http://www.compciv.org/guides/python/fundamentals/sorting-collections-with-sorted/





Bored of loops and conditionals?
--------------------------------

If you have programming experience from CS106 and are wanting to practice something other than the programming fundamentals of loops, conditionals, and basic data structures, then attempt to solve these data exercises the "Pythonic" way.




.. rubric:: Use a list comprehension instead of a for-loop to build a new list

http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html


Instead of:

.. code-block:: python

    newlist = []
    for x in oldlist:
        myval = x['mykey']
        newlist.append(myval)

Try:

.. code-block:: python

    newlist = [x['mykey'] for x in oldlist]


.. rubric:: Use specialized data structures from the collections module


Python's **collections** module has a few variations on the standard Python list and dict types:

https://docs.python.org/3/library/collections.html

For example, given this list of lists:

.. code-block:: python

    vote_results = [
        ['Trump', 48],
        ['Clinton', 46],
        ['Trump', 24],
        ['Clinton', 23],
        ['Gary', 2]
    ]

We want to get do a **group count** by grouping the lists by their "name" values (e.g. ``'Trump', 'Clinton'``) and summing up their "count" values, e.g. ``48`` and ``23``. The result should be a dictionary like this:



.. code-block:: python

     {'Clinton': 69, 'Gary': 2, 'Trump': 72}


To do this using just standard loops and a dictionary:

.. code-block:: python

    tally = {}
    for row in vote_results:
        candidate = row[0]
        votes = row[1]
        if tally.get(candidate):
            tally[candidate] += votes
        else:
            tally[candidate] = votes


But here's one alternative simplification using the ``defaultdict`` type:


.. code-block:: python

    from collections import defaultdict
    tally = defaultdict(int)
    for row in vote_results:
        candidate = row[0]
        votes = row[1]
        tally[candidate] += votes



.. rubric:: Unpacking argument lists

https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

Instead of this:

.. code-block:: python

    results = [['Trump', 48, 'Iowa'], ['Clinton', 46, 'Michigan']]
    for row in results:
        candidate = row[0]
        votes = row[1]
        state = row[2]


Do:


.. code-block:: python

    results = [['Trump', 48, 'Iowa'], ['Clinton', 46, 'Michigan']]
    for row in results:
        candidate, votes, state = row





The questions
=============

All of these questions are meant to be answered by writing functions that return the desired value. The questions apply to both the CSV and JSON version of the data, and the ansewrs should be the same.

Basically, create a single Python script file. And for each question, create an appropriately-numbered function, e.g. ``foo_1`` through ``foo_8``. And each function should have a return statement.

Also, each function should be self-contained in that they download from the relevant data URL and deserialize the downlaoded text into a Python object.


1. In the metadata, what is the value for the `status` key?
-----------------------------------------------------------

Expected result:

.. code-block:: python

    'SUPER!'


2. How many inventory records are there?
----------------------------------------

Expected result:

.. code-block:: python

    5


3. Get an alphabetized list of the names of each inventory item
---------------------------------------------------------------

Expected result:

.. code-block:: python

    ['apples', 'cats', 'dogs', 'kiwis', 'zebras']



4. Get a sum of all the inventory item counts
---------------------------------------------

Expected result:

.. code-block:: python

    607


5. Filter inventory for the "animal" items, and create ordered list of ['animalname', animalcount] pairs
--------------------------------------------------------------------------------------------------------


Expected result:

.. code-block:: python

    [['zebras', 180], ['dogs', 42], ['cats', 9]]



6. Filter inventory for "fruit" items, create ordered list of trimmed-dictionary objects
----------------------------------------------------------------------------------------

Expected result:

.. code-block:: python

    [{'count': 76, 'name': 'kiwis'}, {'count': 300, 'name': 'apples'}]


7. Do a group count of inventory items by their "type"
-----------------------------------------------------

Expected result:

.. code-block:: python

    {'animal': 3, 'fruit': 2}

8. Do a summation of item counts, grouped by "type"
---------------------------------------------------

Expected result:

.. code-block:: python

    {'animal': 231, 'fruit': 376}





The data, as JSON and CSV
=========================

Here's what the JSON looks like:

http://stash.compciv.org/2017/helloworld.json


.. code-block:: json

    {
      "status": "SUPER!",
      "hello": "world",
      "inventory": [
        {
          "name": "dogs",
          "type": "animal",
          "count": 42
        },
        {
          "name": "apples",
          "type": "fruit",
          "count": 300
        },
        {
          "name": "kiwis",
          "type": "fruit",
          "count": 76
        },
        {
          "name": "zebras",
          "type": "animal",
          "count": 180
        },
        {
          "name": "cats",
          "type": "animal",
          "count": 9
        }
      ]
    }



And here's what the CSV version looks like:

http://stash.compciv.org/2017/helloworld.csv

::

    status:SUPER!
    hello:world
    ---
    name,type,count
    dogs,animal,42
    apples,fruit,300
    kiwis,fruit,76
    zebras,animal,180
    cats,animal,9




Solutions
=========


For the JSON-formatted data
---------------------------

..  literalinclude:: /code/python/hello-json.py




From the CSV-formatted data
----------------------------

..  literalinclude:: /code/python/hello-csv.py







