***********************
Happy Birthday Congress
***********************

Write a program that reads from a list of U.S. members of Congress. For those whose birthdays are today, your program should print out a Happy Birthday message to the lucky legislator, along with their full name, title, state, and age.

Sample output for January 31, 2017 (2017-01-31):


.. code-block:: text

    Today is 2017-01-31

    Happy Birthday to Democratic Representative Gwen Graham from FL. You are 54 years old!
    Happy Birthday to Republican Representative Garret Graves from LA. You are 45 years old!
    Happy Birthday to Republican Representative Bill Huizenga from MI. You are 48 years old!
    Happy Birthday to Democratic Representative C. Ruppersberger from MD. You are 71 years old!



Partly inspired by one of the `IFTTT applets from ProPublica <https://www.propublica.org/nerds/item/propublicas-on-ifttt>`_, this is meant as an introductory exercise showing how a dataset can be used to programmatically disseminate information. Usually we think of this in terms of creating visualizations from datasets. But this is an exercise in using programming to quickly filter a dataset to find a story that you could confirm manually, if you had infinite time.

The "story" here isn't that interesting, but it's a trivial step to go from making a dynamically generated text message to a useful news application, like `ProPublica's Represent <https://projects.propublica.org/represent/>`_ and `SOPA Opera <https://projects.propublica.org/sopa/>`_, and 538's `Tracking Congress in the Age of Trump <https://projects.fivethirtyeight.com/congress-trump-score/>`_.



Rubric
======

Due date:
    1:00 PM, 2017-02-02


.. csv-table::
    :header: "Points", "Metric"
    :widths: 10, 90

    1,"Having a correct subject headline of ``compciv-2017::your_sunet_id::happy-birthday-congress``"
    1,"Your email contains an attached script named ``birthday.py``"
    2,"Your script downloads the list of legislators only when necessary"
    1,"Your script filters for legislators that were 'in_office' when the data file was created"
    2,"Your script accurately filters for legislators who have a birthday on a given date"
    2,"Your script prints out a message that accurately labels the birthday-boy/girl"


Requirements
------------

The data file that you will use can be downloaded here:

http://stash.compciv.org/2017/114th-congressmembers.csv

Note that it is not the latest Congress, but that's fine, you can grab an updated file later for real-world work.


- Your program should download the remote datafile and save it somewhere on your hard drive
- Your program should not re-download the remote datafile if you already have a local copy
- Use the ``csv`` library to read the file. Filter out all rows in which the ``in_office`` attribute is *not* ``'1'``, nor the ``title`` is not either ``'Sen'`` or ``'Rep'``.
- Your program should be able to figure out the current date upon launch.



Walkthrough
===========

Program design tips
-------------------

This is a seemingly trivial exercise, but one that has a lot of outsize frustration because of how seemingly trite the output is. Don't worry about this program's lack of impact, focus on these things:


- Break the problem down to many small steps
- Be able to do each small step in the interactive shell before you start writing your program
- Be able to organize your code into functions
- Use variables to represent values (such as filenames) that are re-used and are prone to typos
- Know what it means to deserialize a text file into data objects
- Know how to format a string


To give you a strong helping hand, I'm going to dictate what your program should look like. If you think you know what you're doing, you can go ahead and skip this.


Basic skeleton
^^^^^^^^^^^^^^

Open up your text editor and create ``birthday.py``.


This is what the initial skeleton of your program should look like:


.. code-block:: python


    def main():
        print("Hello world")


    main()



Put that code in, save it, run ``birthday.py`` from the command-line, and make sure 'Hello world' is printed to the screen.


The ``main()`` function defintion contains the logic for doing all the work. That call to ``main()`` should be the last line of your script. It makes it so that your ``main()`` function is executed when ``birthday.py`` is run, even if all it does is say ``'Hello world'``.


Adding functions and constants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

So how do we do interesting things from this shell? Start adding functions that describe the things that you know you'll have to do. For example, you'll have to download the data file and save it to your local disk. I recommend calling that function ``bootstrap_data()``. You can call it from inside ``main()``.


I also include two constants: the URL where the data file exists, and the file path at which that data file will be saved to on your hard drive:


