****************
Congress Bio Fun
****************

This is a set of exercises to flesh out your understanding and usage of variables, functions, importing libraries, loops, and conditional statements.

There's a lot I don't expect you to know off the top of your head, such as how to use Python to unzip a file, or to turn a color photo into black/white. That's OK, because there will always be a lot you don't "know" when programming, so you learn how to abstract those parts out, or at least understand by example.


.. note:: Delays

    If you're reading this for class, I'm still figuring out the exact requirements for this assignment and all the documentation that I need to provide. I'll send out an email when things are more step-by-step.


Rubric
======

Due date:
    1:00 PM, 2017-02-02


.. csv-table::
    :header: "Points", "Metric"
    :widths: 10, 90

    1,"Having a correct subject headline of ``compciv-2017::your_sunet_id::congress-bio-fun``"
    5,"Your email contains attachaments 1.py through 4.py"
    5,"All of your programs have the logic for bootstrapping data files"
    20,"Your scripts produce the expected output"


The Work
========


The datafiles:


- The 114th Congress: http://stash.compciv.org/2017/114th-congressmembers.csv
- The entire list of members of Congress: http://stash.compciv.org/2017/historical-congress-legislators.csv
- A zip file of members of Congress mugshots: http://stash.compciv.org/2017/congress-mugshots.zip



1. Which Congressmember's birthday is it today?
-----------------------------------------------

Inspired by one of the applets from `ProPublica's IFTTT <https://www.propublica.org/nerds/item/propublicas-on-ifttt>`_

Download a list of members of Congress. For every member whose birthday is today, print a message to standard output.

The list of members of the 114th Congress:
http://stash.compciv.org/2017/114th-congressmembers.csv



For Senators, the message should look like this:

.. code-block:: text

    "Happy [n]th Birthday, Pat Doe, [Democrat/Republican/etc] Senator from [State].


For House Representatives for states with just one district:

.. code-block:: text

    "Happy [n]th Birthday, Pat Doe, [Democrat/Republican/etc] Representative from [State].


And for states with multiple House districts:

.. code-block:: text

    "Happy [n]th Birthday, Pat Doe, [Democrat/Republican/etc] Representative from the [n]th District of [State].





2. Congress in Duotone
----------------------

Download a list of members of the 114th Congress and a list of their official headshots. For any given state, create a folder that contains the headshots, except with duotone coloring, i.e. red for Republicans, blue for Democrats, purple for Independents.

For Iowa, your program should create a subfolder named ``IA`` and have the photos for the 2 Senators and 4 representatives.

The list of members of the 114th Congress:
http://stash.compciv.org/2017/114th-congressmembers.csv

A zip file of Congressional mugshots:
http://stash.compciv.org/2017/congress-mugshots.zip



3. Congress Web Album
---------------------

Create a simple webpage that, for every state, prints a headline, e.g. ``<h2>NY</h2>`` followed by a list of duotone-mugshots for each Congressmember.


The list of members of the 114th Congress:
http://stash.compciv.org/2017/114th-congressmembers.csv

A zip file of Congressional mugshots:
http://stash.compciv.org/2017/congress-mugshots.zip


4. How many Stanford alumni made it to Congress?
------------------------------------------------

Using the data file of all Congressmembers in history, make a list of every legislator who attended/graduated Stanford by scraping the `Congressional Bioguide <http://bioguide.congress.gov/biosearch/biosearch.asp>`_

Here is the historical data file of Congressmembers:

http://stash.compciv.org/2017/historical-congress-legislators.csv



The Steps
=========

The trick to this assignment is to see it as a bunch of small steps. In the section below, I describe all of the small steps, the details of which you aren't expected to just know, but will eventually be familiar with.


How to download a file
----------------------

The following snippet makes a HTTP request (i.e. what you do when you visit a URL in the browser) and stores the response in a variable named ``resp``:

.. code-block:: python

    import requests
    url = 'http://stash.compciv.org/2017/114th-congressmembers.csv'
    resp = requests.get(url)


Note that the snippet does not do the following:

- Saves the contents of the response to your computer.
- Parses the contents of the response as "data"


In your interactive shell, run the above snippet and  use the ``type`` function to see the type of object of ``resp``.

Inspect its methods by typing ``resp.`` (i.e. add the dot operator) and hit ``Tab`` to bring up a list of available methods and attributes.



How to save a (text) file to disk
---------------------------------

Reading/writing files is a big subject on its own -- the Automate book has a nice detailed chapter on `Reading and Writing files <https://automatetheboringstuff.com/chapter8/>`_.

The following snippet will create a file named ``hello.txt`` that simply contains the text, ``hello world``. Note that there is no downloading of a file to save it, we're just concerned with how to save a file:


.. code-block:: python

    dest_filename = 'hello.txt'
    stuff = 'hello world'
    df = open(dest_filename, 'w')
    df.write(stuff)
    df.close()

A few things to note:

