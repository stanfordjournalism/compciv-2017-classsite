*****************
Hello World Email
*****************

Some exercises to get you acquainted with plaintext, how data is delimited, and other journalistic concepts.


Rubric
======

Due date:
    1:00 PM, :doc:`/syllabus/agendas/2017-01-12`

.. csv-table::
    :header: "Points", "Metric"
    :widths: 10, 90

    1,Having a correct subject headline
    1,Your email is in plaintext
    1,Line 1 of email describes your operating system
    1,Lines 2-11 are Pulitzer story picks in CSV format
    1,Lines 12-21 are the answers to the included regex exercises






Delivery format
===============

Send an email to dun@stanford.edu with the subject:

``your_sunet_id::hello-world-email``

Where ``your_sunet_id`` is your Stanford student ID, all-lowercase. For example, if I were to submit an assignment to myself, the subject line would look like:

    dun::hello-world-email

.. warning:: Be Exact


    For this assignment, I'll overlook small mistakes. Like not using a double-colon to delimit your Stanford ID from the assignment slug, e.g. `Dun:Helloworld-email`.

    For subsequent homework assignments, though, you will be expected to follow things to the letter, or risk receiving a zero for the assignment.




The Work
========

Sending a plaintext email
-------------------------

Email should have exactly 21 lines.


Line 1: Describe your operating system
--------------------------------------

The first line of your email should simply describe your operating system and version.

- `How to find OSX/macOS version number`  <https://support.apple.com/en-us/HT201260>`
- `How to find Windows version number <https://support.microsoft.com/en-us/help/13443/windows-which-operating-system>`

Sample lines:

``macOS 10.12.1``

``Windows 8.1``


Lines 2-11: The 10 most morally black-and-white Pulitzer winners
----------------------------------------------------------------

Look at the following award categories:

- `Public Service http://www.pulitzer.org/prize-winners-by-category/204`
- `Investigative Reporting http://www.pulitzer.org/prize-winners-by-category/206>`
- `International Reporting <http://www.pulitzer.org/prize-winners-by-category/210>`
- `National Reporting <http://www.pulitzer.org/prize-winners-by-category/209>`
- `Local Reporting <http://www.pulitzer.org/prize-winners-by-category/208>`
- `Explanatory Reporting <http://www.pulitzer.org/prize-winners-by-category/207>`
- `Feature Writing <http://www.pulitzer.org/prize-winners-by-category/211>`

You don't have to read each entry -- the summary is just fine. Make a list of award winners or finalists,
in the years 2000 to now, of the 10 stories which you think are the most black-and-white/cut-and-dry.

In your email to me, include that list in CSV, i.e. **comma-delimited format**, with
the number `1` being the most black-and-white, right-and-wrong of the stories
you selected:

.. code-block:: text

    1,http://www.pulitzer.org/winners/associated-press
    2,http://www.pulitzer.org/winners/sheri-fink
    3,http://www.pulitzer.org/winners/alan-miller-and-kevin-sack
    ...etc
    10,http://www.pulitzer.org/finalists/dave-philipps


Lines 12-21: The answers to the following 10 regex exercises
--------------------------------------------------------------


Given the following sample text:


.. code-block:: text

    hey there
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


What is the regex pattern that will do what is described?


1. The first word of every line
2. Each capitalized word.
3. All words of 6 letters or more
4. All words that begin with a consonant and end with a vowel
5. The word `the` and *only* `the`
6. Both variations of phone number formats
7. Match every dollar amount, sans the dollar signs.
