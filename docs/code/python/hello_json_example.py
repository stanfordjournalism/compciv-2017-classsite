import json
import requests
from os.path import basename, exists, join
from os import makedirs

DEST_DIR = 'data-files'

DATA_URL = 'http://stash.compciv.org/2017/helloworld.json'

def fetch_and_save_url(url):
    """
    For a given URL, creates a filename to save to
    Checks to see if filename already exists; if not, download and save to that file name

    Either way, return the filename as a string
    """
    makedirs(DEST_DIR, exist_ok=True)
    dest_filename = join(DEST_DIR, basename(url))
    if not exists(dest_filename):
        resp = requests.get(url)
        with open(dest_filename, 'wb') as f:
            f.write(resp.content)
    return dest_filename


def parse_data():
    fname = fetch_and_save_url(DATA_URL)
    thefile = open(fname, 'r')
    rawtxt = thefile.read()
    thefile.close()

    return json.loads(rawtxt)


def foo_1():
    jdata = parse_data()
    return jdata['status']


def foo_2():
    jdata = parse_data()
    items = jdata['inventory']
    return len(items)


def foo_3():
    jdata = parse_data()
    items = jdata['inventory']
    y = []
    for i in items:
        y.append(i['name'])

    return sorted(y)




def foo_assertions():
    x = foo_1()
    assert type(x) is str, 'Expect foo_2() to return an str'
    assert x == 'SUPER!', 'Expect the "status" key of the data to havevalue of "SUPER!"'

    x = foo_2()
    assert type(x) is int, 'Expect foo_2() should return an int'
    assert x == 5, 'foo_2() Expect that foo_2() finds that there are 5 itmes'

    x = foo_3()
    assert type(x) is list, 'Expect foo_3() should return a list'
    assert x == ['apples', 'cats', 'dogs', 'kiwis', 'zebras'], 'Expect the list of item names to be in this sorted order'



if __name__ == '__main__':
    foo_assertions()
    print("Done with assertions!")
