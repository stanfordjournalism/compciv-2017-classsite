********************************************
twython - Python wrapper for the Twitter API
********************************************


A collection of guides and information on how to access the Twitter API using the Twython Python library. Assumes varying degrees of familiarity about what Twitter is, and programming in general...


Assuming you have a Twitter account that you can tweet from via the web or your phone, the next step/leap is to access and run that Twitter account programmatically. We use the Python library, Twython, and jump through a bunch of hoops to set up a Twitter Application:

:doc:`/guide/topics/python-nonstandard-libraries/twython-guide/twitter-twython-app-auth`

After we have Twython set up, now it's time to learn the basics of how to tweet and collect data using all the fun programming concepts we've learned so far, including: how to read a Python dictionary, how to use functions, and how to not freak out when seeing error messages.

The following guide assumes you're relatively new to the data world of Twitter, and attempts to show how the Twython library connects to the documentation:

:doc:`/guide/topics/python-nonstandard-libraries/twython-guide/twitter-twython-api-basics`


And applying the basics to making some simple bots (for now):

Creating a bot that, searches for tweets and then based on hard-coded simplistic logic, reacts to each tweet.

:doc:`/guide/topics/python-nonstandard-libraries/twython-guide/twitter-twython-simple-grammar-corrector`


Creating a bot that generates random content (from Twitter, or anywhere) based on a body of text:


:doc:`/guide/topics/python-nonstandard-libraries/twython-guide/twitter-twython-simple-markov-bot`








Getting started with Twitter and Twython
========================================

.. warning:: TKTK

    The rest of this page is just old stuff that needs to be reorganized and expanded upon


Twython documentation: https://twython.readthedocs.io/en/latest/

Twitter REST API docs: https://dev.twitter.com/rest/public

Installing Twython
------------------

Go to your system's command line, and run the following command to install twython:

.. code-block:: shell

    $ pip install twython


Becoming a Twitter Developer
----------------------------


Twython is just code that makes it easier to interact with Twitter. It doesn't magically get you access to Twitter's functionality, especially if you don't have an account.

So:

1. Create a Twitter account if you don't have one.
2. Join the Twitter developers program by going to this URL (while logged in on Twitter): https://apps.twitter.com/app/new


Getting your credentials
------------------------

These next few steps are murky, and I need to revise the workflow, but basically you want to create a Twitter Application, and then go through the authentication process until you get your "OAuth" tokens. I have some instructions here but they probably won't make sense without the context of the previous class:

http://www.compjour.org/tutorials/twitter-app-authentication-process/#login-with-a-secondary-account-via-a-different-browser

(will update for next week)


After jumping through those hoops, you should be able to hand-create your own JSON/dictionary that looks like this:



.. code-block:: python

      {
        "app_key": "adsfasdfadsf",
        "app_secret": "345w345345",
        "oauth_token": "juyi76dsgb",
        "oauth_token_secret": "23423456345"
      }



Interacting with Twython
========================

.. warning:: Watch your security

    This guide is incomplete. The following instructions assume you are just pasting things into your console to try them out. Not that you're saving your credentials to a plaintext file where they can be easily read by anyone.

    If you have any questions, ask me. I'll fill in some more security details as we get into bot-making mode.



Authenticating with Twython
---------------------------



Official notes here: https://twython.readthedocs.io/en/latest/usage/starting_out.html#oauth-1-user-authentication

(you want to follow the Oauth1 workflow)


What I do is store my credentials in a JSON formatted file and read it into a script. But it all ends up looking like this if you paste it into the interactive shell:


.. code-block:: python

    from twython import Twython


    creds = {"app_key": "xyz",
        "app_secret": "Kasdf",
        "oauth_token": "asdf",
        "oauth_token_secret": "asdf"}

    client = Twython(app_key=creds['app_key'],
                app_secret=creds['app_secret'],
                oauth_token=creds['oauth_token'],
                oauth_token_secret=creds['oauth_token_secret'])



If you were able to successfully authenticate, that ``client`` object is what you use to start interacting with the API:



.. code-block:: python

    from twython import Twython


    # get your own profile information as a dict
    client.get_account_settings()

    # get user by screen name
    client.show_user(screen_name='realdonaldtrump')

    # get user by id
    client.show_user(user_id=20)

    # get a list of your 200 most recent followers
    req = client.get_followers_list(count=200)
    # req is a dict
    peeps = req['users']

    # get a list of @ev's 200 most recent followers
    req = client.get_followers_list(count=200, screen_name='ev')
    peeps = req['users']



Doing profile updates
---------------------

Check out the parameters available at the ``update_profile`` end point:

https://dev.twitter.com/docs/api/1.1/post/account/update_profile

And those will be the arguments in the ``update_profile`` method provided by the Twython API:

.. code-block:: python


    client.update_profile(description='i love the computerz', name='Comp Civ STANZ')


Sending tweets
--------------

Now for the fun stuff. To send a tweet, we use the ``update_status`` method.

That method maps directly to the documented endpoint, ``statuses/update``:

https://dev.twitter.com/rest/reference/post/statuses/update


.. code-block:: python

    client.update_status(status='I am alive!')



To send a reply, we need to provide an additional argument: ``in_reply_to_status_id``, which is the ``id`` number of the tweet we're replying to. **And** we have to include the screen name of the user that authored the tweet to which we are replying.

Given this tweet: https://twitter.com/realDonaldTrump/status/832198588201594880

