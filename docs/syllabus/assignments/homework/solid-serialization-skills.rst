**************************
Solid Serialization Skills
**************************


Rubric
======

Points: 100

Bonus: 20

Due date: 2017-02-16




The assignments
---------------

First, read this guide and make sure you can complete it as if it were a pop quiz in class:

:doc:`/guide/exercises/python/hello-data-serialization`

Then, these assignments (more to come by Friday)

.. toctree::
    :maxdepth: 1

    /syllabus/assignments/homework/serials/usa-gov-analytics
    /syllabus/assignments/homework/serials/chicago-homicides
    /syllabus/assignments/homework/serials/spotify-beyonce-relations
    /syllabus/assignments/homework/serials/just-trump-tweets-csv
    /syllabus/assignments/homework/serials/multiple-user-tweets-csv
    /syllabus/assignments/homework/serials/trump-tweets-json


Requirements
------------

For each of these assignments, write the answers to their prompts in the specified script name. Attach this script to an email attachment to me at dun@stanford.edu as before.

Use this subject line:

``compciv-2017::your_sunet_id::solid-serialization-skills``


Instead of each assignment/problem being worth x number of points, I'm just going to dock you for programs that don't work, or for breaking these few rules:


- Every script should have a downloading-helper function that concerns itself with downloading the data onto some specific place on your hard drive. Each ``foo()`` function can call that helper. Some of the data files are large -- if your scripts/functions constantly re-download the data upon each run, not only are you sucking up my bandwidth, but your adding considerable latency to your own programming, which is only going to make programming feel worse for you. (keep on reading this page to see an example of writing a downloading-helper function)
- Every assigntment lists the expected results. Writing your functions to just output the literal answer that was given to you is not the way to pass this assignment.





Projected datasets:

- Donald Trump's tweets as CSV: http://stash.compciv.org/2017/realdonaldtrump-tweets.csv
- Donald Trump's tweets as JSON: http://stash.compciv.org/2017/realdonaldtrump-tweets.json
- Arists most related to Beyonce, according to Spotify: http://stash.compciv.org/2017/spotify-beyonce-related-artists.json
- Homicides in Chicago since 2001 (CSV): http://stash.compciv.org/2017/chicago-homicides.csv
- Ethnic breakdown of popular U.S. last names, according to the Census (XLSX): http://stash.compciv.org/2017/census-2000-last-names.xlsx


Motivation
==========




This assignment has (or is supposed to have) multiple assignments. Each assignment focuses on one real-world dataset and asks you to read, deserialize, transform, sort, filter, and aggregate the data in the ways that you might be accustomed to with a spreadsheet or a database.


The main point of this assignment is to reinforce the idea of data just being text, and how text is just noise until we can deserialize it into an object, such as a **list** or ** dictionary**, that we can loop through with our data tnrasformation/filtering functions.


I know you're deadly bored with text by now -- but dealing with text, and more importantly, knowing how to program well enough to feel our way from text to data structure -- is the hard part of making bots, visualizations, and web applications, which are going to be our projects in the latter half of this quarter.

Once you've mastered the deserialization and transformation of Trump's tweets as cached JSON file, the only thing stopping you from creating a bot that tracks his tweets is just reading up on the hoops you need to jump through to be part of Twitter's Developer API. After that, it's nothing more than a simple function to get whatever Twitter data you need as JSON.

And the hard work of filtering/transforming that text-as-data is all in these exercises.



How to do the assignments
=========================

This assignment isn't much different than what we've worked on before, and is significantly simpler than the previous web-scraping attempts.

All the datasets are cached and mirrored on my servers, and thus their contents are predictable.


Foo everything
--------------

For each prompt in an assignment, write a function that does what the prompt asks for. For example, if the first prompt expects the return value to be the length of the string "Hello world!", then here is your ``foo_1`` function:


.. code-block:: python

    def foo_1():
        return len('Hello world!')


How to interactively foo
------------------------

