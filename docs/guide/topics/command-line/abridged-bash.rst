**********************************************************
The abridged guide to shell scripting and the command line
**********************************************************

There's a lot more to the command line than just running commands like ``curl``.  It is its own programming environment, and as you become a more experienced programmer, in any language, you might find it more convenient to write scripts in the command line (Bash)'s programming syntax, instead of jumping into *another* shell, like the Python interactive shell.

However, the system Unix-like shell has a lot of dangerous, legacy baggage, to the point that it really is easier just to learn a language like Python. That said, the system shell is the de facto shell, the lingua franca if you will, for your OSX laptop and for any Linux machine in the cloud -- which is basically most of them as far as we're concerned.

That is why, as opposed to doing everything via Python code, we learn to run shell commands like this:


.. code-block:: shell

    $ curl `https://www.example.com`

    $ ssh dun@cardinal.stanford.edu

    $ curl http://www.placecage.com/300/400 > awesome.jpg



So for the first two weeks, our experience with the system shell (aka **Bash**), is going to be awkward. Learning about the system shell confers a lot of great programmatic principles. On the other hand, we don't want to spend too much time learning it, because Python is its own language. But on the other hand, the system shell/Bash/Unix is not just a fun theoretical concept, it's the framework for modern computing. So, we just kind of *have* to learn it, and most programmers just get by with trial and error.

This guide is meant to briefly cover some of that trial and error...





Common tasks in the shell
=========================




Finding out more about a command
--------------------------------

Use the ``man`` program to read the documentation for any given command/program. To learn more about ``cat``, for example:


.. code-block:: shell

    $ man cat


Reading/writing/input/output
----------------------------

.. rubric:: How to download a URL

Use the **curl** program, which is basically ubiquitous across all command-line systems:


.. code-block:: shell

    $ curl https://www.nytimes.com


.. rubric:: How to write to a file


Use the ``>`` operator to signify that you want to send the output of one program into a file at the given filename. Whatever is currently at that filename gets **wiped out**:


.. code-block:: shell

    $ curl https://www.nytimes.com > nytimesfrontpage.html

    $ echo 'oops' > nytimesfrontpage.html



.. rubric:: How to print the contents of a file to screen (standard output)

For text files, use **cat**:


.. code-block:: shell

    $ cat nytimesfrontpage.html



.. rubric:: How to direct the output of one program into another program

That's the **pipe**, a concept so integral to the command-line that you just have to memorize it:


.. code-block:: shell

    $ curl https://www.nytimes.com | ack 'Trump'




File and directory navigation
-----------------------------


.. rubric:: What directory am I currently in?

Use ``pwd`` (print working directory) to print out the full path of the current working directory. Any operation you do, such as creating new files/directories, are relative to the current working directory.

.. code-block:: shell

    $ pwd


In general, you should never do anything that creates, accesses, or destroys a file/directory without making sure you know exactly where you are.


.. rubric:: What files and subdirectories exist in the current working directory?

Run the ``ls`` command ("list directory contents") without any arguments:

.. code-block:: shell

    $ ls



.. rubric:: How do I move up to the parent directory?

The **double dot** character sequence is interpreted as "the parent directory".

For example, if you start out in your home directory, and then you ``cd`` (change directory) into your ``Downloads`` subdirectory, which itself has a ``movies`` subdirectory:

.. code-block:: shell

    $ cd Downloads/movies


To get back to ``Downloads``, i.e. the parent directory of ``movies``:

.. code-block:: shell

    $ cd ..


.. rubric:: How do I jump back to my "home" directory?

You can either call ``cd`` without any arguments:

.. code-block:: shell

    $ cd

Or use the ``~`` (tilde), which is interpreted as a shortcut for the home directory:


.. code-block:: shell

    $ cd ~





.. rubric:: What computer am I on? Who am I?


Seems silly, but you're going to frequently find yourself logging/tunneling into remote computers to do things like launch a web application or an annoying Twitter bot. Like Leonardo DiCaprio in "Inception", you might forget what system you're actually on.

Use ``whoami`` and ``hostname``, respectively, to print out your username and the name of the computer.



How to write a Bash script
==========================

A Bash script is just a series of commands that you've put into a text file to execute in a batch, rather than typing them one-by-one.

Bell Labs programmer Lorinda Cherry explains in this `1982 video <https://youtu.be/tc4ROCJYbm0?t=15m37s>`_  what it means to create a shell script. Nothing has changed since then.

