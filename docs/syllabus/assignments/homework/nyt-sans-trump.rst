***********************************
New York Times Headlines Sans Trump
***********************************

Write a script that downloads the RSS feed of New York Times front-page stories, selects the first 10 headlines of stories that **do not** mention Trump, and then produces a printed output of the headlines, as well as an audio version of the headlines.

This is mostly a review of how to do HTML/XML scraping/parsing (pretty much just like JSON/CSV, it's just structured text), as well as an example of how to use a "fun" API (Amazon's AWS). But more importantly, how simple and important it is to *filter* things.

This exercise was inspired by Farhad Manjoo, the NYT tech writer, who struggled vainly to ignore Trump news for a week:

https://www.nytimes.com/2017/02/22/technology/trump-news-media-ignore.html


    My point: I wanted to see what I could learn about the modern news media by looking at how thoroughly Mr. Trump had subsumed it. In one way, my experiment failed: I could find almost no Trump-free part of the press.

    But as the week wore on, I discovered several truths about our digital media ecosystem. Coverage of Mr. Trump may eclipse that of any single human being ever. The reasons have as much to do with him as the way social media amplifies every big story until it swallows the world. And as important as covering the president may be, I began to wonder if we were overdosing on Trump news, to the exclusion of everything else...

    In previous media eras, the news was able to find a sensible balance even when huge events were preoccupying the world. Newspapers from World War I and II were filled with stories far afield from the war. Today’s newspapers are also full of non-Trump articles, but many of us aren’t reading newspapers anymore. We’re reading Facebook and watching cable, and there, Mr. Trump is all anyone talks about, to the exclusion of almost all else.

    There’s no easy way out of this fix. But as big as Mr. Trump is, he’s not everything — and it’d be nice to find a way for the media ecosystem to recognize that.



Filtering is both deceptively simple, and as complex as Manjoo makes it. So we're only focusing on the simple parts, which can be done by a computer and an if-statement and loop.



Rubric
======

Points: 10

Due date: 2017-03-07


Deliverable
-----------

Email dun@stanford.edu with the subject line:

``compciv-2017::your_sunet_id::nyt_sans_trump``

And attach a script named ``nyt_sans_trump.py``


Expected results
----------------

When I run ``nyt_sans_trump.py`` on my own machine and command-line, like so:

.. code-block:: shell

    $ python nyt_sans_trump.py

I should see 10 headlines printed to my screen that do not mention Trump:

.. code-block:: text

    Colon and Rectal Cancers Rising in Young People
    Lee Jae-yong, Samsung Leader, Is Indicted on Bribery Charges
    Women Suspected in Kim Jong-nam Killing to Be Charged, Malaysia Says
    Automakers Knew of Takata Airbag Hazard for Years, Suit Says
    A Constitutional Right to Facebook and Twitter? Supreme Court Weighs In
    How to Get Better Customer Service, and Skip the Rage
    Losing a Fortune Often Comes Down to One Thing: Family
    In California, a Move to Ease the Pressures on Aging Dams
    Finally, a Retirement Plan for Job-Hopping Millennials
    In the Middle of a Career, and Finding a New One



When ``nyt_sans_trump.py`` script finishes its work, it should also save a file (in the same working directory) named:

``trump-less-headlines.mp3``

This MP3 is the audio readout of those 10 headlines.


Requirements
------------

The RSS feed for the NYTimes front page is here:

http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml

You should use the AWS Polly API to turn text into headlines.

You can read more about how to get started with AWS and Polly: :doc:`/guide/topics/aws/intro-to-aws-boto3`

Your script should filter out any stories that have something to do with Trump. The algorithm can be as easy as stories that don't have "Trump" in either the headline or description.

Your script should only include the first 10 Trump-less headlines, for printing out to standard output, and for turning into a MP3.





Walkthrough
===========

RSS feeds are used to serialize a publisher's stories in easy, machine-readable format. That is, it's a data format much more formal and easier to work with than trying to scrape stories from raw HTML.


Downloading and parsing XML
---------------------------

Reading XML is similar to reading HTML. First, since the RSS feed is online, we use ``requests`` to download from the URL:

