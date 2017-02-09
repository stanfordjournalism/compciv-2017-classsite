*************************************
Beautiful Soup - HTML and XML parsing
*************************************

HTML is just a text format, and it can be deserialized into Python objects, just like JSON or CSV. HTML is notoriously messy compared to those data formats, which means there are specialized libraries for doing the work of extracting data from HTML which is essentially impossible with regular expressions alone.

Obligatory link to infamous StackOverflow question: "RegEx match open tags except XHTML self-contained tags"

http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags



HTML Basics
===========

HTML is yet another language, a *markup language*, to be specific.


To see the difference between HTML and "just text", make a HTML file that contains this text:

.. code-block:: html

    This is one line.

    This is another line.

    This is a link: http://www.example.com/


Compare that to a HTML file with that text:

.. code-block:: html

    <p>This is one line.</p>

    <p>This is another line line.</p>

    <p>This is a <a href="http://www.example.com/">link</a></p>


HTML tags
---------

The most prominent feature of HTML are **tags** that are denoted by angle brackets, e.g. The **p** tag is denoted by an opening tag, ``<p>`` and a closing tag, ``</p>``.

.. code-block:: html

    <p>This is some text inside paragraph tags</p>

Tags can be nested within each other:

.. code-block:: html

    <p>
        Here is <strong>bold text</strong>
    </p>



Not all tags come in pairs. For instance, line breaks are represented with a single ``<br>`` tag:


.. code-block:: html

    <p>Hello

    <br> World</p>


Tag attributes
--------------


The other prominent feature of HTML is how tags can have **attributes**. For example, the tag ``<a>`` -- think of "a" as short for **anchor** -- represents what is commonly known as a **hyperlink**:

.. code-block:: html

    This is supposed to be a <a>link</a>


But we commonly think of hyperlinks as, well, *linking* to something. To encode the destination of an anchor tag, we use the ``href`` **attribute**:


.. code-block:: html

    This is a <a href="http://www.example.com">link</a>


The syntax for HTML tag attributes is:

- The **name** of the attribute, e.g. ``href``
- Followed by an **equals** sign with no surrounding whitespace
- Followed by a quoted value (common convention is double-quotes)

The attributes are always in the **opening** tag. And a tag can have multiple attributes:


.. code-block:: html

    This is <a href="http://www.nytimes.com" target="_blank">another link</a>



CSS selectors
-------------

CSS stands for `Cascading Style Sheets <https://www.w3.org/Style/CSS/Overview.en.html>`_. It's a whole language of its own, but what we're most concerned about is the convention of using HTML attributes of ``id`` and ``class`` as a way to specify a group of elements:


.. code-block:: html

    <p id="a-first-paragraph">A paragraph</a>

    <p class="hello">A paragraph with class</p>




Additional reading about HTML
-----------------------------

HTML could be its own course. My intent is that you know the fundamentals of HTML -- basically, that it's another data-as-text format -- without having to be burdened by the details. Here is some recommended reading to give you some additional background:

- Getting started with HTML: https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started
- HTML text fundamentals: https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals
- The **HTML** section in Chapter 3 of "Interactive Data Visualization for the Web": http://chimera.labs.oreilly.com/books/1230000000345/ch03.html

The **HTML** section of "Automate the Boring Stuff" chapter on Web Scraping also contains some useful background material:

https://automatetheboringstuff.com/chapter11/#calibre_link-2937

Using BeautifulSoup
===================