.. code-block:: python

    DATA_URL = 'http://stash.compciv.org/2017/114th-congressmembers.csv'
    DATA_FILENAME = '114th-congressmembers.csv'


    def bootstrap_data():
        print("Boostrapping the data")

    def main():
        print("Hello world")


    main()



A suggested roadmap of functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There's no one right way to approach this. But if you're new to programming, you may not have practice or confidience in breaking down a big problem into small problems. Below I've included a script full of functions that can be written one at a time so that you aren't overwhelmed. But it's not just about being overwhelmed, it makes it easier to organize your work, and reduce hard-to-track bugs.



.. code-block:: python


    DATA_URL = 'http://stash.compciv.org/2017/114th-congressmembers.csv'
    DATA_FILENAME = '114th-congressmembers.csv'


    def bootstrap_data():
        """
        Makes sure the essential data file is downloaded and saved to my local drive
        """


    def get_full_name_and_title(firstname, last_name, title):
        """
        first_name and last_name are strings
        title is a string like 'Sen' or 'Rep'

        returns a string like: `Senator Chuck Grassley`
        """
        firstname = 'Chuck'
        lastname = 'Grassley'
        fulltitle = 'Senator'
        fname = ' '.join(fulltitle, firstname, lastname)

        return fname

    def get_party_name(party_initial):
        """
        party_initial is some string like 'R' or 'D'

        returns a string representing the full name of the party based on the initial, e.g.
         'Democratic' for 'D'. If neither 'R' nor 'D', returns 'Independent0'
        """

        partyname = 'Independent'
        return partyname



    def get_legislators():
        """
        returns a list of dicts, with each dict representing a legislator who is in office
        and either a 'Sen' or 'Rep' in their title
        """

        legislators = []
        return legislators



    def make_birthday_message(firstname, lastname, title, age,  state, party):
        """
        Constructs a happy birthday message, including the person's name and age and title, etc.

        Returns the message as a string:

        'Happy Birthday to Republican Representative Bill Huizenga from MI. You are 48 years old!'
        """


        msg_template = 'Happy Birthday to {party} {allname} from {state}. You are {age} years old!'

        fname = get_full_name_and_title(firstname, lastname, title)
        pname = get_party_name(party)

        return msg_template.format(party=pname, allname=fname, state=state, age=age)



    def today_date_string():
        """
        Returns today's date as a string in 'YYYY-MM-DD' format, e.g. '2017-01-30'
        """

        return '2017-01-30'



    def was_born_on_this_day(birthdate, thisdate):
        """
        birthdate and thisdate are date strings in 'YYYY-MM-DD' format

        if today is the birthday for birthdate, returns an integer representing the age of
           the birthday person
        else, returns False
        """






Interactive exploration
-----------------------

OK, now that we have a good idea of the things that we need to do, we need to make sure we can do each step in isolation. This includes downloading and saving a file, parsing CSV-formatted data, finding out today's date, and figuring out if someon's birthday is today.


So pop into your command-line and run ``ipython`` to follow along.


What is today's date
^^^^^^^^^^^^^^^^^^^^

Let's start with a seemingly easy problem: what is today?

In reality, figuring out time functions, not just in Python, but in most modern languages, can easily drive you crazy. Let me just walk you through the exact steps to save you a lot of pain.

First, let's remind ourselves what we need to end up with. It's not just *today's* date we care about. But we want today's date in a specific format: as a string: 'YYYY-MM-DD', e.g. '2017-02-01'.

OK, makes sense to find whatever Python function generates today's date, no mater what the data type is. We find the answer in the `standard library's ``datetime`` package <https://docs.python.org/3/library/datetime.html>`_.

You can explore in the interactive shell by importing ``datetime``, and then typing ``datetime.``, then the Tab key, to get a list of the packages methods and modules:

.. code-block:: python

    >>> import datetime
    >>> datetime.


Confusingly enough, the datetime package has a class named ``datetime``, and that ``datetime`` class has a method named ``now()``, which is what we want. Remember, in ``ipython``, you can run the ``help()`` function and pass in module/package/class names to see the documentation if you don't want to switch out of Terminal:



.. code-block:: python

    >>> import datetime
    >>> help(datetime.datetime.now)


Running the ``now()`` function returns a data type that is not a simple nubmer or string:

.. code-block:: python


    >>> import datetime
    >>> todaysdate = datetime.datetime.now()
    >>> type(todaysdate)
    datetime.datetime
    >>> todaysdate
    datetime.datetime(2017, 1, 30, 20, 59, 30, 253386)


OK, we need to convert that datetime.datetime object into a string. Go ahead and read the `official documentation for datetime.datetime objects <https://docs.python.org/3/library/datetime.html#datetime-objects>`_. But in this situation, and many others, we want to use the ``strftime()`` method.

``strftime()``, which I read to myself as *"string from time"* is well-known function that appears in many programming languages. This variation takes a string argument. That string is how we specify the *format* of the datetime. Unfortunately, this requires learning a meta-language -- there are even sites dedicated to explaining the syntax: http://strftime.org/


Long story short, the string that expresses the ``'YYYY-MM-DD'`` format that we want is, in strftime syntax:

``'%Y-%m-%d'``


Try it out in the interactive shell:


.. code-block:: python


    >>> todaysdate
    datetime.datetime(2017, 1, 30, 20, 59, 30, 253386)
    >>> todaysdate.strftime('%Y-%m-%d')
    '2017-01-30'


Looks like we got what we need to fill out the ``todays_date_string()`` function that we defined earlier. In the snippet below, I'll include the ``import`` statement, though the imports should be at the top of the script.


.. code-block:: python

    import datetime

    def todays_date_string():
        """
        Returns today's date as a string in 'YYYY-MM-DD' format, e.g. '2017-01-30'
        """
        t = datetime.datetime.now()
        s = t.strftime('%Y-%m-%d')
        return s



Obviously that function could be a one-liner. But paste it into your shell and try it out:


.. code-block:: python

    >>> todays_date_string()
    '2017-01-30'



Is it really your birthday?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

OK, let's move on to an algorithm: how do we know if it is someone's birthday? Other than them telling us, *"Hey, today is my birthday?"*

Well, we can start with figuring out what *today* is, which we have thanks to the ``todays_date_string()`` function.


As it turns out, `114th-congressmembers.csv data file <http://stash.compciv.org/2017/114th-congressmembers.csv>`_ contains a ``birthdate`` column, and the values are in ``YYYY-MM-DD`` format.

So in the interactive shell, set a ``today`` variable to some arbitrary datestrings, and then think of 3 more arbitrary datestrings in which:

- the date string is obviously the same day as ``today``, and is thus a "birthday"
- the date string is obviously not the same day, nor a "birthday" when compared to ``today``
- the date string is not ``today``, but it counts as a "birthday"


.. code-block:: python

    >>> today = '2015-12-25'
    >>> a = '1999-03-08'
    >>> b = '2015-12-25'
    >>> c = '1967-12-25'
    >>> today == a
    False
    >>> today == b
    True
    >>> today == c
    False


    So ``b`` represents a date value in which the birthdate *is* today. That's not a situation that we care about, but it's not a situation that should make our logic more complicated.

    ``c`` is the comparison we care about. It's not equal to ``today``, but it is a *birthday*. What makes it a birthday? That the ``MM-DD`` components of the strings are matching, e.g. ``'12-25'``


    So there's several ways to make a test for birthday. One would be just to compare the last 5 characters of ``today`` and the given date:


    >>> todaymd = today[-5:]
    >>> todaymd
    '12-25'
    >>> todaymd == a[-5:]
    False
    >>> todaymd == b[-5:]
    True
    >>> todaymd == c[-5:]
    True


    Looks like we have a birthday test. Let's add this to the ``was_born_on_this_day()`` function:




    .. code-block:: python

        def was_born_on_this_day(birthdate, thisdate):
            """
            birthdate and thisdate are date strings in 'YYYY-MM-DD' format

            if today is the birthday for birthdate, returns an integer representing the age of
               the birthday person
            else, returns False
            """

            if birthdate[-5:] == thisdate[-5:]:
                return True
            else:
                return False



    This function needs to do one more thing. In the event that it is someone's birthday, the value returned should be the birthday person's age on ``thisdate``.


    That's easy enough: just subtract the year value from ``birthdate`` from ``thisdate``. Remember to convert the year string values into integers before doing that:


    .. code-block:: python

        def was_born_on_this_day(birthdate, thisdate):
            if birthdate[-5:] == thisdate[-5:]:
                y1 = thisdate[0:4]
                y0 = birthdate[0:4]
                return int(y1) - int(y0)

            else:
                return False




    Paste the function definition into your interactive shell, then try it out:

    .. code-block:: python

        >>> today = '2017-01-12'
        >>> was_born_on_this_day('1999-12-01', today)
        False
        >>> was_born_on_this_day('1999-01-12', today)
        18
        >>> was_born_on_this_day(today, today)
        18




