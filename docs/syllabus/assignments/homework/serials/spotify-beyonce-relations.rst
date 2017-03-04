******************************************************
Solid Serialization of Béyoncé and her Spotify Friends
******************************************************

This assignment is part of: :doc`/syllabus/assignments/homework/solid-serialization-skills`


.. contents::


Using a JSON data response from Spotify's API, sort/filter/analyze the artists most related to Béyoncé, according to Spotify's algorithm.

The data file is mirrored here:

http://stash.compciv.org/2017/spotify-beyonce-related-artists.json

You can read Spotify's documentation of its ``related-artists`` endpoint here, including a description of each field:

https://developer.spotify.com/web-api/get-related-artists/

While messing around with the Spotify API may not be the most high-minded civic use of our time, it's certainly a really fun API with broad appeal to just about anyone. The fact that it's one of the best documented and easily accessible commercial APIs makes it a no-brainer to play with.


Deliverables
============

You are expected to deliver a script named: ``spotify_beyonce_relations.py``

This script has **4** prompts, which means at the very least, your script will contain 4 separate function definitions, from `foo_1` to `foo_4`.


When I run your script from the command line, I expect to see something like this:



.. code-block:: shell

    $ python spotify_beyonce_relations.py
    Done running assertions!


And I expect your script to have this code at the bottom:

.. code-block:: python

    def foo_assertions():
        assert type(foo_1()) is list
        assert len(foo_1())  is 20
        assert foo_1()[0] == "Destiny's Child"


        assert type(foo_2()) is list
        assert foo_2()[0]  == ['name', 'followers']
        assert foo_2()[-1][0]  == "Kelis"

        assert type(foo_3()) is list
        assert foo_3()[0]['name']  == 'Rihanna'
        assert foo_3()[-1]['popularity'] == 62

        assert type(foo_4()) is list
        assert foo_4()[0][1] == 20


    if __name__ == '__main__':
        foo_assertions()
        print("Done running assertions!")



That script should have a ``if __name__ == '__main__'`` conditional block, in which a function named ``foo_assertions()`` is executed.


Prompts
=======

The mirror of the ``related-artists.json`` result for Béyoncé is here:

http://stash.compciv.org/2017/spotify-beyonce-related-artists.json


Download (and cache) that file, then parse/deserialize the text data, then write the ``foo_`` functions to satisfy the following prompts:

1. List the names of the related artists
----------------------------------------

The Spotify API response contains a lot of metadata, such as thumbnails for each artist, that makes it hard just to see which artists are purportedly related to Béyoncé without straining your eyes.

Traverse the data object and print a simple list of names, in the same order as they are listed in the Spotify response.



Expected results:

.. code-block:: python

    ["Destiny's Child",
     'Kelly Rowland',
     'Alicia Keys',
     'Rihanna',
     'Ciara',
     'Keri Hilson',
     'Justin Timberlake',
     'Mariah Carey',
     'Christina Aguilera',
     'Cassie',
     'Jennifer Lopez',
     'Jennifer Hudson',
     'Chris Brown',
     'The Pussycat Dolls',
     'Fergie',
     'TLC',
     'Whitney Houston',
     'Ashanti',
     'Kelis',
     'Mary J. Blige']

2. List artists' names with number of followers, rank by followers
------------------------------------------------------------------


Expected output:

.. code-block:: python

    [['name', 'followers'],
     ['Rihanna', 8792360],
     ['Chris Brown', 3832426],
     ['Justin Timberlake', 2853318],
     ['Jennifer Lopez', 1493872],
     ['Alicia Keys', 1464533],
     ['Christina Aguilera', 1168887],
     ['Mariah Carey', 1106762],
     ['Whitney Houston', 903522],
     ['Ciara', 803715],
     ["Destiny's Child", 634049],
     ['Fergie', 539632],
     ['Mary J. Blige', 536947],
     ['Kelly Rowland', 479842],
     ['The Pussycat Dolls', 414452],
     ['TLC', 387450],
     ['Ashanti', 245022],
     ['Keri Hilson', 221302],
     ['Jennifer Hudson', 195102],
     ['Cassie', 140344],
     ['Kelis', 115659]]