- Where does ``hello.txt`` exist? It's wherever you ran the above code. That is, if you ran ``ipython`` from your home directory, you will see ``hello.txt`` in your home directory (so, you should probably run ``ipython`` from some directory that you don't mind cluttering up). Look for ``hello.txt`` and open it and make sure it contains what we wrote to it.
- What is ``df``? Use the ``type()`` function to inspect it yourself. The main concept is that the variable ``dest_filename`` is just the string of text that represents the **filename**. The ``df`` object is the "file handler" -- the actual file object that is being opened and written to. Confusing the filename with the file itself is one of the most common mistakes to make, becausewe normally think of files by their names.
- There's a difference between writing a text file, and writing a **binary file** -- i.e. everything that is not text, which includes image files, zip files, etc. For now, just note how I invoke the ``open()`` function, specifically, the second argument of ``'w'``.



How to download a (text) file and save it to disk
-------------------------------------------------

Let's download a file and write it to your hard drive. It's a combination of the two previous steps, with the additional knowledge that the ``resp`` object has a ``text`` attribute, which, if you inspect it with ``type``, is a ``str`` object, just like ``'hello world'`` is of type ``str``:


.. code-block:: python

    import requests
    url = 'http://stash.compciv.org/2017/114th-congressmembers.csv'
    resp = requests.get(url)
    stuff = resp.text

    dest_filename = 'hello.txt'
    df = open(dest_filename, 'w')
    df.write(stuff)
    df.close()



How to download a binary file and save it to disk
-------------------------------------------------

An image file is an example of a binary file, i.e. something that is read as a stream of **bytes**, not text.

For example, visit the following URL to see an image of the Stanford logo:

http://stash.compciv.org/2017/stanford-logo.png

Downloading a binary file is the same as a text file, but what differs is how we access it from the ``resp`` object, and how we open the file object for writing. See if you can notice the differences:


.. code-block:: python

    import requests
    url = 'http://stash.compciv.org/2017/stanford-logo.png'
    resp = requests.get(url)
    stuff = resp.content

    dest_filename = 'logo.png'
    df = open(dest_filename, 'wb')
    df.write(stuff)
    df.close()


Use the ``type`` function on ``stuff`` -- you'll see that its type is not ``str`` but ``bytes``. And hence, why we call ``open`` with the ``'wb'`` argument (short for "write bytes").

There's a lot more to why some things are considered "text" in Python, and some things are "bytes", even though technically every thing a computer handles is in bytes. Right now, it's enough to be aware that there is a difference. And if you make the wrong call, you'll either get an error or garbage data.




How to make a directory
-----------------------

Now we're diving into even more boring detail: how to make a directory (i.e. a folder) using Python. There's many ways to do it, but let's start with the most straightforward: the ``makedirs`` function from the ``os`` package:

.. code-block:: python

    from os import makedirs
    makedirs('mytestdirectory')

Wherever you run this code, an empty directory named ``mytestdirectory`` should exist.


How to avoid an error caused by trying to create an already existing directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Try running ``makedirs()`` again. You should get an error complaining that the directory already exists:

.. code-block:: text

    FileExistsError: [Errno 17] File exists: 'mytestdirectory'

Frequently, we'll write programs that are run multiple times without knowing what pre-conditions are, i.e. if a program has already run and created the directory. We don't want this ``FileExistsError`` to stop our program. We can tackle this issue in 2 ways:

We could use an if-conditional statement and the ``os.path.exists`` method to test if the path *doesn't* exist. If that's the case, then create the directory:


.. code-block:: python

    from os.path import exists
    my_dirname = 'mytestdirectory'
    if not exists(my_dirname):
        makedirs(my_dirname)


Or, we could look at the `specification for the makedirs function <https://docs.python.org/3/library/os.html#os.makedirs>`_ and see that has an optional ``exist_ok`` argument that is, by default, set to ``False``. Set it to ``True`` and ``makedirs`` won't throw a ``FileExistsError``:

.. code-block:: python

    makedirs('mytestdirectory', exist_ok=True)


How to not download an existing file
------------------------------------

For some situations, it's not worth re-downloading a file, over and over, especially if the file is large. So we can use an if statement to check the existence of a file path before trying to download and save to it:


.. code-block:: python

    from os.path import exists
    import requests
    url = 'http://stash.compciv.org/2017/test.zip'
    destname = 'mytest.zip'

    if not exists(destname):
        print("Downloading", url)
        resp = requests.get(url)

        print("Saving to", destname)
        df = open(destname, 'wb')
        df.write(resp.content)
        df.close()

    else:
        print(destname, "already exists; skipping download")



How to unzip a file
-------------------

The `shutil <https://docs.python.org/3/library/shutil.html>`_ library contains the ``unpack_archive`` function, which takes a filename and unpacks it.

To test it out, download this test zip file at this URL:

http://stash.compciv.org/2017/test.zip

It's a simple zip file which contains a single text file (``data.txt``):


.. code-block:: python

    import requests
    url = 'http://stash.compciv.org/2017/test.zip'
    resp = requests.get(url)

    df = open('test.zip', 'wb')
    df.write(resp.content)
    df.close()


After the file has been written to disk, we can use ``unpack_archive``

.. code-block:: python

    from shutil import unpack_archive
    unpack_archive('test.zip')















