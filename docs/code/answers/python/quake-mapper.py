
import requests
import csv
from sys import argv

DATA_URL = 'http://stash.compciv.org/2017/usgs_quakes_significant_month.csv'

MAP_SIZE = '800x400'
BASE_MAP_URL = 'https://maps.googleapis.com/maps/api/staticmap'

def make_map_url(locations):
    """
    assume locations is a list of dicts, with 'latitude' and 'longitude'
    keys
    """
    myparams = {}
    myparams['size'] =  MAP_SIZE
    myparams['markers'] = []
    for loc in locations:
        marker = loc['latitude'] + ',' + loc['longitude']
        myparams['markers'].append(marker)

    pre_req = requests.PreparedRequest()
    pre_req.prepare_url(BASE_MAP_URL, myparams)

    return pre_req.url


def fetch_quake_data():
    resp = requests.get(DATA_URL)
    lines = resp.text.splitlines()
    return list(csv.DictReader(lines))


def sortfoo(q):
    return float(q['mag'])

def sort_quakes(records, numlimit):
    """ records should be a list of deserialized quake objects
        numlimit is how many top-quakes-by-magnitude should be returned
    """
    sortedrecs = sorted(records, key=sortfoo, reverse=True)

    return sortedrecs[0:numlimit]


if __name__ == '__main__':
    if len(argv) < 2:
        print("You must supply an argument specifying number of quakes to map")
    else:
        numquakes = argv[1] # remember that this is just a string...
        numquakes = int(numquakes)
        print('Hello user, you want this many quakes:', numquakes)
        # get the quake data
        quakes = fetch_quake_data()
        thequakes = sort_quakes(quakes, numquakes)
        url = make_map_url(thequakes)
        print(url)

