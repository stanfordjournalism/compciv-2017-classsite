**************************
Finding the Raven's rhymes
**************************

You can check out an interactive example at `http://regexr.com/3f1c8`_


We know that the Len\ **ore** sound is prominent in Edgar Allen Poe's, The Raven. But what about all the other rhymes?

    This I sat engaged in **guessing**, but no syllable **expressing**

    Leave no black plume as a **token** of that lie thy soul hath **spoken**!

Prompt
======

Find the 10 most common rhymes used in the poem.

Expected output
===============

.. code-block:: text


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



Approach 1: gather last 3 letters of every word
===============================================

Let's break it down in pseudocode.


1. Use ack and a regex to match the last 3 letters of every word

    The pattern we want is: :regexp:`\w{3}\b`

    Putting that in :cmd:`ack`:

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

    .. code-block:: console

        $ ack -o '\w{3}\b' poe-raven.txt \
            | sort \
            | uniq -c


5. Sort the counted list in reverse-numerical order

    .. code-block:: console

        $ ack -o '\w{3}\b' poe-raven.txt \
            | sort \
            | uniq -c \
            | sort -rn

6. Filter for the first 10 results.

        $ ack -o '\w{3}\b' poe-raven.txt \
            | sort \
            | uniq -c \
            | sort -rn \
            | head -n 10



Unexpected output
-----------------

Unfortunately, not quite right, Only 3 of the line-endings in the expected output are in this output:


.. code-block:: text
   :emphasize-lines: 1,3,9

      65 ing
      58 the
      53 ore
      31 and
      24 his
      23 hat
      18 oor
      14 ber
      13 ven
      11 ill



Approach 2: gather last 3 letters of every 5-letter-or-more word
================================================================





Complete solution
=================

.. code-block:: console

    ack '\b\w\w+(\w{3,})\b' --output '$1' | sort | uniq -c | sort -n

