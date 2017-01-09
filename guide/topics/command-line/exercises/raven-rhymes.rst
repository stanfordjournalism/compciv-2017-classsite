**************************
Finding the Raven's rhymes
**************************

We know that the ``ore`` sound is prominent in Edgar Allen Poe's, The Raven. But what about all the other rhymes?

    This I sat engaged in **guessing**, but no syllable **expressing**

    Leave no black plume as a **token** of that lie thy soul hath **spoken**!

Prompt
======

Find the 10 most common rhymes used in the poem.

Expected output
===============

          65 ing
          36 ore
          14 ber
          13 ven
          11 ght
          10 tly
          10 red
           9 ken
           9 ess
           7 ted



Strategy
========

Let's break it down in pseudocode.


1. Use ack and a regex to match the last 3 letters of every word
   .. code-block:: console

         $ ack '\w{3}\b' poe-raven.txt

2. Specify that ack outputs only the match
    .. code-block:: console

         $ ack -o '\w{3}\b' poe-raven.txt

3. Sort the result
    .. code-block:: console

        $ ack -o '\w{3}\b' poe-raven.txt \
            | sort

4. Get a unique count of each term

5. Sort the counted list in reverse-numerical order

6. Filter for the first 10 results.




Complete solution
=================

.. code-block:: console

    ack '\b\w\w+(\w{3,})\b' --output '$1' | sort | uniq -c | sort -n