The `BeautifulSoup library <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_, which comes with the Anaconda distribution of Python, is a popular library for **parsing** HTML. By "parse", I mean, to take raw HTML text and deserialize it into Python objects.

This is the preferred way of importing the BeautifulSoup library:

.. code-block:: python

    from bs4 import BeautifulSoup


We typically want to parse HTML pages fetched from the Internet. But since HTML is *just text*, we can practice on plain old strings of HTML. In the snippet below, I use the variable ``html`` to refer to a simple HTML formatted string.

I use the ``BeautifulSoup()`` function, which takes 2 arguments:

- The **string** of HTML to be parsed
- The name of the HTML parser to use, as a string. This second argument, you just memorize as being ``"lxml"`` (BeautifulSoup is meant to be a wrapper around different HTML parsers -- a technical detail you don't need to worry about at this point).

I use the variable named ``soup`` to refer to the object that the ``BeautifulSoup()`` function returns. I leave it to you to interactively investigate for yourself what the ``type`` of that object is, and to read up on its documentation:

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup

.. code-block:: python

    from bs4 import BeautifulSoup
    html = '<p>Hello</p> <p>world</p>'
    soup = BeautifulSoup(html, 'lxml')


The ``soup`` variable contains a ``BeautifulSoup`` object, which has a bevy of attributes and methods.

One is ``text``, which will basically remove all of the HTML code and produce the readable text from the HTML:

.. code-block:: python

    >>> soup.text
    'Hello world'


Deserializing objects from HTML
-------------------------------

Sometimes the plaintext simplification is useful. But generally, we care about the HTML structure, because the markup often denotes things that are meant to be thought of as discrete objects.

In the simple HTML string as given -- ``"<p>Hello</p> <p>world</p>"`` -- we have 2 paragraphs. The ``BeautifulSoup`` object contains a method named ``find_all()`` which allows us to deserialize that structure as a **list** of tags:


.. code-block:: python

    >>> things = soup.find_all('p')
    >>> things
    [<p>Hello</p>, <p>world</p>]


Those square brackets usually denote a Python **list**. Actually, what we have as a return value of the ``find_all()`` method, is a ``bs4.element.ResultSet`` object. Think of it as a special kind of list in the world of ``bs4``. Each element of that list is also a special object -- e.g. ``<p>Hello</p>` -- but more than just a standard Python string:


.. code-block:: python

    >>> type(things)
    bs4.element.ResultSet
    >>> len(things)
    2
    >>> t = things[0]
    >>> type(t)
    bs4.element.Tag
    >>> t.name
    'p'
    >>> t.text
    'Hello'


Extracting attributes from HTML with BeautifulSoup
--------------------------------------------------

A very common pattern in web-scraping is to download a page full of links and then to extract the URLs that those links point to, and then programmatically download/parse those pages.

Take a look at http://www.example.com

If you're using a modern browser, you should be able to right-click and **View Source**. Or you could just ``curl`` the URL and download it as raw text. Either way, this is an excerpt of what you'll see:

.. code-block:: html

    <body>
    <div>
        <h1>Example Domain</h1>
        <p>This domain is established to be used for illustrative examples in documents. You may use this
        domain in examples without prior coordination or asking for permission.</p>
        <p><a href="http://www.iana.org/domains/example">More information...</a></p>
    </div>
    </body>


That "More information..." text is a hyperlink that goes to the URL:

http://www.iana.org/domains/example

Here's how to extract that URL with BeautifulSoup -- first, we have to use the ``requests`` library to actually download the contents of that URL:

.. code-block:: python

    >>> from bs4 import BeautifulSoup
    >>> import requests
    >>> resp = requests.get('http://www.example.com')
    >>> html = resp.text
    >>> soup = BeautifulSoup(html, 'lxml')

Use the ``find_all()`` method of the ``soup`` object to specify the ``<a>`` tags. Though there's only one hyperlink in this HTML text, it's still treated as a list (or rather, a ``ResultSet``) of *one element*:

.. code-block:: python

    >>> tags = soup.find_all('a')
    >>> tags
    [<a href="http://www.iana.org/domains/example">More information...</a>]
    >>> t = tags[0]
    >>> t
    <a href="http://www.iana.org/domains/example">More information...</a>
    >>> type(t)
    bs4.element.Tag
    >>> t.text
    'More information...'


The ``Tag`` object also a ``attrs`` attribute, which returns a **dict** object of the HTML tag's attributes. In this case, there is only one attribute:

.. code-block:: python

    >>> type(t.attrs)
    dict
    >>> t.attrs
    {'href': 'http://www.iana.org/domains/example'}
    >>> t.attrs['href']
    'http://www.iana.org/domains/example'

What if we want to print all the URLs that are linked to from the page at ``http://www.iana.org/domains/example``? See if you can repeat the above logic on your own:


(for explicitness sake, I pretend we're writing a script from scratch)

.. code-block:: python

    from bs4 import BeautifulSoup
    import requests

    resp = requests.get('http://www.example.com')
    soup = BeautifulSoup(resp.text, 'lxml')

    new_url = soup.find_all('a')[0]['href']

    new_resp = requests.get(new_url)
    new_soup = BeautifulSoup(new_resp.text, 'lxml')

    links = new_soup.find_all('a')

    for link in links:
        print(link.attrs['href'])


CSS selectors with BeautifulSoup
--------------------------------

Note: I'm kind of new to BS4 myself. ``find_all()`` is a nice method, but ultimately, I think we want to use the ``BeautifulSoup`` object's method of ``select()``:


.. code-block:: python

    from bs4 import BeautifulSoup
    import requests

    resp = requests.get('http://www.example.com')
    soup = BeautifulSoup(resp.text, 'lxml')

    links = soup.select('a')

Read more here:

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors



More reading about BeautifulSoup
--------------------------------

I don't recommend reading *all* of the documentation on BeautifulSoup. But here are some examples/sections that you should familiarize yourself with:


Official documentation
^^^^^^^^^^^^^^^^^^^^^^

- Making the soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup
- Kinds of objects: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-objects
- Navigating the tree: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree
- Searching the tree: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree
- Calling a tag is like calling ``find_all()``: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all
- CSS selectors: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors


The "Automate the Boring Stuff" textbook has a `whole chapter on Web Scraping <https://automatetheboringstuff.com/chapter11/>`_. But it encompasses a lot about web-scraping beyond HTML parsing.

For the purposes of this lesson, read the following sections:

- Opening Your Browser’s Developer Tools
- Using the Developer Tools to Find HTML Elements
- Creating a BeautifulSoup Object from HTML
- Finding an Element with the select() Method
- Getting Data from an Element’s Attributes




Cats and Dogs exercises
-----------------------

Do you know HTML parsing? Then try this exercise:

Given the HTML at this URL:

http://stash.compciv.org/2017/webby/pets.html

1. Print the total number of URLs.
2. Print the total number of URLs that are nested in a `<li>` tag.
3. Print the number of links that have a ``dog`` class.
4. Print all the URLs of the links that are of class ``cat`` and ``video``
5. Print the text and URL of each hyperlink that has a class of ``dog`` and ``article``



Answers
^^^^^^^

Download the contents of the URL and make it into soup:

.. code-block:: python

    from bs4 import BeautifulSoup
    import requests

    URL = 'http://stash.compciv.org/2017/webby/pets.html'

    rawhtml = requests.get(URL).text
    soup = BeautifulSoup(rawhtml, 'lxml')


1. Print the total number of URLs.
""""""""""""""""""""""""""""""""""


.. code-block:: python

    >>> links = soup.select('a')
    >>> print(len(links))
    10


2. Print number of URLs that are nested in a `<li>` tag.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: python

    >>> links = soup.select('li a')
    >>> print(len(links))
    8

3. Print the number of links that have a ``dog`` class.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: python

    >>> links = soup.select('a.dog')
    >>> print(len(links))
    4

4. Print the URLs of the links that are of class ``cat`` and ``video``
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: python

    >>> links = soup.select('a.cat.video')
    >>> for a in links:
    ...:    atts = a.attrs
    ...:    print(atts['href'])
    https://www.youtube.com/watch?v=2XID_W4neJo
    https://www.youtube.com/watch?v=tntOCGkgt98
    https://www.youtube.com/watch?v=nX1YzS_CYIw
    https://www.youtube.com/watch?v=pNhESKKiEDI


5. Print text and URL of each hyperlink that has class of ``dog`` and ``article``
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: python

    for a in soup.select('a.dog.article'):
        print(a.text, a.attrs['href'])


Note how whitespace (i.e. the newline characters) from the original HTML are preserved in the printed values:


.. code-block:: text

                    A dog that does not work
                 https://en.wikipedia.org/wiki/Companion_dog
    Dogs in the military http://ngm.nationalgeographic.com/2014/06/war-dogs/paterniti-text