Downloading the data
^^^^^^^^^^^^^^^^^^^^

OK, let's get to some more concrete work: the actual downloading of the data and saving to some place on our hard drive.


I regret not having a more complete ``requests`` guide, but this will do for what we need, which is to download a text file:


`Downloading files with the Requests library <http://www.compciv.org/guides/python/how-tos/downloading-files-with-requests/>`_


Applying it to our own situation, but doing it from the interactive shell:

.. code-block:: python

    >>> import requests
    >>> url = 'http://stash.compciv.org/2017/114th-congressmembers.csv'
    >>> resp = requests.get(url)

Now's the time to make sure you know what's going on with ``requests`` library and the objects that it creates, including remembering that the URL is just a string, and that we have to use the response's ``text`` attribute to refer to the downloaded data:


.. code-block:: python

    >>> type(url)
    str
    >>> type(resp)
    requests.models.Response
    >>> resp.status_code
    200
    >>> type(resp.status_code)
    int
    >>> txt = resp.text
    >>> type(txt)
    str
    >>> txt[0:50]
    'title,firstname,middlename,lastname,name_suffix,ni'
    >>> len(txt)
    269070
    >>> lines = txt.splitlines()
    >>> type(lines)
    list
    >>> len(lines)
    899


Saving the data to a local file path
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The data contained in the ``txt`` variable is CSV-formatted plaintext data, but it's impossible to read in our current state. No matter, all we care about is saving it to our own local drive, which means we can open it in Excel if we wish:


.. code-block:: python

    >>> destname = '114th-congressmembers.csv'
    >>> destfile = open(destname, 'w')
    >>> destfile.write(txt)
    >>> destfile.close()


I leave it to you to interactively inspect each of those commands. But whereever you are running your ``ipython`` shell, you should see a file named ``114th-congressmembers.csv``

The work of reading and writing files can seem pretty bizarre even to programmers. Here's a quick reference guide, I'll try to put together a more complete cheatsheet later:

`Opening files and writing to files <http://www.compciv.org/guides/python/fileio/open-and-write-files/>`_



Downloading the remote file only if the local file doesn't already exist
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OK, we're heading into a world of hurt involving the two hard problems in computer science of naming things and cache invalidation. But we'll pretend the world is simple right now:

It takes time to download that data file. The data in it, for our purposes, isn't going to change. So why spend precious seconds waiting for it to download, breaking our flow of development? Nevermind the additional errors that come when the Internet is down.

This is where the **if-conditional** expressions come in. We also need the help of the ``os.path`` standard library, which includes a method named ``exists()`` that returns True if a file exists at a given filename path. Try it out for yourself:



.. code-block:: python

    >>> from os.path import exists
    >>> exists('114th-congressmembers.csv')
    True
    >>> exists('aklsdfjaklsdfjaklsdfjadsklfj334')
    False



Here's how to check before downloading a file if the file already exists. Throw it in a script and run it from the command-line:

.. code-block:: python

    from os.path import exists
    import requests

    url = 'http://www.example.com'
    destname = "example.html"


    if exists(destname):
        print("Already downloaded", destname)
    else:
        resp = requests.get(url)
        with open(destname, 'w') as f:
            f.write(resp.text)
            print("Downloaded from", url, "saved to", destname)



The first time you run it, you should see something like this:

.. code-block:: shell

    $ python examplefoo.py
    Downloaded from http://www.example.com saved to example.html

Each subsequent execution should result in nothing new being downloaded:


.. code-block:: shell

    $ python examplefoo.py
    Already downloaded example.html




Creating the bootstrap_data function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We know enough to create the ``bootstrap_data()`` function that takes care of the mundane details of whether or not a data file has been downloaded to the proper location.