.. code-block:: python

    import requests
    resp = requests.get('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
    rawtxt = resp.text


Note that the XML of a RSS feed, like the HTML of a webpage, is still just text. We need to use a library to deserialize that text into data objects. In this case, BeautifulSoup works just as it does for HTML:


.. code-block:: python

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(rawtxt, 'lxml')


We don't have a lot of time to go over the formal specifics of XML. But it is something we can kind of read and understand the structure. For example, we can observe that the structure contains lots of ``<item>``  elements, each one looking like this:

.. code-block:: xml

    <item>
        <title>
        On Washington: Trump’s Budget Is Aspirational. Reality in Congress Will Change It.
        </title>
        <link>
        http://www.nytimes.com/2017/02/28/us/politics/trumps-budget-is-aspirational-reality-in-congress-will-change-it.html?partner=rss&emc=rss
        </link>
        <guid isPermaLink="true">
        http://www.nytimes.com/2017/02/28/us/politics/trumps-budget-is-aspirational-reality-in-congress-will-change-it.html
        </guid>
        <media:content url="https://static01.nyt.com/images/2017/03/01/us/01hulse/01hulse-moth.jpg" medium="image" height="151" width="151"/>
        <media:description>
        House Speaker Paul D. Ryan and Senate Majority Leader Mitch McConnell spoke after a meeting with President Trump at the White House on Monday.
        </media:description>
        <media:credit>Stephen Crowley/The New York Times</media:credit>
        <description>
        The president’s budget proposal is simply a starting point, and will look quite different once lawmakers have their say.
        </description>
    </item>



Extracting the title and description of each story
--------------------------------------------------

There's a lot of gunk in each ``<item>`` element, but at least we can assume that each ``<item>`` element has its own children ``<title>`` and ``<description>`` elements:


I leave it to you to test what the result of each command is in the interacctive shell...but the end result should be that the ``titletxt`` and ``desctxt`` variables contains string objects that are the plaintext representations of a story's title and description.

.. code-block:: python


    items = soup.select('item')
    item = items[0]
    title = item.select('title')[0]
    desc = item.select('description')[0]


    titletxt = title.text
    desctxt = desc.text



Filtering for Trump
-------------------

Go back to using your human senses. Go to the front-page of https://www.nytimes.com, and ask yourself: *how do I know if a story contains something about President Trump?*

If you, like me, like to keep things simple, your algorithm is probably this:

- Does the word "Trump" appear in the headline?
- Does the word "Trump" appear in the description?

If the answer to both questions, i.e. boolean expressions, is "No" or ``False``, then we might assume that a given story is *not* about Trump.

Just to be extra careful, you may want to do further filtering, like excluding all stories that are in the Politics section. But for our purposes, a simple search for the literal value "Trump" is good enough.





Creating an audio reading of the top 10 headlines
-------------------------------------------------

Before we move further, there's no point in jumping to the audio-conversion if your script can't even *print* each Trump-less headline to standard output. Somewhere in your ``nyt_sans_trump.py`` script should be this kind of action (minus all the setup of course):


.. code-block:: python

    for item in items:
        # etc
        headline = item.select('title')[0].text
        if 'TRUMP' not in headline.upper():
            print(headline)


That variable ``headline`` is just a string of text, right? No reason that we can't test out the Amazon Polly API independently.

Referring to this boto3/AWS-in-general guide:

:doc:`/guide/topics/aws/intro-to-aws-boto3`

Here's a quick snippet of how to send text to the Polly API, get a response, get the audio stream as ``bytes``, and then to write those ``bytes`` to a file on disk so that you can play it with your favorite MP3 player:


.. code-block:: python

    HEADLINE = 'Dewey Defeats Truman, And Popcorn is Yummy'

    import boto3
    session = boto3.Session(profile_name='default')
    polly = session.client('polly')
    polly_resp = polly.synthesize_speech(OutputFormat='mp3',
                                    Text=HEADLINE,
                                    VoiceId='Russell')



To write the contents of that response to a file:

.. code-block:: python

    audiodata = polly_resp['AudioStream'].read()
    thefile = open('trump-less-headlines.mp3', 'wb')
    thefile.write(audiodata)
    thefile.close()


Note that we don't want to be calling the Polly API more than once. That is, we want to collate all of the headlines into a single string, and then make a single audio file. In other words, this is **not** a good pattern:


.. code-block:: python

    for item in items:
        # etc
        headline = item.select('title')[0].text
        if 'TRUMP' not in headline.upper():
            print(headline)

            polly_resp = polly.synthesize_speech(OutputFormat='mp3',
                                    Text=headline,
                                    VoiceId='Russell')

            audiodata = polly_resp['AudioStream'].read()
            thefile = open('trump-less-headlines.mp3', 'wb')
            thefile.write(audiodata)
            thefile.close()



Look at where the file-writing logic is in regards to the loop. For every item, the file is re-written, over and over...that's not what we want.


You will probably want to **two** loops.

The first loop creates a list of headlines belonging to Trump-less stories.

The second loop prints out the first ten of those Trump-less headlines and also creates a big string, that is just those 10 headlines concatenated together.

Pass that "big string" into Polly.
