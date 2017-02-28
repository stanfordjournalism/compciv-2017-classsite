******************************************
Checklist of Understanding Lists and Dicts
******************************************

Accessing a simple list
=======================

Start off with the variable ``mylist`` set to this list:


.. code-block:: python

    mylist = ['oranges', 'pears', 'kiwis', 'apples', 'eggs' ]


Questions
---------

1. Get the number of elements in the ``mylist``.
2. Get the first element in the ``mylist``.
3. Get the last element in the ``mylist``
4. Get the second element in the ``mylist``
5. Get the second to last element in the ``mylist``
6. Make a slice (i.e. sublist) of ``mylist``, beginning with the 3rd element.
7. Make a slice of ``mylist``, beginning with the 2nd element, through the 2nd-to-last element.


Expected results
----------------

1. Get the number of elements in the ``mylist``.


.. code-block:: python

    5




2. Get the first element in the ``mylist``.

.. code-block:: python

    THING

3. Get the last element in the ``mylist``

.. code-block:: python

    THING

4. Get the second element in the ``mylist``

.. code-block:: python

    THING

5. Get the second to last element in the ``mylist``

.. code-block:: python

    THING

6. Make a slice (i.e. sublist) of ``mylist``, beginning with the 3rd element.

.. code-block:: python

    THING


7. Make a slice of ``mylist``, beginning with the 2nd element, through the 2nd-to-last element.

.. code-block:: python

    THING



Solutions
---------


1. Get the number of elements in the ``mylist``.


.. code-block:: python

    >>> len(mylist)
    5

2. Get the first element in the ``mylist``.

.. code-block:: python

    >>> mylist[0]
    mylist[0]

3. Get the last element in the ``mylist``


.. code-block:: python

    >>> mylist[-1]
    THING

4. Get the second element in the ``mylist``

.. code-block:: mylist[1]

    >>> mylist
    THING

5. Get the second to last element in the ``mylist``

.. code-block:: mylist[-2]

    >>> mylist
    THING


6. Make a slice (i.e. sublist) of ``mylist``, beginning with the 3rd element.

.. code-block:: python

    >>> mylist
    THING

7. Make a slice of ``mylist``, beginning with the 2nd element, through the 2nd-to-last element.

.. code-block:: python

    >>> mylist
    THING



Looping through a list
----------------------


Questions
^^^^^^^^^

1. Print out each element in ``mylist``, but in upper-case.
2. Count the number of elements in ``mylist`` using a for-loop (i.e. without using ``len``)
3. Get the sum of the lengths of each element (i.e. character length) in ``mylist``


Sorting a list with sorted()
----------------------------

1. Make a new copy of ``mylist``, except with the elements sorted in alphabetical order.
2. Make a new copy of ``mylist``, except with the elements sorted in reverse-alphabetical order
3. Make a copy of ``mylist`` with the elements sorted by length, shortest to longest.
4. Make a copy of ``mylist`` with the elements sorted by length, longest to shortest
5. Make a copy of ``mylist`` with the elements sorted by length, longest to shortest, and in case of a tie, in alphabetical order.
6.