There's different ways to style this, but you should have an if-conditional expression, and you should probably use the constants for the ``DATA_URL`` and ``DATA_FILENAME``:



.. code-block:: python


    def bootstrap_data():
        # download the data if it isn't already downloaded
        if exists(DATA_FILENAME):
            print("Skipping download;", DATA_FILENAME, 'already exists')
        else:
            print("Downloading", DATA_URL)
            resp = requests.get(DATA_URL)
            df = open(DATA_FILENAME, 'w')
            df.write(resp.text)
            df.close()
            print("Wrote data to:", DATA_FILENAME)


    In my version, I don't return anything in the function: that's OK, a function doesn't have to return something if it has an effect.



Main intermission
^^^^^^^^^^^^^^^^^

Edit your ``main()`` function. Add a call to ``bootstrap_data()`` so that it runs when you run ``birthday.py``.

Also, add a ``print()`` call that prints out a friendly message with today's date.

Here's what your ``main()`` function could look like:


.. code-block:: python

    def main():
        bootstrap_data()
        today = todays_date_string()
        print("Hello, today's date is:", today)




Converting CSV text data into data about legislators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Read the guide: :doc:`/guide/topics/python-standard-library/csv`

The ``get_legislators()`` method is where you can put in the work of opening the CSV text file, processing it with ``csv.DictReader``, and then filtering it for only the rows that we want.

Here's code that will open the downloaded CSV file, create a list of its data, filter that list for only legislators who are in office, and then returns the filtered list to be used elsewhere. You'll have to modify it so that only rows in which ``title`` is ``'Sen'`` or ``'Rep'`` are allowed:



.. code-block:: python


    def get_legislators():
        """
        returns a list of dicts, with each dict representing a legislator who is in office
        and either a 'Sen' or 'Rep' in their title
        """

        df = open(DATA_FILENAME, 'r')
        rows = list(csv.DictReader(df))
        df.close()

        # trim all non-in-office members
        legislators = []
        for r in rows:
            if r['in_office'] == '1':
                legislators.append(r)


        return legislators



If things are going well, you should be very close to this in your ``main()`` function:


.. code-block:: python


    def main():
        bootstrap_data()
        legislators = get_legislators()
        todaystr = todays_date_string()

        for x in legislators:
            age = was_born_on_this_day(x['birthdate'], todaystr)
            if age:
                print("We have a birthday for", x['firstname'], x['lastname'])






Party making
^^^^^^^^^^^^

Part of the requirements is to print a message that includes the party of the birthday person. The dataset, however, only includes initials, i.e. ``R`` instead of ``Republican``.


Easy enough to fix. Use conditional expressions to pick the right label:


.. code-block:: python

    if party_initial == 'R':
        party_name = 'Republican'
    elif party_initial == 'D':
        party_name = 'Democrat'
    else:
        party_name = 'Independent'




It's hard to interactively test out conditional constructs, so wrap it in a function:



.. code-block:: python

    def get_party_name(party_initial):
        if party_initial == 'R':
            party_name = 'Republican'
        elif party_initial == 'D':
            party_name = 'Democrat'
        else:
            party_name = 'Independent'
        return party_name


Interactively testing it:

.. code-block:: python

    >>> get_party_name('R')
    'Republican'
    >>> get_party_name('D')
    'Democrat'
    >>> get_party_name('X')
    'Independent'



Making a birthday message
^^^^^^^^^^^^^^^^^^^^^^^^^

This is just more string-building. Start off with a template string in which placeholder variable names are wrapped in curly-braces:


.. code-block:: python

    msg_template = 'Happy Birthday to {party} {allname} from {state}. You are {age} years old!'


To fill in the placeholders, use the string object's ``format()`` method to pass arguments:


.. code-block:: python

    >>> msg = msg_template.format(party='Whatever',
                              allname='Master of the Universe Al Roker',
                              state='Somewhere',
                              age='99')

    >>> msg
    'Happy Birthday to Whatever Master of the Universe Al Roker from Somewhere. You are 99 years old!'


You can read more about Python's various string formatting methods here:

- Format examples: https://docs.python.org/3/library/string.html#format-examples
- Parametrized formats: https://pyformat.info/#param_align