Here's a primer `on creating basic shell scripts <http://www.compciv.org/recipes/cli/basic-shell-scripts/>`_, i.e. how to wrap your code into a file and run it from the command line.



Important keyboard shortcuts in the shell
=========================================

This may seem counter-intuitive, but you'll find dealing with the shell (and programming in general) a lot easier if you memorize the important keyboard shortcuts. These keyboard shortcuts exist to minimize the kinds of mistakes you can make in the first place, especially the kind of unknown unknown errors that are easy to make when dealing with the Spartanesque command line interface.


(Note that many of these keyboard shortcuts work in other shells, including Python's interactive shell.)


Tab or Die
----------


The Tab key is used for autocompletion of programs and filenames that exist on the system. That is its function in almost every programming environment, whether its the Atom or Sublime Text editor, the Unix shell of the 80s or of today, or the Python shell.

If you're programming, and you aren't hitting Tab several times a minute, you are probably doing something wrong, or about to do something catastrophic.

Relying on the Tab key is a realization that our human minds cannot be trusted to remember exactly the correct spelling of archaic program names, nor our fingers to type without making typos, nor our eyes to reliably differentiate a ``l`` from ``1`` or ``I``.

Here's a nice friendly explainer by How-To Geek: `Use Tab Completion to Type Commands Faster on Any Operating System <http://www.howtogeek.com/195207/use-tab-completion-to-type-commands-faster-on-any-operating-system/>`_



Use Ctrl-C to break out of confusing situations
-----------------------------------------------

Sometimes you'll accidentally run a program that executes, oh, an infinite number of times. Like the ``yes`` program:


.. code-block:: shell

    $ yes yes


Hit **Ctrl-C** on your keyboard to break execution of a program, or non-responsiveness from the interpreter. This also works in the Python shell.


Use the up-arrow to cycle through past commands
-----------------------------------------------

Running the ``history`` command will show you all the commands that you've recently run, in sequential order. But if you just need to re-run the previous command with a minor alteration, hit the **Up arrow** and the command will be fully written out at the prompt, ready for you to hit Enter.


Use Ctrl-A and Ctrl-E to jump to the beginning and end of a line
----------------------------------------------------------------

The command line, being all-text, doesn't have the convenience of mouse-clicking to move the cursor, like we're used to in a modern word processor or text editor. While you *could* just hold down the left or right arrow when you need to fix something at the beginning or end of a line, you should memorize using **Ctrl-A** to jump to the beginning of a line , or **Ctrl-E**, to jump to the end.

I think "A", as in, the beginning of the alphabet. And "E", as in, "End".


Use Ctrl-L to clear the screen
------------------------------

Command-line programs spit a lot of text on to the screen. And usually, that output text can be a distraction. Use **Ctrl-L** to start with a blank screen.




Things to basically just memorize
=================================


Again, we don't have time to go through a comprehensive guide on how to program in the Unix shell. So here are a few shell features to just memorize for expediency:


There is no undo
----------------

The following command will direct the text string, ``hello world``, into the file named ``LIFESAVING_INFO.docx``:


.. code-block:: shell

    $ echo 'hello world' > LIFESAVING_INFO.docx

What if ``LIFESAVING_INFO.docx`` already exists and actually lives up to its name? Too bad, it now contains ``hello world``, and there is no undelete or undo.


The following command uses ``cp`` to copy the contents of one file to another filename:


.. code-block:: shell

    $ cp dumbfile.txt super-valuable-file.xlsx


Again, makes no difference if the destination file already exists -- ``cp`` wipes out what was there.




Use single quotes to enclose arguments and values
-------------------------------------------------

Basically, if something is not a command -- e.g. ``curl``, ``echo``, ``ls`` -- then you probably want to wrap it in **single-quotes**. In the example below, the argument to the ``curl`` program -- ``http://www.example.com`` is enclosed in single-quotes:

.. code-block:: shell

    $ curl 'http://www.example.com'

To be fair, ``http://www.example.com`` is considered "safe", in that it doesn't have any special characters that will be interpreted/executed by the shell. However, the following URL, which is a valid URL that generates a Google static map, has special characters such as the **ampersand** which will not be read in as literal text by the standard Unix-like shell:


https://maps.googleapis.com/maps/api/staticmap?size=800x500&zoom=14&center=Stanford+CA


In other words, do **not** do this:

.. code-block:: shell

    $ curl https://maps.googleapis.com/maps/api/staticmap?size=800x500&zoom=14&center=Stanford+CA > map.jpg


Enclose that URL argument in single quotes. Might as well enclose that simple destination filename too:


.. code-block:: shell

    $ curl 'https://maps.googleapis.com/maps/api/staticmap?size=800x500&zoom=14&center=Stanford+CA' > 'map.jpg'



Why not double-quotes?
^^^^^^^^^^^^^^^^^^^^^^

In other languages, such as Python, double-quotes can be used just as single-quotes when it comes to enclosing text values.

However, in Bash, special characters that are quoted in double-quotes *will* be interpreted.

In other words, this command:

.. code-block:: shell

    $ echo "$987,293"

-- is equivalent to:

.. code-block:: shell

    $ echo $987,293


And dollar-signs have a very special meaning for the Bash interpreter. If you want to actually print out the literal string of ``$987,293``, use single quotes:


.. code-block:: shell

    $ echo '$987,293'



Use the backslash at the end-of-a-line to continue a long command
-----------------------------------------------------------------

The shell interprets each **newline character** as the *end* of a command. You notice this when, every time you hit Enter, the command you typed in gets executed.

So commands are read in, one line at a time. But for aesthetic and readability concerns, sometimes we need to break up a single command into separate lines.

To do this, put a backslash at the end of the line. Do not add any space after the backslash.

In the following example, the ``curl`` command has some verbose options (e.g. ``--silent``) and the URL to download is very long.

The backslash is used to split the single command into two lines for easier reading.



.. code-block:: shell

    $ curl --silent --output destination.file \
        http://somereally.long.weburl/thatis/too/long/for/easy/readability.html


Use the backslash to split up a pipe sequence
---------------------------------------------

Note that if you end a line with a **pipe** character, the shell will anticipate that your sequence is not quite done and won't execute until you type a line *without* a pipe at the end:


.. code-block:: shell

    $ curl http://www.example.com |
        ack '\w+' |
        sort |
        uniq -c > wordcount.txt



However, I recommend that you use a **backslash** to signify continuation of a long pipe sequence. It's interpreted the same by the shell, so my recommendation is purely a stylistic one that is easier to read and may prevent mistakes later on. Remember, you will spend far more time reading over your own code than actually writing it:



.. code-block:: shell

    $ curl http://www.example.com \
        | ack '\w+' \
        | sort \
        uniq -c > wordcount.txt







.. Text is the default interface
.. =============================


.. Most command line programs are designed in the spirit of how Doug McIlroy summarized the `Unix philosophy <https://en.wikipedia.org/wiki/Unix_philosophy>`_:

..         This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.


.. This means that, in general, programs don't have any opinions about what should be done with their output, other than to spit it out to screen (standard out). It's up to the user to decide whether or not to



.. How to direct the output from a program onto the screen
.. -------------------------------------------------------

.. Most computers today have a monitor connected to them.



.. echo hello world
.. ----------------



.. cat is our friend
.. -----------------



..  which has several facets and phrasings the main principle of which is:





.. How to direct the output of a program into a file
.. ===================================================






Fear the power of the command line
==================================

One of the other principles of Unix is "silence is golden", i.e. if don't raise errors unless an error actually happens. This is not bad design, theoretically. But sometimes things that are errors to humans -- such as accidentally running the ``rm`` command in such a way that it deletes *everything* from your system -- is **not** an error to the computer.


There's a lot of advantages to that approach. It respects the intelligence of the programmer -- if the programmer wrote that code, then that's what the programmer must really want to do. But programmers are human, and when they make mistakes, the Unix philosophy doesn't do much to protect them.



A famous example is Pixar literally wiping out "Toy Story 2" because of a slightly errant Bash command; or, as Mental Floss puts it: `How One Line of Text Nearly Killed 'Toy Story 2' <http://mentalfloss.com/uk/entertainment/27204/how-one-line-of-text-nearly-killed-toy-story-2>`_:

    Writing in his book Creativity Inc, Pixar co-founder Ed Catmull recalled that in the winter of 1998, a year out from the release of Toy Story 2, somebody (he never reveals who in the book) entered the command '/bin/rm -r -f *' on the drives where the film's files were kept.

    The object of said command is to remove everything from a given location, and to remove it quickly. It did its job.

    "First, Woody's hat disappeared. Then his boots. Then he disappeared entirely," recalls Catmull. "Whole sequences—poof!—were deleted from the drive."

    ...The plug was pulled, but not in time—90% of the film was gone, erased "in a matter of seconds."


Here's a fun animated recap of that disaster: `How Toy Story 2 Almost Got Deleted: Stories From Pixar Animation <https://www.youtube.com/watch?v=8dhp_20j0Ys>`_.


