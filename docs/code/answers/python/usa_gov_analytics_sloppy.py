import csv
import requests
from os.path import basename, exists, join
from os import makedirs


DEST_DIR = 'data-files'


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



def foo_1():
    """
    Read the list of top traffic sources in the past 30 days to federal websites:
    http://stash.compciv.org/2017/analytics.usa.gov-top-traffic-sources-30-days.csv

    Return a dictionary that lists number of total visits by these facets:
        total_vists, total_pageview, source_count

    Expected answer:
    {'source_count': 20, 'total_pageviews': 1864771726, 'total_visits': 725573027}

    """
    srcurl = 'http://stash.compciv.org/2017/analytics.usa.gov-top-traffic-sources-30-days.csv'
    src_data_filename = fetch_and_save_url(srcurl)

    # very verbose way to serialize as CSV
    thefile = open(src_data_filename, 'r')
    lines = thefile.read().splitlines()
    thefile.close()
    thecsv = csv.DictReader(lines)
    records = list(thecsv)

    total_visits = 0
    for row in records:
        total_visits += int(row['visits'])

    return total_visits


def foo_2():
    """
    Read the list of top traffic sources in the past 30 days to federal websites:
    http://stash.compciv.org/2017/analytics.usa.gov-top-traffic-sources-30-days.csv

    Return a dictionary that lists number of total visits by these facets:
        total_vists, total_pageview, source_count

    Expected answer:
    {'source_count': 20, 'total_pageviews': 1864771726, 'total_visits': 725573027}

    """
    srcurl = 'http://stash.compciv.org/2017/analytics.usa.gov-top-traffic-sources-30-days.csv'
    src_data_filename = fetch_and_save_url(srcurl)

    # very verbose way to serialize as CSV
    thefile = open(src_data_filename, 'r')
    lines = thefile.read().splitlines()
    thefile.close()
    thecsv = csv.DictReader(lines)
    records = list(thecsv)

    d = {}
    d['source_count'] = len(records)
    d['total_pageviews'] = 0
    d['total_visits'] = 0
    for row in records:
        d['total_pageviews'] += int(row['pageviews'])
        d['total_visits'] += int(row['visits'])

    return d



def foo_3():
    """
    Read the list of top traffic sources in the past 30 days to federal websites:
    http://stash.compciv.org/2017/analytics.usa.gov-top-traffic-sources-30-days.csv

    Return a dictionary that lists number of total visits by these facets:
        social, direct, search, total

    Expected answer:

    {'direct': 208516971,
     'search': 355065438,
     'social': 11994983,
     'total': 725573027}

    """
    srcurl = 'http://stash.compciv.org/2017/analytics.usa.gov-top-traffic-sources-30-days.csv'
    src_data_filename = fetch_and_save_url(srcurl)

    # less verbose way to serialize as CSV
    thefile = open(src_data_filename, 'r')
    thecsv = csv.DictReader(thefile.read().splitlines())
    thefile.close()
    records = list(thecsv)

    d = {}
    d['total'] = sum(int(r['visits']) for r in records)
    d['direct'] = next(int(r['visits']) for r in records if r['source'] == '(direct)')
    d['search'] = sum(int(r['visits']) for r in records if r['source'] in ('google', 'bing', 'yahoo'))
    d['social'] = sum(int(r['visits']) for r in records if r['has_social_referral'] == 'Yes')

    return d



def foo_4():
    """
    Return dict representing number of visits as a percentage of the total visits

    Actual answer:

    {'direct_pct': 28.7,
     'search_pct': 48.9,
     'social_pct': 1.7,
     'total_visits': 725573027}

    """
    srcurl = 'http://stash.compciv.org/2017/analytics.usa.gov-top-traffic-sources-30-days.csv'
    src_data_filename = fetch_and_save_url(srcurl)

    # using the ``with`` block to more concisely open/close file objects
    with open(src_data_filename, 'r') as thefile:
        lines = thefile.read().splitlines()
        records = list(csv.DictReader(lines))

    d = {}
    d['total_visits'] = sum(int(r['visits']) for r in records)

    d['direct_pct'] = round(100 * next(int(r['visits']) for r in records if r['source'] == '(direct)') / d['total_visits'], 1)
    d['search_pct'] = round(100 * sum(int(r['visits']) for r in records if r['source'] in ('google', 'bing', 'yahoo')) / d['total_visits'], 1)
    d['social_pct'] = round(100 * sum(int(r['visits']) for r in records if r['has_social_referral'] == 'Yes') / d['total_visits'], 1 )

    return d




def foo_5():
    """
    Return list of lists, with header, and each list showing the source name, visits as percentage of total visits, and pageviews vs visits (2 decimal places)

    First five rows of expected list:

    [['source', 'pct_of_total_visits', 'pageviews_per_visit'],
     ['google', 43.38, 2.41],
     ['(direct)', 28.74, 2.78],
     ['usps.com', 4.45, 2.5],
     ['bing', 3.77, 3.4],
     ['weather.gov', 2.69, 2.12],
     ['irs.gov', 2.37, 3.5],
     ['yahoo', 1.79, 2.59],
     # ...]
    """

    srcurl = 'http://stash.compciv.org/2017/analytics.usa.gov-top-traffic-sources-30-days.csv'
    src_data_filename = fetch_and_save_url(srcurl)
    # trying to cram everything into one line
    with open(src_data_filename, 'r') as thefile:
        records = list(csv.DictReader(thefile.read().splitlines()))


    thelist = []
    thelist.append(['source', 'pct_of_total_visits', 'pageviews_per_visit'])

    total_visits = sum(int(r['visits']) for r in records)

    for row in records:
        x = []
        thelist.append(x)

        x.append(row['source'])
        pct_visits = round((100 * int(row['visits']) / total_visits), 2)
        x.append(pct_visits)
        page_per_visit = round(int(row['pageviews'])  / int(row['visits']), 2)
        x.append(page_per_visit)

    return thelist



def foo_assertions():
    assert foo_1() == 725573027, "Expect foo_1() to return integer value equal to exactly 725573027"

    r = foo_2()
    assert type(r) == dict, 'Expect foo_2() to return a dictionary'
    assert r['source_count'] == 20, "Expect 'source_count' to be 20"
    assert r['total_pageviews'] == 1864771726, "Expect 'total_pageviews' to be 1864771726"

    r = foo_3()
    assert r['search'] == 355065438, "Expect 'search' sources to have 355065438 visits"
    assert r['social'] == 11994983, "Expect 'social' sources to have 11994983 visits"

    r = foo_4()
    assert r['search_pct'] == 48.9, "Expect 'search' sources to make 48.9 percent of total visits"

    r = foo_5()
    assert type(r) is list, 'Expect foo_5() to return a list'
    assert r[0] == ['source', 'pct_of_total_visits', 'pageviews_per_visit'], 'Expect header rows to have specified keys and order'
    assert r[1][0] == 'google', "Expect first row, first col to equal 'google'"
    assert r[1][1] == 43.38, "Expect first row, 2nd col to equal 43.38"
    assert r[10] == ['login.usajobs.gov', 1.54, 5.37], 'Expect 10th row to contain data for login.usajobs.gov source'


if __name__ == '__main__':

    foo_assertions()

    print("Done running assertions!")
