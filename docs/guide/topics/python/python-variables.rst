*******************
Variables in Python
*******************

**Variables** are human-readable labels that we assign to data objects inside our programs. Variables are such a simple, fundamental feature of programming that most "Intro to Programming" courses cover them in the first 5 minutes you're expected to just recognize and use them.

I can't argue against how variables *seem* simple. Here's the minimum you need to know; how to assign a value to a variable:

.. code-block:: python

    my_variable = 1024

The variable is on the **left** side. On the **right** that we want to represent with the label ``my_variable``. And that **single equals sign** is Python's operator for assigning values to variables.


Quick principles for naming variables
=====================================

If you already know how to program in another language, you can probably get by with reading the `PEP 8 Python Style Guide's section on Naming Conventions <https://www.python.org/dev/peps/pep-0008/#naming-conventions>`_

If you're new to programming, read the "Suggested readings" section that immediately follows this section.  Read the rest of my rambling and examples. Make sure you can answer the "pretend quiz questions" at the end of this section.

And then novice or expert, you can consider my recommendations for naming files; rather than remember all the rules for **invalid** variable names, just stick to the basic good patterns for names (basically, letters and underscore characters)


.. rubric:: Use lowercase letters for most variable names

Virtually everything you need to express in a filename can be done with lowercase letters and underscore characters.

Avoid numbers whenever possible because they are easily misread (lowercase-``L`` vs ``1``) and they can add unintentional meaning to a variable name.

Don't mix uppercase with lowercase.


.. code-block:: python

    # Good
    url = 'http://www.example.com'
    latlng = (37.92923, -117.23123)
    numx = 99
    numy = 7

    # No
    Url = 'http://www.example.com'
    latLng = (37.92923, -117.23123)
    num1 = 99
    num2 = 7



.. rubric:: Use snakecase


For variable names consisting of compound words, use an underscore character, ``_``, to separate the words for easier readability:


.. code-block:: python

    # Good
    dest_filename = 'file.txt'
    index_page_url = 'http://www.example.com/index.html'

    # Meh
    destfilename = 'file.txt'
    indexpageurl = 'http://www.example.com/index.html'


.. rubric:: Use all-uppercase and underscore for constants

A *constant value* in a program is something that is not meant to change during the entire execution of the program. For example, if your program is always going to save files into the path ``/tmp/stuff``, assign that value to a variable name in all-uppercase so that it is obvious that that variable contains a special value.


.. code-block:: python

    DEST_PATH = '/tmp/stuff'



However, it is important to note that just because you want something to be a constant and that you've all-uppercased the variable name, that this is just a *visual* convention. It doesn't prevent this from happening:

.. code-block:: python

    DEST_PATH = '/tmp/stuff'
    # (later down in the program)

    DEST_PATH = 'blahblahblah'


For the purposes of this class, the above scenario shouldn't be something to worry about. Most of our scripts will be short and compact, and when you're writing your own code you aren't typically going to do something so deliberately confusing.


.. rubric:: Length of name depends on "distance"

Variable names are meant to be descriptive, but if they're too long, they create a lot of visual noise that makes a program hard to understand:


.. code-block:: python
    import requests

    the_url_of_the_web_file_that_must_be_downloaded = 'http://www.example.com'
    the_server_response = requests.get(the_url_of_the_web_file_that_must_be_downloaded)
    print(the_server_response.text)


Look how much clearer the code is when the variable names aren't completely dominating your cognitive space:

.. code-block:: python

    import requests
    url = 'http://www.example.com'
    response = requests.get(url)
    print(response.text)


But why not go completely minimalist?

.. code-block:: python

    import requests
    u = 'http://www.example.com'
    r = requests.get(u)
    print(r.text)


The above snippet with one-letter variables isn't too difficult to read, but only because this program is so short and all the functionality is wrapped up in those few lines. It becomes a much bigger problem if the ``r`` variable is used 20 lines later, and you have no idea what it has without re-reading the beginning of the program.

Generally, the longer a variable's "lifetime" in your program -- i.e. if it appears at the beginning and keeps being used far down into the script -- the longer the variable's name should be.

For variables with a very short lifespan, such as within a loop, it's OK to use a one-letter variable, with the expectation that it'll be re-used and overwritten later in the program.


Suggested reading
=================



If you are new to programming in general, please read this entire section and manually work out every example. There's not much code, but it's important to have the concept as grounded in to your head as much as the answer to ``1 + 1``.









