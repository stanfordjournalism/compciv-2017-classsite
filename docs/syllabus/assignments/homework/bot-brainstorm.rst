**************
Bot-Brainstorm
**************

Brainstorm the ideas for five different data-focused bots. You don't actually have to build them, just think of ideas that you might want to do for the final project, alone, or with a partner.



Rubric
======

Points: 20

Due date: 2017-03-07


Deliverables
------------

Email dun@stanford.edu with the subject line:

``compciv-2017::your_sunet_id::bot-brainstorm``

And attach 5 text files, ``bot1.txt`` to ``bot5.txt``


Requirements
------------

Each text writeup has these sections:


- Description: just a couple of lines describing what the bot does.
- The Arguments: What are the values the bot will take as input, e.g. a location, or date, or some other value that will affect what the bot calculates.
- Data sources: descriptions, including links, to at least 3 different datasets or APIs that the bot will draw from.
- Data transformations: descriptions of what the bot will *do* to the data to find insights, e.g. sorting, filtering, transforming.
- The Story: a rough template of what the bot will *publish*. This is not the same as how or where it publishes (e.g. to Twitter, or Reddit, or to a website).
- References: links to any other useful resources, or inspirations.



Example writeups
================




Example: Your Congressmember's Latest Votes
-------------------------------------------

Given a user's home location, finds out who their Congressmembers are (both Senators and House member), and what their latest roll call votes are, and their email address and phone numbers.


Arguments
^^^^^^^^^

The user's home location, e.g. "Menlo Park, CA, 94025"


Data sources
^^^^^^^^^^^^

- Mapzen Search API: used to convert human-readable locations into geospatial coordinates: https://mapzen.com/documentation/search/search/
- Sunlight Foundation Congress Locate API: Given a zip code, or a latitude/longitude, find likely House representative https://sunlightlabs.github.io/congress/legislators.html
- ProPublica Congress Represent endpoint for a specific member's vote positions: https://propublica.github.io/congress-api-docs/#get-a-specific-member-39-s-vote-positions


Data transformations
^^^^^^^^^^^^^^^^^^^^

- Converting human-readable address or location to latitude/longitude (i.e. geocoding)
- Filtering Congress roll for legislators who represent a given geography
- Filtering votes by Congressmember, sorting by most recent


Example story
^^^^^^^^^^^^^

If the user puts inputs "100 University Ave, Palo Alto, CA"

A possible story might be:

.. code-block:: text

    For the address of:
    100 University Ave, Palo Alto, CA

    The likely House representative is:
    Rohit Khanna, Democrat, CA-17
    https://khanna.house.gov/
    555-867-5309

    The U.S. Senators for CA are:

    Diane Feinstein, Democrat
    http://www.feinstein.senate.gov/public/
    555-222-3333

    Kamala Harris, Democrat
    https://www.harris.senate.gov/
    555-777-9999

    Latest votes:

    Khanna:

    2017-02-12: HR 101 - "Standard Equal Rules Act of 2016
    Yes

    2017-02-01: HR 101 - "Super Patriot Act"
    No

    2017-01-25: HR 101 - "Cookies Taste Good Act"
    Yes


    (etc for the Senators)


Inspirations
^^^^^^^^^^^^

ProPublica app for finding your legislators my address/zip code, as well as a listing of major votes:

https://projects.propublica.org/represent/

Who Represents You in the U.S. Congress:
http://www.whoismyrepresentative.com/



Example: Officer-involved shootings near you
--------------------------------------------

Description
^^^^^^^^^^^

Given a user's human-readable location (e.g. "Stanford University"), this bot produces a message listing the 5 closest officer-involved shootings, as well as a locator map showing the user's location in relation to those 5 incidents, and a Google Street View Map for each shooting location.

Arguments
^^^^^^^^^

The bot takes in one argument: the user's location/address, e.g. "Omaha, Nebraska"


Data sources
^^^^^^^^^^^^

- Washington Post fatal police shootings data: a CSV of the data collected by WaPo reporters. Includes addresses/locations for each incident: https://github.com/washingtonpost/data-police-shootings
- Mapzen Search API: used to convert human-readable locations into geospatial coordinates: https://mapzen.com/documentation/search/search/
- Google Static Maps API: used to show the user's location in relation to the incidents: https://developers.google.com/maps/documentation/static-maps/intro#quick_example
- Google Street View Image API: used to get a Google Street View image of a given address https://developers.google.com/maps/documentation/streetview/intro#url_parameters