3. List Beyonce's related artists as a list of slimmed-down data objects
-----------------------------------------------------------------------


For each artist in Beyonce's list, trim their data object to include only the following fields:

- 'followers'
- 'href'
- 'name'
- 'popularity'


Expected results:


.. code-block:: python


    [{'followers': 8792360,
      'href': 'https://api.spotify.com/v1/artists/5pKCCKE2ajJHZ9KAiaK11H',
      'name': 'Rihanna',
      'popularity': 94},
     {'followers': 3832426,
      'href': 'https://api.spotify.com/v1/artists/7bXgB6jMjp9ATFy66eO08Z',
      'name': 'Chris Brown',
      'popularity': 90},
     {'followers': 2853318,
      'href': 'https://api.spotify.com/v1/artists/31TPClRtHm23RisEBtV3X7',
      'name': 'Justin Timberlake',
      'popularity': 86},
     {'followers': 1464533,
      'href': 'https://api.spotify.com/v1/artists/3DiDSECUqqY1AuBP8qtaIa',
      'name': 'Alicia Keys',
      'popularity': 81},
     {'followers': 1106762,
      'href': 'https://api.spotify.com/v1/artists/4iHNK0tOyZPYnBU7nGAgpQ',
      'name': 'Mariah Carey',
      'popularity': 80},
     {'followers': 1168887,
      'href': 'https://api.spotify.com/v1/artists/1l7ZsJRRS8wlW3WfJfPfNS',
      'name': 'Christina Aguilera',
      'popularity': 80},
     {'followers': 1493872,
      'href': 'https://api.spotify.com/v1/artists/2DlGxzQSjYe5N6G9nkYghR',
      'name': 'Jennifer Lopez',
      'popularity': 79},
     {'followers': 634049,
      'href': 'https://api.spotify.com/v1/artists/1Y8cdNmUJH7yBTd9yOvr5i',
      'name': "Destiny's Child",
      'popularity': 75},
     {'followers': 903522,
      'href': 'https://api.spotify.com/v1/artists/6XpaIBNiVzIetEPCWDvAFP',
      'name': 'Whitney Houston',
      'popularity': 75},
     {'followers': 539632,
      'href': 'https://api.spotify.com/v1/artists/3r17AfJCCUqC9Lf0OAc73G',
      'name': 'Fergie',
      'popularity': 74},
     {'followers': 803715,
      'href': 'https://api.spotify.com/v1/artists/2NdeV5rLm47xAvogXrYhJX',
      'name': 'Ciara',
      'popularity': 73},
     {'followers': 387450,
      'href': 'https://api.spotify.com/v1/artists/0TImkz4nPqjegtVSMZnMRq',
      'name': 'TLC',
      'popularity': 73},
     {'followers': 536947,
      'href': 'https://api.spotify.com/v1/artists/1XkoF8ryArs86LZvFOkbyr',
      'name': 'Mary J. Blige',
      'popularity': 73},
     {'followers': 414452,
      'href': 'https://api.spotify.com/v1/artists/6wPhSqRtPu1UhRCDX5yaDJ',
      'name': 'The Pussycat Dolls',
      'popularity': 71},
     {'followers': 245022,
      'href': 'https://api.spotify.com/v1/artists/5rkVyNGXEgeUqKkB5ccK83',
      'name': 'Ashanti',
      'popularity': 71},
     {'followers': 479842,
      'href': 'https://api.spotify.com/v1/artists/3AuMNF8rQAKOzjYppFNAoB',
      'name': 'Kelly Rowland',
      'popularity': 70},
     {'followers': 221302,
      'href': 'https://api.spotify.com/v1/artists/63wjoROpeh5f11Qm93UiJ1',
      'name': 'Keri Hilson',
      'popularity': 67},
     {'followers': 115659,
      'href': 'https://api.spotify.com/v1/artists/0IF46mUS8NXjgHabxk2MCM',
      'name': 'Kelis',
      'popularity': 66},
     {'followers': 195102,
      'href': 'https://api.spotify.com/v1/artists/35GL8Cu2GKTcHzKGi75xl5',
      'name': 'Jennifer Hudson',
      'popularity': 65},
     {'followers': 140344,
      'href': 'https://api.spotify.com/v1/artists/27FGXRNruFoOdf1vP8dqcH',
      'name': 'Cassie',
      'popularity': 62}]




