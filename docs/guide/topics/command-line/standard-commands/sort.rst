*****************************
sort - sort lines in a stream
*****************************


The ``sort`` program takes lines of text as input and outputs the text in alphabetical-sorted order.

To sort the lines in a file:

.. code-block:: shell

    $ sort fruits.txt


The most common use, though, is to sort lines from **standard inpput**, piped in from another program:

.. code-block:: shell

    $ curl http://2017.compciv.org/_downloads/fruits.txt | sort


Use-cases
=========


Sorting in reverse
------------------

If you want the list of sorted lines to be in descending order, i.e. ``z`` before ``a``, use the ``-r`` flag:


.. code-block:: shell

    $ sort -r fruits.txt


Sorting numbers
---------------

By default, ``sort`` sorts *alphabetically*. When numbers are treated as just characters, then ``100`` will be less than ``9``.

Given this list of numbers:

.. code-block:: text

    99
    8
    0
    100
    42
    -7

The default sorting behavior will result in:


.. code-block:: text

    -7
    0
    100
    42
    8
    99


Using the ``-n`` flag will force ``sort`` to rank numerical characters by their **numerical** order:


.. code-block:: shell

    $ sort -n numbers.txt


The result:

.. code-block:: text

    -7
    0
    8
    42
    99
    100


Sorting in reverse numerical order
----------------------------------

A very common use-case is to sort a list of numbers in reverse-order, i.e. biggest on top. You can call ``sort`` with both the ``-r`` and the ``-n`` flags:


.. code-block:: shell

    $ sort -r -n numbers.txt

    # alternatively, you can combine the flags like this:

    $ sort -rn numbers.txt



A very common question is to look for the "Top N" of a sorted list. So pipe ``sort`` into ``head``.

The following example reads the data from a remote URL via ``curl``, pipes it into ``sort``, and finally into ``head`` to show only the top 5 numbers

.. code-block:: shell

    $ curl http://2017.compciv.org/_downloads/numbers.txt \
        | sort -rn \
        | head -n 5


A necessary step before uniq
============================

The ``uniq`` program is a nice example of a Unix program that does something very focused: it takes in a stream of lines, and outputs just the unique lines. But it can do this unique/grouping comparison line-by-line. In other words, if you feed it a file in which "apples" is the first line and "apples" is the last line, and there are a bunch of non-"apples" lines in between, ``uniq`` will not know that ``apples`` was duplicated.


In order to get the intended effect of ``uniq``, ``sort`` is used to sort the lines of text before piping into ``uniq``:



.. code-block:: shell

        $ curl http://2017.compciv.org/_downloads/fruits.txt | sort | uniq


Sorting by most frequent occurrences
------------------------------------

The ``sort`` program, in modern implementations, does have a ``-u`` flag that effectively does the ``uniq`` function, without actually having to call ``uniq``:

.. code-block:: shell

        $ curl http://2017.compciv.org/_downloads/fruits.txt | sort -u