Our ``update_status`` call looks like this:


.. code-block:: python

    client.update_status(status="But surely that cannot be, @realdonaldtrump?",
                         in_reply_to_status_id=832198588201594880)



Attaching media to our tweets
-----------------------------

Attaching an image or video to your tweet is not the same as just tweeting a link to the URL of that media:

https://twython.readthedocs.io/en/latest/usage/advanced_usage.html

There's a multi-stage process

1. Open a file for reading in byte-mode, i.e. ``'rb'``
2. Use the ``upload_media`` method and pass the file object into the ``media`` argument
3. The ``upload_media`` actually executes an API call that uploads to Twitter's media server. The return value of that call is a dictionary with a ``media_id`` key, which we need when actually sending our tweet with embedded media.
4. Finally, we call ``update_status``, and we pass a **list** of ``media_id`` values to the method's ``media_ids`` argument (even if we are only embedding one image)



.. code-block:: python

    # 1. open the image file for reading
    imgfile = open('image.jpg', 'rb')

    # 2. Call upload_media and pass in the imgfile object
    twit_resp = client.upload_media(media=imgfile)

    # 3. get the id value from the response object
    mx_id = twit_resp['media_id']


    # 4. Now send the tweet
    client.update_status(status='here is a photo i hope u like it', media_ids=[mx_id])

    # and of course, close the original file
    imgfile.close()


Here's a slimmer variation on that routine:


.. code-block:: python


    with open('image.jpg', 'rb') as img:
        twit_resp = client.upload_media(media=img)
        client.update_status(status="Heres more photos for u", media_ids=[twit_resp['media_id']])



Here's a routine that uploads multiple images. The flow is a little bit different. We use a for loop to call ``upload_media`` multiple times, each time extracting the ``'media_id'`` value from the response and adding to an array.

Then, after uploading all the images, we send the tweet and past the list of media ids as an argument:

.. code-block:: python

    image_filenames = ['clinton.jpg', 'bush-2.jpg', 'obama.jpg', 'trump.jpg']
    uploaded_ids = []
    for fname in image_filenames:
        with open(fname, 'rb') as img:
            twit_resp = client.upload_media(media=img)
            uploaded_ids.append(twit_resp['media_id'])


    client.update_status(status="i <3 these guys!", media_ids=uploaded_ids)




And here's some random fun:


.. code-block:: python

    from random import randrange, choice
    import requests
    import io


    # http://www.hanselman.com/blog/TheInternetsBestPlaceholderImageSitesForWebDevelopment.aspx
    IMG_SERVICES = [
        'http://baconmockup.com/{}/{}',
        'http://placebear.com/{}/{}',
        'http://fillmurray.com/{}/{}'
    ]


    def make_random_image_url():
        service_url = choice(IMG_SERVICES)
        w = randrange(15, 40) * 15
        h = randrange(15, 40) * 15

        return service_url.format(w, h)



    def get_remote_image_bytestream(url):
        resp = requests.get(url)
        bytestream = io.BytesIO(resp.content)

        return bytestream


    imgids = []

    for i in range(4):
        img = get_remote_image_bytestream(make_random_image_url())
        twit_resp = client.upload_media(media=img)
        imgids.append(twit_resp['media_id'])

    client.update_status('LOVE THESE RANDOM IMAGES', media_ids=imgids)





One of the big challenges in bot-making is thinking about everything before the actual action. This includes preparing the data that fuels the tweets:

https://www.engadget.com/2017/02/13/uk-bookstore-tweets-entire-harry-potter-novel-at-piers-morgan/

https://twitter.com/Biggreenbooks/status/832302666130788353


.. raw:: html

    <blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">.<a href="https://twitter.com/piersmorgan">@piersmorgan</a> They didn&#39;t stop to eat or drink all day. By nightfall Dudley was howling. 682/32567</p>&mdash; Big Green Bookshop (@Biggreenbooks) <a href="https://twitter.com/Biggreenbooks/status/832302666130788353">February 16, 2017</a></blockquote>
    <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>



.. code-block:: python

    import textwrap
    from time import sleep
    from random import random
    from twython import Twython


    def get_text():
        resp = requests.get('http://stash.compciv.org/2017/us-constitution.txt')
        return resp.text


    def chunk_text(the_text, maxchars=90):
        return textwrap.wrap(the_text, width=maxchars, break_long_words=False)


    def make_tweet(txt_chunk, screen_name, current_step, total_steps):
        t = "@{screen_name} ...{text}... [{x}/{y}]"
        return t.format(screen_name=screen_name,
            text=txt_chunk,
            x=current_step,
            y=total_steps)

    # gather up the tweets
    chunks = chunk_text(get_text())
    total_chunks = len(chunks)
    i = 0
    tweets = []
    for chunk in chunks:
        i += 1
        t = make_tweet(chunk, 'realdonaldtrump', i, total_chunks)
        tweets.append(t)



    # send em out
    for t in tweets:
        client.update_status(status=t)
        print("Sent:", t)
        sleep(random() * 2)


More tasks
==========

- Get a list of 200 of your most recent followers


- Sort them by most followers, and print out their names and follower counts



.. code-block:: python

    r = client.get_followers_list(count=200)
    ylist = sorted(r['users'], key=lambda x: x['followers_count'], reverse=True)


    for y in ylist:
        print(y['screen_name'], y['followers_count'], y['following'])

