**********************************
Hello Regular Expression Exercises
**********************************

A variety of regular expression exercises that are probably way too hard for you to figure out after just one lesson.


.. note::


    Lesson: :doc:`/guide/topics/regular-expressions/regex-early-overview`


    Practice: :doc:`/guide/topics/regular-expressions/regex-early-overview`


Rubric
======

Due date:
    1:00 PM, :doc:`/syllabus/agendas/2017-01-12`

.. csv-table::
    :header: "Points", "Metric"
    :widths: 10, 90

    1,Having a correct subject line of ``yourid::hello-regex``
    1,Your email is in plaintext
    3,Lines 1-10 are the answers to the included regex exercises



Delivery format
===============

Send an email to dun@stanford.edu with the subject:

``your_sunet_id::hello-regex``

Where ``your_sunet_id`` is your Stanford student ID, all-lowercase.


Milestones
==========

Sending a plaintext email
-------------------------

Email should have exactly 10 lines and be in plaintext.

The answers to each of the exercises should be one-line only. No need to number them.




Regex Exercises 1 to 4, using the Presidential Debate transcript
----------------------------------------------------------------

The answers to each of the regex exercises should consist of a single line and the regex pattern that satisfies the prompt.



Download this text transcript from the first presidential debate between Trump and Clinton and open it in your text editor: :download:`Presidential Debate Transcript, 2016-09-27 </stash/speeches/presidential-debate-2016-09-27.txt>`.




.. rubric:: 1. All words of 15 letters or more.



.. rubric:: 2. Each time someone was interrupted.

I'll just give this to you. In the transcript, an interruption seems to be indicated by a hyphen, or double-hyphen, at the end of the line. But hyphens are also used to indicate pauses in the middle of speech:

.. code-block:: text

        Wallace: Thank you secretary Clinton. I want to follow-up-

        Trump: Chris, I think it’s -- I think I should respond. First of all, I had a very good meeting with the President of Mexico. Very nice man. We will be doing very much better with Mexico on trade deals. Believe me. The NAFTA deal signed by her husband is one of the worst deals ever made of any kind signed by anybody. It’s a disaster. Hillary Clinton wanted the wall. Hillary Clinton fought for the wall in 2006 or there abouts. Now, she never gets anything done, so naturally the wall wasn't built. But Hillary Clinton wanted the wall.

        Wallace: Well, let me --

        Trump: We are a country of laws. By the way --



So we need to use the :regexp:`$` anchor to specify that we want only the hyphens in that position.

Here is the pattern that seems to answer this question:

:regexp:`-$`


Bonus question: what would be the pattern needed to count interruptions per speaker?



.. rubric:: 3. When the words "right" or "wrong" were used to end a sentence.

Hint: the end of a sentence is generally indicated by some kind of punctuation. But remember you need to match a *literal* dot.


.. rubric:: 4. Each time Trump spoke in 140 or fewer characters.

Doesn't have to be word characters.





Regex Exercises 5 to 7 with Trump tweets
----------------------------------------



Download this CSV file of :download:`@realDonaldTrump tweets into your text editor </stash/data/twitter/realdonaldtrump-tweets.csv>`



.. rubric:: 5. All words that are followed by the word, me


We don't have an easy way to specify just the ``Text`` field of each tweet, but that's ok, the other fields don't have free-form text.


.. rubric::  6. Match the hour of the day that a tweet was sent.

Here's what a tweet's timestamp looks like:

``2016-12-31 13:17:21 +0000``




.. rubric::  7. Match every URL that is in the tweet text

Even though the web-verison of each tweet has the URLs full-resolved:

`<https://twitter.com/realDonaldTrump/796055597594578944>`_

In the simplified data, only the Twitter-t.co-shortened versions are used:

    - `<https://t.co/MXrAxYnTjY>`_
    - `<https://t.co/FZhOncih21>`_


But *assume* that the URL could have any domain, not just ``t.co``. Better to be safe and lexible than make a bad assumption...



.. rubric:: Using the San Francisco HSA 90-day emergency shelter waitlist data


Download this :download:`CSV file of emergency shelter waitlist data </stash/data/socrata/sf-hsa-90-day-emergency-shelter-waitlist.csv>`.

The data as it appears on Socrata can be `found here <https://data.sfgov.org/w/w4sk-nq57/ikek-yizv?cur=N8Bh_VodE4F&from=root>`_


.. rubric::  8. Match every row in which the date of birth was before 1950.

OK, this exercise is meant to show that there are limitations to regexes. We can't do math with them, for example, e.g. filter the birthdates to be older than 1950.

The best we can do is think of an admittedly clunky hack: what's another way to describe the set of numbers smaller than ``50``? Or, for that matter, ``5``?


.. rubric::  9. Capture the month, day, and year of birth for each row.

Given that the DOB field is in this format:


``MM-DD-YYYY``


Here's what the pattern *without* capturing groups looks like:


:regexp:`\d{2}-\d{2}-\d{4}`


And here is the answer, with capturing groups for each datapoint:

:regexp:`(\d{2})-(\d{2})-(\d{4})`


.. rubric::  10. Reformat each date of birth so that they are in `YYYY-MM-DD` format


Here's what the original data looks like:

.. code-block:: text

    649,16363001,05-18-1944,394674,6664080,
    827,17005010,12-02-1963,29676,6689096,
    447,16352006,10-21-1974,394128,6633925,
    773,17002007,09-28-1971,398594,6680655,
    782,17003004,08-03-1962,19817,6683536,
    659,16363012,05-12-1949,307904,6665382,
    829,17005012,06-16-1997,391891,6691363,

With the correct replacement format, this is the result:

.. code-block:: text

    649,16363001,1944-05-18,394674,6664080,
    827,17005010,1963-12-02,29676,6689096,
    447,16352006,1974-10-21,394128,6633925,
    773,17002007,1971-09-28,398594,6680655,
    782,17003004,1962-08-03,19817,6683536,
    659,16363012,1949-05-12,307904,6665382,
    829,17005012,1997-06-16,391891,6691363,