4. Do a group count of every genre keywords associated with Beyonce's related artists, list the genres by most popular
----------------------------------------------------------------------------------------------------------------------

.. note:: Update

    I neglected to mention what to do in the case of a tie, i.e. how ``pop`` and ``r&b`` have the same number of results. So you can just ignore that situation. I've altered the relevant assertion from:

    ``assert foo_4()[0] == ('pop', 20)``

    to:

    ``assert foo_4()[0][1] == 20``



Expected results:

.. code-block:: python

    [('pop', 20),
     ('r&b', 20),
     ('dance pop', 19),
     ('urban contemporary', 17),
     ('hip pop', 17),
     ('pop rap', 15),
     ('post-teen pop', 13),
     ('pop christmas', 13),
     ('soul christmas', 9),
     ('neo soul', 9),
     ('deep pop r&b', 7),
     ('europop', 5),
     ('southern hip hop', 3),
     ('soul', 3),
     ('new jack swing', 3),
     ('quiet storm', 2),
     ('indie r&b', 2),
     ('dwn trap', 2),
     ('motown', 1),
     ('boy band', 1),
     ('escape room', 1),
     ('neo mellow', 1),
     ('hollywood', 1),
     ('pop rock', 1),
     ('rap', 1)]






Background
==========

For a more thorough exploration of the Spotify API (albeit from the Command Line), check out my guide from a couple years back: http://www.compciv.org/recipes/data/touring-the-spotify-api/

The actual URL for the live endpoint of related-artists for Béyoncé can be found here:

https://api.spotify.com/v1/artists/6vWDO969PvNqNYHIOW5v0m/related-artists


Answers (Partial)
=================


I like to start off by writing a function that does the downloading and deserializing:

.. code-block:: python

    import json
    from os import makedirs
    from os.path import exists, join, basename
    import requests


    SRC_URL  = 'http://stash.compciv.org/2017/spotify-beyonce-related-artists.json'
    DATA_DIR = 'data-files'
    DATA_FNAME = join(DATA_DIR, basename(SRC_URL))

    def bootstrap_data():
        """ returns serialized object"""
        if exists(DATA_FNAME):
            rawjson = open(DATA_FNAME).read()
        else:
            r = requests.get(SRC_URL)
            makedirs(DATA_DIR, exist_ok=True)
            with open(DATA_FNAME, 'w') as f:
                f.write(r.text)
            rawjson = r.text
        return json.loads(rawjson)



The above script is a result of my desire for some organization. I only want to download the source data once. And I want that data file to be saved in a subdirectory:

``data-files/spotify-beyonce-related-artists.json``


However, you may not care about that. In any case, if you're going to use my code above, make sure you know what each line does, e.g. ``basename(SRC_URL)``.


After you've created a ``bootstrap_data()`` function that does all the data grabbing/parsing work, each subsequent function that needs the data can just call ``bootstrap_data()``:


.. code-block:: python


  def foo_1():
      """
      Return a list of artist names, from the list of artists most related to Béyoncé, according to the Spotify API, sorted by popularity
      """

      data = bootstrap_data()
      names = []
      for a in data['artists']:
          names.append(a['name'])

      return names



Or, if you prefer brevity:


.. code-block:: python

    def foo_1():
      return [a['name'] for a in bootstrap_data()['artists']]





