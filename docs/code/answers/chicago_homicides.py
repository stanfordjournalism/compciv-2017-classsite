import requests
import csv
from collections import Counter, defaultdict
from datetime import datetime

# https://data.cityofchicago.org/Public-Safety/Homicides/iyvd-p5ga/data
# https://data.cityofchicago.org/api/views/iyvd-p5ga/rows.csv?accessType=DOWNLOAD


url = 'https://data.cityofchicago.org/api/views/iyvd-p5ga/rows.csv?accessType=DOWNLOAD'

import csv
import requests
from os.path import basename, exists, join
from os import makedirs

DEST_DIR = 'data-files'
DATA_URL = 'http://stash.compciv.org/2017/chicago-homicides.csv'

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


def get_and_parse_data():
    dname = fetch_and_save_url(DATA_URL)
    with open(dname, 'r') as f:
        records = list(csv.DictReader(f))
        return records


def foo_1():
    """
    Return the total count of homicides

    """
    records = get_and_parse_data()
    return(len(records))
    # returns 8282


def foo_2():
#   {'false': 4284, 'true': 3998, 'rate': 48.3}
    records = get_and_parse_data()
    d = dict(Counter(r['Arrest'] for r in records))
    d['rate'] = round(100 * d['true'] / len(records), 1)
    return d


def foo_3():
    records = get_and_parse_data()
    yrcount = Counter(r['Year'] for r in records)
    mylist = []
    mylist.append(['year', 'count'])
    mylist.extend(list(k) for k in sorted(yrcount.items()))

    return mylist



def foo_4():
    records = get_and_parse_data()
    seasons_count = {'fall': 0, 'winter': 0, 'summer': 0, 'spring': 0}

    for r in records:
        mth = int(r['Date'][0:2])
        if mth in [9, 10, 11]:
            season = 'fall'
        elif mth in [12, 1, 2]:
            season = 'winter'
        elif mth in [3, 4, 5]:
            season = 'spring'
        elif mth in [6, 7, 8]:
            season = 'summer'

        seasons_count[season] += 1

    # Expected result
    # {'fall': 2168, 'spring': 1931, 'summer': 2591, 'winter': 1592}
    return seasons_count



def foo_5():
    """
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

           {'Friday': 1091,
             'Monday': 1115,
             'Saturday': 1461,
             'Sunday': 1457,
             'Thursday': 1083,
             'Tuesday': 1044,
             'Wednesday': 1031})

    """
    records = get_and_parse_data()
    d = defaultdict(int)
    for r in records:
        datestr = r['Date'].split(' ')[0]
        dt = datetime.strptime(datestr, '%m/%d/%Y')
        dayname = dt.strftime('%A')
        d[dayname] += 1
    return dict(d)



def foo_assertions():
    r = foo_1()
    assert type(r) is int, 'Assert foo_1() returns an integer'
    assert r == 8282, 'Expect total number of homicides in foo_1() to be equal to 8282'

    r = foo_2()
    assert type(r) is dict, 'Assert foo_2() returns dictionary'
    assert r['true'] == 3998, 'Assert foo_2() shows 3,998 arrests made in homicide cases'
    assert r['false'] == 4284, 'Assert foo_2() shows arrests not made in 4284 homicide cases'
    assert r['rate'] == 48.3, 'Assert foo_2() is equal to homicide arrest rate to be 48.3'


    r = foo_3()
    assert type(r) is list, 'Assert foo_3() returns list'
    assert r[0] == ['year', 'count'], 'Expect first row of foo_3() to be two column list: year, count'
    assert len(r[1:]) == 17, 'Expect total number of records (i.e. not the header row) to be 17'
    assert r[1][0] == '2001', "Expect earliest year to be '2001'"
    assert r[-1] == ['2017', 53], "Expect last row to be for year '2017' with a partial count of homicides"


    r = foo_4()
    assert type(r) is dict, 'Assert foo_4() returns dict'
    assert sorted(r.keys()) == ['fall', 'spring', 'summer', 'winter'], 'Expect four seasons, fall, spring, summer, winter'
    assert r['fall'] == 2168 , 'Expect fall to have had 2,168 homicides'
    assert r['summer'] > r['fall'], 'Expect summer to have more homicides than the fall'


    r = foo_5()
    assert type(r) is dict, 'Assert foo_5() returns dict'
    assert len(r.keys()) == 7, 'Assert 7 days in the week'
    # list of obj, sorted by most homicides per day
    mostdeaths = sorted(r.items(), key=lambda x: x[-1], reverse=True)
    assert mostdeaths[0] == ('Saturday', 1461), 'Assert that most homicides are reported on Saturday'


if __name__ == '__main__':
    foo_assertions()
    print("Done with assertions!")