Naming things is a hard problem in computer science and life
============================================================

Because variables are used to *name* things in our program, using them automatically puts us in the hard territory of that hard problem in computer science: naming things. As I've mentioned before, the vast majority of errors I see in this class, even from students who have taken a couple quarters of Stanford CS, are errors that came from how something was named. Usually its students blindly copying my examples, not realizing that the example is a "quickie" script where you have to fill in things that apply to you.

And then there are the bugs that come from being sloppy and lazy in naming things. **Do not be lazy**:

1. You will spend far more time reading your code than writing it.
2. If you know what a variable should be named, it means you know what role it has in your program, because you actually know what your program will do.


It's important to keep realizing that **you have agency**. If you see a sample program of mine in which I apparently couldn't be bothered to spell out names properly, I don't care if you copy the program. But you *must* prove to yourself that it works.

Here's a program that downloads a cat photo from a URL and makes it black and white. If none of the code looks familiar to you, that's OK, because I found it on this StackOverflow question:

`Convert RGB to black OR white
<http://stackoverflow.com/questions/18777873/convert-rgb-to-black-or-white>`_


Here's a code snippet posted as an answer; you can guess from the topic that it has something to do with turning images from color into black and white:

.. code-block:: python

    from PIL import Image

    col = Image.open("cat-tied-icon.png")
    gray = col.convert('L')
    bw = gray.point(lambda x: 0 if x<128 else 255, '1')
    bw.save("result_bw.png")


I'm as clueless as you, but I retyped this code by hand. Notice how I took the value for `"cat-tied-icon.png"`and assigned it to a variable name that makes sense to *me* (``srcname`` destination for source file name).

Then I set ``srcname`` to a photo file that exists on my computer.

.. code-block:: python

    from PIL import Image

    srcname = '/tmp/obama.jpg'
    destname = '/tmp/obama.bw.jpg'

    img = Image.open(srcname)
    gray_img = img.convert('L')
    bw_img = gray_img.point(lambda x: 0 if x < 128 else 255, '1')
    # finally, save the file
    bw_img.save(destname)







you need to realize two things:

1. Copying the snippet is fine, but change the variable names so that they make sense to you. You are the only person that matters in your own program (well, for this class at least), so **write for yourself**.
2. Have absolute confidence that your naming changes don't result in the program "breaking" because all they were were naming changes.


Even as an experienced programmer, when I'm trying to



This includes the most obvious and pedantic naming error: a typo in a URL or filename. Students who ignore my commandment to reflexively hit the Tab-key to autocomplete a filename will inevitably lose hours of their life not to debugging an intellectually-challenging program, but because of a spelling error.

After you've made a few "The computer can't find the program by the name that you can't correctly spell" errors, you gain greater appreciation why it's important to come up with thought out names







I've mentioned before that there are barely a dozen very simple English words that we have to memorize for Python -- e.g. ``if``, ``for``, ``def``, ``import``, etc -- because they have special and immutable meaning in the Python language.

But even in a simple Python program, there looks to be a whole lot more than just a dozen simple English words:


.. code-block:: python

    import requests

    MSG_TEMPLATE = "The site {x} contains {y} characters"
    BOOKMARKS_URL = 'http://stash.compciv.org/2017/newsmarks.txt'

    xresp = requests.get(BOOKMARKS_URL)
    if xresp.status_code == 200:
        urls = xresp.text.splitlines()
        for url in urls:
            resp = requests.get(url)
            numchars = len(resp.text)
            msg = MSG_TEMPLATE.format(x=url, y=numchars)
            print(msg)





When you understand **variables**,



is not just a required fundamental of programming languages, they are one of the most obvious ways in we can be *expressive* in code.

Another way of putting it: being good at naming things means you'll have a much easier time of creating complex programs. Even if you are the only person to read your own code, you will be spending far more time reading your own code than writing it.






Core concept
============

The ability to assign *names* to a *value* is one of the few fundamental features of every complete programming language.

Here's a simple example of assigning a *name* (``mynum``) to a *value* ``42``:

.. code-block:: python

    mynum = 42


If you want to do something with the value ``42``, you can refer to ``mynum`` in your script:


.. code-block:: python

    mynum = 42
    print(mynum * 5)


This is equivalent to the previous snippet, but assigns the value of ``5`` to the name ``myfactor``:


.. code-block:: python

    mynum = 42
    myfactor = 5
    print(mynum * myfactor)


