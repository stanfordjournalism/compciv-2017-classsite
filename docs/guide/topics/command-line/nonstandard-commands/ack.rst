**********************
ack - better than grep
**********************

**Ack** is a program meant to be a friendly replacement for the famous **grep**. Many of its most common flags and options are the same as ``grep`` (and here's a `separate overview guide on grep <http://www.compciv.org/unix-tools/#grep>`_), which makes it a "friendly" replacement.

But there are two key advantages to ``ack``:

1. It supports the full flavor of regular expressions (often referred to as `PCRE <http://pcre.org/>`_), which is the basically the same flavor of regex we'll be using in Python and most other languages.
2. It has an ``--output`` flag, which is a great way to combine with `capturing groups <https://regexone.com/lesson/capturing_groups>`_ for custom output.


Like ``grep`` and other grep-likes, you can use ``ack`` to match lines in a given file:


.. code-block:: shell

    $ ack '\w{5}' words.txt


But the most frequent usage is to have ``ack`` be part of a pipeline of filtering programs:


.. code-block:: shell

    $ curl http://www.example.com | ack '\w{5}'



Use-cases
=========

Outputting only where the pattern matches
-----------------------------------------

One of the kind of confusing things about all grep-like programs is that, by default, output any line that *contains* a specified pattern:


.. code-block:: shell

    $ curl http://www.example.com | ack '\w{5}'


Use the ``-o`` flag to return only the matches made by the specified regex pattern:


.. code-block:: shell

    $ curl http://www.example.com | ack -o '\w{5}'



Outputting captured groups
--------------------------

This feature (which requires understanding the regex notion of capturing groups) is the killer feature that makes ``ack`` worth installing no matter how many other grep-like programs you might already have. Use the ``--output`` flag (not to be mistaken for the ``-o`` flag), which takes as an argument the kind of string you would put in the "Replace" field, when doing a "Find-and-Replace".

Here's a toy example:


.. code-block:: shell

    $ echo 'Call Jenny at 8675309' | ack '(\d{3})(\d{4})' --output '$1-$2'



References
==========

- `Why Ack? <http://beyondgrep.com/why-ack/>`_
- `Command-line switches documentation <http://beyondgrep.com/documentation/>`_
