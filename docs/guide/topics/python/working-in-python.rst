***********************************************
Working in Python (How to Interact with Python)
***********************************************

Terminology in this guide:


.. rubric:: Just plain Python script

.. code-block:: python

    print('hello world')
    print('this is Python code in a script')
    99 + 33


.. rubric:: Interactive Python

This is demonstrating Python at the interactive shell.

.. code-block:: python

    >>> print('hello world')
    hello world
    >>> print('this is Python code executed by the interactive prompt')
    this is code entered into the interactive prompt
    >>> 99 + 33
    132



How to print to standard out
============================



.. code-block:: python

    print('hello world')



It's like the command line's ``echo``.



Using the Python interactive shell
==================================

From your system command line (doesn't matter if it's Windows or OSX or Linux):


.. code-block:: shell

    $ python


When Python is installed on your computer, the ``python`` command invokes the **Python interpreter**.



Always use ipython
------------------

When doing interactive Python, the only reason not to use ``ipython`` is if you've forgotten to type ``ipython`` instead of ``python``


Mind your shells and where you are
----------------------------------

It's like being taught in French class how to say "I'd like some cheese", *Je voudrais du fromage*, then flying to Beijing and wondering why no one is giving you the cheese.


.. code-block:: shell

    $ print(2 + 3)
    -bash: syntax error near unexpected token `2'

.. code-block:: python

    >>> echo 2 + 3
    File "<stdin>", line 1
        echo 2 + 3
         ^
    SyntaxError: invalid syntax





