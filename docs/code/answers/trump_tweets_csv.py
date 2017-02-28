import csv
import requests
from os.path import basename, exists, join
from os import makedirs
SRC_URL_BASE = 'http://stash.compciv.org/2017/{}-tweets.csv'
DATA_DIR = 'data-files'

def make_url(sname):
    return SRC_URL_BASE.format(sname)


def make_filename_from_url(url):
    bname = basename(url)
    return join(DATA_DIR, bname)


def fetch_tweets(tname):
    makedirs(DATA_DIR, exist_ok=True)
    url = make_url(tname)
    destname = make_filename_from_url(url)

    if not exists(destname):
        resp = requests.get(url)
        with open(destname, 'wb') as f:
            f.write(resp.content)


def read_tweets(tname):
    """
    returns a list of dicts of tweets for a given twitter name
    """
    fetch_tweets(tname)
    fname = make_filename_from_url(make_url(tname))
    with open(fname, 'r') as f:
        tweets = list(csv.DictReader(f))
        return tweets


def foo_1():
    total = 0
    total = len(read_tweets('realdonaldtrump'))
    return total


def foo_2():
    d = {}
    tcount = 0
    tweets = read_tweets('realdonaldtrump')
    for t in tweets:
        if t['Posted at'] >= '2016-11-09':
            tcount += 1

    d['realdonaldtrump'] = tcount
    return d



def foo_3():
    d = {}
    screenname = 'realdonaldtrump'
    tweets = read_tweets(screenname)
    before_count = 0
    after_count = 0
    for t in tweets:
        if t['Posted at'] >= '2016-11-09' and t['Posted at'] <= '2016-11-16':
            after_count += 1
        elif t['Posted at'] >= '2016-11-01' and t['Posted at'] <= '2016-11-08':
            before_count += 1

    d[screenname] = {'before': before_count, 'after': after_count}
    return d



def foo_4():
    tweetmonths = {}
    screenname = 'realdonaldtrump'
    tweets = read_tweets(screenname)
    for t in tweets:
        month = t['Posted at'][0:7]
        if tweetmonths.get(month):
            tweetmonths[month] += 1
        else:
            tweetmonths[month] = 1
    return [('month', 'count')] + sorted(tweetmonths.items())



def foo_5():
    data = []
    screenname = 'realdonaldtrump'

    tweetmonths = {}
    tweets = read_tweets(screenname)
    for t in tweets:
        month = t['Posted at'][0:7]
        if tweetmonths.get(month):
            tweetmonths[month] += 1
        else:
            tweetmonths[month] = 1


    for row in tweetmonths.items():
        month = row[0]
        tcount = row[1]
        x = (screenname, month, tcount)
        data.append(x)

    return [('screen_name', 'month', 'count')] + sorted(data)


def foo_assertions():
    assert type(foo_1()) == int
    assert foo_1() == 3200

    assert type(foo_2()) == dict
    assert foo_2() == {'realdonaldtrump': 529}

    assert type(foo_3()) == dict
    assert list(foo_3().keys())[0] == 'realdonaldtrump'
    assert list(foo_3().values())[0] ==  {'after': 20, 'before': 83}

    assert type(foo_4()) == list
    assert type(foo_4()[0]) == tuple
    assert foo_4()[0] == ('month', 'count')
    assert foo_4()[1] == ('2016-03', 167)
    assert foo_4()[-1] == ('2017-02', 87)


    assert type(foo_5()) == list
    assert type(foo_5()[0]) == tuple
    assert foo_5()[0] == ('screen_name', 'month', 'count')
    assert foo_5()[1] == ('realdonaldtrump', '2016-03', 167)
    assert foo_5()[-1] == ('realdonaldtrump','2017-02', 87)



if __name__ == '__main__':
    foo_assertions()
    print("Done running assertions!")