Pretend your homework script is named ``test_foo.py`` and contains the above ``foo_1`` function. How do you run ``foo_1`` just to double check that it does what you hoped?

Open up an ``ipython`` session in the **same directory** that contains ``test_foo.py``.

The ``test_foo.py`` script will be treated as a *module*, which means you can ``import`` it:

.. code-block:: python

    import test_foo


The functions that you've defined in ``test_foo.py`` are now accessible via the ``test_foo`` module object:


.. code-block:: python

    >>> import test_foo
    >>> test_foo.foo_1()
    12


I recommend writing and executing each line of code in the interactive shell before stuffing it into a function. But, if you're tired of copying/pasting chunks of code from your editor to ipython, you might like wrapping things up in a function and invoking the function from your script-as-a-module.





Checking the assertions
-----------------------


For each assignment, I provide a list of assertion expressions that, when false, will throw an error. This is just a way to give you an automated check of what I expect from your functions. To use the assertions, just paste the code that I've provided for a given assignment into your script. When you execute the script from the command line, ``foo_assertions()`` will run and happily tell you what doesn't seem to be working.


This is what your script could look like:


.. code-block:: python

    def foo_1():
        return len('Hello world!')



    def foo_assertions():
        assert 1 == 1, 'just for fun'
        assert foo_1() == 12


    if __name__ == '__main__':
        foo_assertions()




Practicing downloads-and-saves
------------------------------

I don't care how sick you are of the ``requests`` library, or of all the steps needed to read/write a file. Not only is it not difficult to whip up a download-and-save function, it's just good practice. And more valuable than it seems when you try to figure out how to save files, and communicate to other parts of your script where a stashed datafile exists.


Let's run through the different ways we could write a downloading-helper function, using the CSV version of this warmup exercise: :doc:`/guide/exercises/python/hello-data-serialization`


The data URL is going to be a constant:

http://stash.compciv.org/2017/helloworld.csv

And, since it's only one file, we can think of the local filename for the data as being a constant.


Here's a fetching function that checks to see if ``helloworld.csv`` exists locally, and if not, downloads from the given data URL and then saves the contents to ``helloworld.csv``. All other functions in the script just assume the constant DATA_FNAME points to that path:


.. code-block:: python

    import requests
    from os.path import exists

    DATA_URL= 'http://stash.compciv.org/2017/helloworld.csv'
    DATA_FNAME = 'helloworld.csv'

    def fetch_data():
        if not exists(DATA_FNAME):
            resp = requests.get(DATA_URL)
            f = open(DATA_FNAME, 'w')
            f.write(resp.text)
            f.close()


Keeping things organized
^^^^^^^^^^^^^^^^^^^^^^^^

As written, ``fetch_data`` dumps the downloaded file into the same folder in which the main script itself exists, and who knows what else. For some situations, we might get to a point where we're downloading so many files that it can cause real harm to mix up downloaded files in the same space as your working code.

The easiest fix is to save data files and other external additions to some kind of subdirectory.

As with everything in programming, there are an infinite number of ways to accomplish this task, so here's some relevant reading:

- How to create a directory idempotently with makedirs(): http://www.compciv.org/practicum/shakefiles/a-creating-a-directory-idempotently/
- Documentation for built-in ``os.makedirs()`` method: https://docs.python.org/3/library/os.html#os.makedirs
- Using Python 3's pathlib module for common file operations http://blog.danwin.com/using-python-3-pathlib-for-managing-filenames-and-directories/
- Documentation for built-in ``os.path.join()`` method



My recommendations:

Call ``os.makedirs()`` with its ``exist_ok`` argument set to ``True``. This allows you to call ``makedirs('some/path')`` without checking to see if it already exists -- if it does, then nothing happens. This is a bit more convenient that ``makedirs()`` causing your entire program to crash when otherwise trying to create a directory that already exists:


.. code-block:: python

    >>> import os
    >>> os.makedirs('somedir')
    >>> os.makedirs('somedir')
    FileExistsError: [Errno 17] File exists: 'somedir'
    >>> os.makedirs('somedir', exist_ok=True)