One question you should immediately ask: What's with all the extra code? If you want to print the result of ``42 * 5``, why use a variable at all? What's the difference between the above snippet and the one-line snippet below?


.. code-block:: python

    print(42 * 5)


The answer is, as with everything programming-related: well, what do you mean by the word *difference*? The snippets are obviously different in a literal sense. The above snippet is just one line, and the previous snippets are 3 and 2, lines, respectively. That's obviously *different*.

But you probably mean: is there a difference in what the 3 snippets *print*? The answer is **no**. They print the same value, which is the product of ``42`` and ``5``, which you learned to calculate in grade school: ``220``


Why pronouns?
-------------

At this point, this guide assumes you don't know about **functions** and **imports** (among many other fundamentals), nevermind how to construct an entire Python program, and that all you know are simple mathematical expressions --  ``2 + 3`` -- and, now, variable assignment ``a = 5``

So to answer the question about why use variables when we can just refer to values directly,contemplate this grammar lesson:


We have to learn about **nouns** and **proper nouns**, such as "apple" and "Alice", and "Alice's apples". So what's the deal with `pronouns <http://www.gocomics.com/calvinandhobbes/1986/02/24>`_? Why use pronouns -- e.g. "it", "her", and "her apples" -- when we can just directly refer to things nouns?


    Alice took Alice's apples out of Alice's lunchbox. Bob asked Alice if Bob could have some apples of Alice's.

    Alice nodded and gave Bob several apples that were in Alice's possession. Bob ate all of the apples as quickly as Bob could because Bob was hungry.

    "How does Bob like those apples of Alice's?" Alice asked Bob.


Going back to the use of variables in programming. Yes, when we have simple standalone expressions, using variables is silly because, well, nothing *varies*:


.. code-block:: python

    x = 1
    y - 2
    z = x + y
    print(z)



One situation where we might use a variable even when the values and results are *constant* is if the value is difficult to represent. Such as the result of dividing ``1`` by ``7``, and then multiplying that result by some other difficult to literally-type-out quantity:

.. code-block:: python

    ratio = 1 / 7
    a = 3
    b = 42.4871
    ratio = -8712.3123 / 7.2361

    print(ratio * a, ratio * b)


But 99% of the time as a programmer, especially in the context of journalism, you will be writing scripts in which *very little* is constant, neither the input nor the output nor real-world circumstances (e.g. Is the Internet currently working? What is the time-zone on the current computer? How fast is the computer moving relative to the speed of light?).





The assignment operator, ``=``
==============================

The **equals** sign is one of the most common operators we'll see in Python, because it is the operator used for assigning a variable names to values:


.. code-block:: python

    myval = 9999



Quick test for whether you will flunk this course HARD
------------------------------------------------------

OK, time for a dramatic flourish.

Given the following snippet:

.. code-block:: python

    x = 9999

Here's how I would describe it in English:

    The variable ``x`` represents the value ``9999``

Or:

    9999 is assigned to the variable ``x``


This is because I studied computer engineering in college, in which I had to learn the C, C++, Java languages. And then I learned PHP, Ruby, and Python as a journ-coder. What do these languages have in common? The **equals sign** is used to do assignment as I have described above.


But what if you're a just a regular product of the American education system, in which you've learned arithmetic, and even taken a year of Algebra?

When you see the following snippet:

.. code-block:: python

    x = 9999


You probably describe it as:

    x is equal to 9999

And even:

    9999 is equal to x


And if the only programming language you've learned so far is SQL, in which a single ``=`` is used in conditional statements, you're going to have an additional cognitive burden:


.. code-block:: sql

    SELECT * from people WHERE first_name = 'Daniel';


After reading `Hadley Wickham's style guide for R <http://adv-r.had.co.nz/Style.html>`_, I seriously considered re-writing this course using the R language because this is how assignment is done in R:


.. code-block:: r

    x <- 9999



OK, all of this is to say that a very common novice mistake is to see this example of variable assignment:


.. code-block:: python

    x = 9999
    y = x



And then assume that the following will work:

.. code-block:: python

    9999 = a
    a = b


It. **Will**. **Not**. If you doubt this, try this in the interactive Python console right now:


.. code-block:: python

    >>> a = 9
    >>> 42 = a


.. code-block:: python

    >>> x = 42
    >>> x - 10 = y
















Variables in practice
=====================

For example, expect to see the following snippet very frequently in our work, at least the work that involves fetching a file from a URL:

.. code-block:: python

    import requests
    url = 'http://www.example.com'
    response = requests.get(url)
    text = response.text

    print(text)


