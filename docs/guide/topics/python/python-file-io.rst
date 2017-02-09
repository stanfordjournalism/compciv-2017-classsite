


Fundamentals of reading and writing files
=========================================


A file path





Opening a file for reading or writing


The ``open()`` method returns a **file object**. The arguments we specify are:

1. A string containing the path to a file, i.e. the **filename**
2. A string specifying the operation mode for the file: basically, do we want to *read* or *write* to a file?



Reading and writing to the contents of a file object
----------------------------------------------------


https://docs.python.org/3.6/tutorial/inputoutput.html#methods-of-file-objects

The file object has methods for the reading and writing of the contents of a file.



https://docs.python.org/3.6/tutorial/inputoutput.html

https://docs.python.org/3.6/tutorial/inputoutput.html#reading-and-writing-files



- Reading a file by lines using ``for``


- wr



Common file errors
==================

Errors of file-naming
---------------------

As I've said before, the misnaming of things, especially files, will be the kind of dumb bug that will suck hours of your life if you are not careful.


Mistaking the filename (i.e. a string object) as the file object itself:

.. code-block:: python


    >>> fn = 'data.txt'
    >>> fn.read()


Trying to read from a file that doesn't exist:

.. code-block:: python

    fn = 'blahalsdkfjasklj38731ljxzcvlkj278.txt'
    open(fn, 'r')
    FileNotFoundError: [Errno 2] No such file or directory:     'blahalsdkfjasklj38731ljxzcvlkj278.txt'


Trying to write to a file that doesn't exist

If you write to a path *relative* to where your code is running, the ``open()`` method will create a new file if a file doesn't already exist:

.. code-block:: python
    from random import randint

    fn = 'randomfilename-{a}-{b}.txt'.format(a=randint(1,10000), b=randint(1,10000))
    open(fn, 'w')
    # no error because open() assumes we want to create a new file
    # by the name of whatever is in ``fn``


However, if you try to write to a filename that includes a directory that doesn't exist, ``open()`` will throw an error:


fn = join('some', 'fun', 'path', 'sdakflblahblalh.txt')
open(fn, 'w')

FileNotFoundError: [Errno 2] No such file or directory: 'some/fun/path/sdakflblahblalh.txt'



Advanced file reading and writing
=================================


Common Patterns
===============


Not overwriting a file if it already exists


Saving a file after downloading it using ``requests``


Check the existing of a file before trying to re-download it


Parsing a file, line by line, as CSV

Reading from a file, line by line, writing to a new file