Use ``os.path.join()`` to create a path out of strings for each subdirectories:


.. code-block:: python

    >>> import os
    >>> os.path.join('/tmp', 'hey', 'you')
    '/tmp/hey/you'


Why not just handle things yourself using the ``str`` object's ``join()`` method?


For starters, ``os.path.join()`` is attuned to the current operating system. Just because you created your script on a machine that recognizes ``/tmp/hey/you`` as a proper path doesn't mean that your script will always run on such machines.


More importantly, ``os.path.join()`` knows the actual rules of joining path segments, including how to deal with redundant or missing separators, or absolute segments:

.. code-block:: python

    >>> import os
    >>> os.path.join('/tmp', '/dog.html')
    'dog.html'
    >>> '/'.join(['/tmp', '/dog.html'])
    '/tmp//dog.html'



Here's a download-this-URL-and-save function that stows the given file into a subdirectory:



.. code-block:: python

    import requests
    from os import makedirs
    from os.path import exists, join

    DATA_URL= 'http://stash.compciv.org/2017/helloworld.csv'
    DIR_NAME = 'tempdata'
    DATA_FNAME = join(DIR_NAME, 'helloworld.csv')

    def fetch_data():
        if not exists(DATA_FNAME):
            resp = requests.get(DATA_URL)
            makedirs(DIR_NAME, exist_ok=True)
            f = open(DATA_FNAME, 'w')
            f.write(resp.text)
            f.close()



Going Pythonic
^^^^^^^^^^^^^^

As you get better at Python and programming, feel free to ignore my verbose-style-for-novices and doing things the "Pythonic" way. This is often not just a style thing, but good practices when it comes to functionality and consistency.


Using the ``with`` block to open/close files
""""""""""""""""""""""""""""""""""""""""""""

This is a pattern that confused me at first but now it's one that I use all the time, except for writing code examples for novices. But it's not hard to master and it immediately provides a visual benefit.


This is what you might have been doing to read from a file:


.. code-block:: python

    xfname = 'somedata.txt'
    xfile = open(xfname, 'r')
    print(xfile.read())
    xfile.close()


Here's the equivalent using ``with`` and ``as``:


.. code-block:: python

    xfname = 'somedata.txt'
    with open(xfname, 'r') as xfile:
        print(xfile.read())


Try adding it to the ``fetch_data()`` method:


.. code-block:: python

    import requests
    from os import makedirs
    from os.path import exists, join

    DATA_URL= 'http://stash.compciv.org/2017/helloworld.csv'
    DIR_NAME = 'tempdata'
    DATA_FNAME = join(DIR_NAME, 'helloworld.csv')

    def fetch_data():
        if not exists(DATA_FNAME):
            resp = requests.get(DATA_URL)
            makedirs(DIR_NAME, exist_ok=True)
            with open(DATA_FNAME, 'w') as f:
                f.write(resp.text)



Avoid unnecessary nesting
^^^^^^^^^^^^^^^^^^^^^^^^^

``fetch_data()`` is a small enough function, but because of the way the conditional branch has been phrased, that short function has 3 levels of indentation. When you get to the bottom, it's hard to know what the function did:


.. code-block:: python

    def fetch_data():
        if not exists(DATA_FNAME):
            resp = requests.get(DATA_URL)
            makedirs(DIR_NAME, exist_ok=True)
            with open(DATA_FNAME, 'w') as f:
                f.write(resp.text)


Here's a variation that brings balance by adding an ``else`` clause, but without changing the logic or flow:

.. code-block:: python

    def fetch_data():
        if exists(DATA_FNAME):
            pass
        else:
            resp = requests.get(DATA_URL)
            makedirs(DIR_NAME, exist_ok=True)
            with open(DATA_FNAME, 'w') as f:
                f.write(resp.text)






Read PEP 8 -- Style Guide for Python Code for ideas and inspiration: https://www.python.org/dev/peps/pep-0008/