The first 1 line contains 2 new concepts and doesn't have much to do specifically with variables. Just accept these concepts as they are, and you'll see them again very soon:

- ``import`` is one of the very few Python words that are special to Python, i.e. it can never be used as a variable name.

- ``requests`` `is a library <http://docs.python-requests.org/en/master/>`_ that contains functionality for connecting to resources on the Web (i.e. to download a file). Technically, we can give this library a *different* name if we wish, like ``webgetter`` and then use ``requests`` as a name for something else. We could also switch the labels for the aspirin and rat poison bottles in our homes. But we just generally don't, because we don't want to confuse people unnecessarily.


The next 3 lines are variable assignments. It's not important to know what ``requests.get(url)`` does -- only that it is assigned to the variable ``response``.

And this might look confusing:

.. code-block:: python

    text = response.text


But don't worry about what ``response.text`` actually does or *means*. Just stick with the core truth that you know: the variable ``text`` represents whatever ``response.text`` resolves to.

The last line just outputs to screen whatever ``text`` is.


So here's a rundown of all the different ways that snippet can be expressed, depending on what we want to do.


Being less verbose
^^^^^^^^^^^^^^^^^^

I find that using ``response`` as a variable name can be problematic with some beginners, because ``response`` looks like an official programmy-ish word, with special meaning, rather than just an abstract label. And ``response`` is 8 whole characters to type out.

So, you'll often see this in my examples:


.. code-block :: python

    import requests
    url = 'http://www.example.com'
    resp = requests.get(url)
    text = resp.text

    print(resp.text)




Caring only about the raw HTML content from a URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's ignore the details of what ``requests.get(url)`` actually returns. Just trust me that what's assigned to ``resp`` is a "response" from the remote Web server, i.e. the computer serving up the page we find at `http://www.example.com <http://www.example.com>`_

A response from a web server consists of more than just the data/payload/contents at that URL. But again, let's ignore the details. We we do care about is that the object represented by ``resp`` has a ``.text`` attribute, which we assign to ``text``.

Since we don't care about anything else in the ``resp`` object, why not put lines 3 and 4 together like this:

.. code-block :: python

    url = 'http://www.example.com'
    resp = requests.get(url)
    text = resp.text

    print(numchars)
    print(response.text)










Naming style and conventions
============================

As I've said many times before, programming is as subjective as normal writing. That said, the least path of resistance for both novices and experts is to  read PEP 8 (the Style Guide for Python), and adhere to the `naming conventions it proscribes <https://www.python.org/dev/peps/pep-0008/#naming-conventions>`_, until you don't even remember what it was like to think differently.




Naming things is a hard problem
-------------------------------

Remember the






Hypothetical Quiz A
===================

If I were to throw a quiz tomorrow on the basics of variables, these are things I would absolutely expect you to know without referring to notes. In other words, if you can't look at these and *know* the answer, then open up ``ipython`` and *test this code out*.

What is the output of each ``print`` statement?

.. code-block:: python
    >>> x = 9
    >>> y = 7
    >>> print(x + y)


    >>> a = 'b'
    >>> print(a)

    >>> b = a
    >>> a = 'z'
    >>> print(b)


    >>> a = 'world'
    >>> a = 'hello'
    >>> print(a + a)


    >>> b = 42
    >>> a = b
    >>> b = a + b
    print(b)



Why does the following Python expression throw a ``SyntaxError``:

.. code-block:: python

    >>> 3 = a
    File "<stdin>", line 1
    SyntaxError: can't assign to literal


If the following Python script were executed, which line would cause it to throw a ``NameError``?


.. code-block:: python

    import requests
    url = 'http://www.example.com'
    example = Requests.get(url)
    _tx = example.text
    print(example)
    print(_tx)




Both of these Python expressions each throw an error (assume that you start each in a separate interactive prompt):


.. code-block:: python

    >>> 42 = z


.. code-block:: python

    >>> y = 42
    >>> z = y




Which of the following are *not* valid variable names, and why?


(Note that I said "valid", not "good")

.. code-block:: python

    hello
    HELLO
    _h
    2000party
    h3ll0
    camelCase
    __snake_case__
    th!ng
    x
    X
    'y'
    DONALD_TRUMP
    barackTrump
    DonaldJ.Trump
    one%
    hello_world
    hello-world
    helloWORLD
    import
    cat
    cat2
    d0ge
    5nake
    d0g
    C-3PO
    C3P0
    print
    def