(note: as it turns out, the Washington Post may not be the best place to get this data as they don't have it down to the address level)


Data transformations
^^^^^^^^^^^^^^^^^^^^

- Translate a human-readable address into geospatial coordinates, e.g. ``
100 W Broadway, Council Bluffs, IA`` into the latitude/longitude values of ``41.238``,``-95.854``, i.e. "geocode"
- Geocode each of the Washington Post police shootings incidents, i.e. create a new dataset with ``latitude`` and ``longitude`` columns.
- Sort the police shootings by distance to a given point (use the haversine formula once everything has been geocoded)
- Given a location string, produce the equivalent Street View Image and STatic Maps API URLs


Example story
^^^^^^^^^^^^^



.. code-block:: text

    Here is a map of the 3 nearest fatal police shootings to Stanford University, California, since 2015:


    https://maps.googleapis.com/maps/api/staticmap?size=650x400&markers=Stanford+University,CA&markers=Palo+Alto,CA


    1. John Doe, 28, unarmed white male shot in Palo Alto, California, on March 10, 2016

    https://maps.googleapis.com/maps/api/streetview?size=600x400&location=Palo+Alto,CA

    2. Sally Doe, 56, armed Asian female shot in Menlo Park, California, on February 10, 2016:

    https://maps.googleapis.com/maps/api/streetview?size=600x400&location=Menlo+Park,CA

    3.  Nick Doe, 42, unarmed black male shot in Sacramento, California, on February 10, 2015: https://maps.googleapis.com/maps/api/streetview?size=600x400&location=Sacramento,CA


References/Inspirations
^^^^^^^^^^^^^^^^^^^^^^^

The Officer Involved project, by Josh Begley, data artist for the Intercept, is an array of street view images geocoded to the recorded address of a fatal police encounter:

https://theintercept.co/officer-involved/




Reading about bots
==================

Read these examples/anecdotes/case studies over the weekend:

The Best Bots
-------------

- The L.A. Times Quakebot: most people think of bots as something to serve users, or at least the abstract needs of said users. Quakebot was built to take over the boring and repetitive work of a reporter so that the reporter could do real work. And as is the nature of data and reproducible processes, Quakebot also produced content useful for LAT readers.

    + Example QuakeBot-bylined story: http://www.latimes.com/local/lanow/la-me-earthquakesa-earthquake-39-quake-strikes-near-view-park-windsor-hills-calif-onvisi-story.html
    + https://www.theatlantic.com/technology/archive/2014/03/how-a-california-earthquake-becomes-the-news-an-extremely-precise-timeline/284506/
    + http://www.slate.com/blogs/future_tense/2014/03/17/quakebot_los_angeles_times_robot_journalist_writes_article_on_la_earthquake.html
    + http://sanfrancisco.cbslocal.com/2015/05/29/usgs-mistakenly-reports-magnitude-5-1-earthquake-near-redding/

- SCOTUS_Servo: https://twitter.com/scotus_servo - Life and death and the pursuit of happiness are directly impacted by how Justices interpret even just commas, nevermind words, or clauses. Same goes for what they write in opinions



    - http://joshblackman.com/blog/2015/10/05/scotus-now-tracks-changes-to-revised-opinions-and-combats-link-rot/
    - https://gigaom.com/2014/06/12/clever-piece-of-code-exposes-hidden-changes-to-supreme-court-opinions/
    - Example catch: https://twitter.com/SCOTUS_servo/status/476118183473319936
    - Tweets Track Secret Edits to SCOTUS Opinions (headlines always focusing on the delivery vehicle/tech, and not on the idea):  http://www.lawsitesblog.com/2014/06/tweets-track-secret-edits-scotus-opinions.html
    -
- @Politwoops: One of the most well-known and beloved bots. Also notable for being an example of how an API is defined by a company's priorities and values.

    + https://projects.propublica.org/politwoops/
    + http://www.theverge.com/2015/8/24/9196969/twitter-shuts-down-politwoops-diplotwoops
    + https://www.buzzfeed.com/alexkantrowitz/twitters-politwoops-shutdown-explanation-doesnt-add-up
    + Source code: https://github.com/propublica/politwoops
    + Twitter API for status deletion notices, https://dev.twitter.com/streaming/overview/messages-types#status_deletion_notices_delete


- NewsDiffs http://newsdiffs.org/

    + Taking the Stealth Out of Editing https://www.nytimes.com/2016/09/25/public-editor/liz-spayd-new-york-times-public-editor.html
    + Insider’s View of Changes, From Outside http://www.nytimes.com/2012/07/01/opinion/sunday/article-changes-are-shown-in-a-tool-created-by-outsiders.html

- The botmaker who sees through the Internet https://www.bostonglobe.com/ideas/2014/01/24/the-botmaker-who-sees-through-internet/V7Qn7HU8TPPl7MSM2TvbsJ/story.html

- IFTTT: bots aren't just for programmers. Create a free IFTTT account and play around with all the possible APis and combinations. It's point-and-click, it reveals endpoints you might not have thought of before, and the trigger part "just works"

    + http://lifehacker.com/the-best-ifttt-recipes-to-make-the-most-of-your-vacatio-1778763165
    + Ask HN: What's the most creative use of IFTTT you've seen? https://news.ycombinator.com/item?id=5755879

- Sam Lavigne and Fletcher Bach's collection of news/performance-art bots/scripts. Some of them might not fall under the usual definition of "bot", but only inasmuch as a bot is really no different from any other automated process of mundane steps.

    + Auto-generated supercuts of CPSAN videos: https://twitter.com/cspanfive
    + The Bot That Automatically Faxes Prisons Their Shitty Yelp Reviews  https://motherboard.vice.com/en_us/article/the-bot-that-automatically-faxes-prisons-their-shitty-yelp-reviews
    + Street Views of interesting political addresses http://antiboredom.github.io/streetviews/
    + Online Shopping Center (shopping via EEG) http://lav.io/shopping_center/
    + Transform any text to a patent application

Bots that have a beginning and end and/or a determined path
-----------------------------------------------------------

- @everyword, One Man's Quest to Tweet Every Word in the English Language: http://gawker.com/5854314/one-mans-quest-to-tweet-every-word-in-the-english-language
- @fuckeveryword, @BenghaziWord: http://www.slate.com/blogs/future_tense/2015/12/29/thinkpiece_bot_magic_realism_bot_and_other_great_2015_twitter_bots.html
- A Bookshop Is Tweeting "Philosopher’s Stone" To Piers Morgan After He Said He’d Never Read A Word Of Harry Potter https://www.buzzfeed.com/ikrd/a-bookshop-is-tweeting-the-entire-harry-potter-book
- @momarobot https://twitter.com/momarobot

Bots that react to user (i.e. external) input/activation
--------------------------------------------------------

- Twitter taught Microsoft’s AI chatbot to be a racist asshole in less than a day: http://www.theverge.com/2016/3/24/11297050/tay-microsoft-chatbot-racist
- Make Hitler Happy: The Beginning of Mein Kampf, as Told by Coca-Cola: http://gawker.com/make-hitler-happy-the-beginning-of-mein-kampf-as-told-1683573587
- @PrimitivePic https://twitter.com/primitivepic?lang=en
- Which are some of the most interesting Slack bots? https://www.quora.com/Which-are-some-of-the-most-interesting-Slack-bots
- The internet’s alt-right are mistakenly arguing with a bot http://www.theverge.com/2016/10/7/13202794/arguetron-twitter-bot-alt-right-internet-bigots-4chan-sarah-nyberg
- On Twitter, a Battle Among Political Bot https://www.nytimes.com/2016/12/14/arts/on-twitter-a-battle-among-political-bots.html

Bots that monitor a stream of data, or subscribe to a source of "push notifications"
------------------------------------------------------------------------------------


- NYT Anonymous: https://twitter.com/nytanon
- Edits to Wikipedia pages on Bell, Garner, Diallo traced to 1 Police Plaza http://www.politico.com/states/new-york/city-hall/story/2015/03/edits-to-wikipedia-pages-on-bell-garner-diallo-traced-to-1-police-plaza-087652
- With Twitter's Help, Watch Congress Edit Wikipedia https://www.nytimes.com/2014/07/15/upshot/twitter-wikipedia-and-a-closer-eye-on-congress.html
- FEC Itemizer - what political campaigns filed for today: https://projects.propublica.org/itemizer/
- When Trump Tweets, This Bot Makes Money: http://www.npr.org/2017/02/04/513469456/when-trump-tweets-this-bot-makes-money
- How I won 4 Twitter contests a day (every day for 9 months straight) http://www.hscott.net/twitter-contest-winning-as-a-service/
- Reuters built a bot that can identify real news on Twitter http://www.popsci.com/artificial-intelligence-identify-real-news-on-twitter-facebook
- Two news developers built a Twitter bot to tell you when the game is getting good http://www.niemanlab.org/2014/03/one-shining-moment-alert-two-news-developers-built-a-twitter-bot-to-tell-you-when-the-game-is-getting-good/
- The Year of the FactChecking Bot http://www.niemanlab.org/2016/12/the-year-of-the-fact-checking-bot/
- AWS urges developers to scrub GitHub of secret keys https://www.itnews.com.au/news/aws-urges-developers-to-scrub-github-of-secret-keys-375785



Scheduled bots
--------------

- Google Bot: https://support.google.com/webmasters/answer/182072?hl=en
- On this Day feature for Facebook: https://www.facebook.com/help/439014052921484/
- Facebook Friend Anniversary: https://www.theatlantic.com/technology/archive/2015/11/the-virtue-of-the-facebook-friend-anniversary/415272/

Bots that just do their own things
----------------------------------

- Darius Kazemi's Blindfolded Bot Shops for You http://www.core77.com/posts/23892/Darius-Kazemis-Blindfolded-Bot-Shops-for-You
- @twoheadlines https://twitter.com/twoheadlines
- A bot crawled thousands of studies looking for simple math errors. The results are concerning. http://www.vox.com/science-and-health/2016/9/30/13077658/statcheck-psychology-replication

