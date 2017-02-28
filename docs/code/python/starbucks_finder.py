"""
starbucks_locations.py

Stashed cache:
http://stash.compciv.org/2017/starbucks-locations.csv

Source data URL:
https://opendata.socrata.com/api/views/xy4y-c4mk/rows.csv?accessType=DOWNLOAD

Source landing page:
https://opendata.socrata.com/Business/All-Starbucks-Locations-in-the-World/xy4y-c4mk
"""


import requests
from csv import DictReader
from os.path import exists, join
from os import makedirs

SRC_DATA_URL = 'http://stash.compciv.org/2017/starbucks-locations.csv'
LOCAL_DATA_DIR = 'datastash'
LOCAL_DATA_PATH = join(LOCAL_DATA_DIR, 'starbucks-locations.csv')

def fetch_and_save_from_data_source():
    """
    Checks to see if LOCAL_DATA_PATH exists
    - if so, then do nothing
    - if not, then:
        - download from SRC_DATA_URL
        - save to LOCAL_DATA_PATH


    Return value:
        This function does not return a value
    """

    if exists(LOCAL_DATA_DIR):
        pass # i.e. do nothing
    else:
        print(LOCAL_DATA_DIR, "doesn't exist, so downloading it for first time...")
        # make sure the specified data directory exists if it doesn't already
        makedirs(LOCAL_DATA_DIR, exist_ok=True)
        # download the data
        resp = requests.get(SRC_DATA_URL)
        # assuming download is successful, write response as bytes
        # to LOCAL_DATA_PATH
        with open(LOCAL_DATA_PATH, 'wb') as f:
            print("Saving to:", LOCAL_DATA_PATH)
            f.write(resp.content)
    # all done...



def read_and_parse_data():
    """
    Runs: fetch_and_save_from_data_source()

    Assumes LOCAL_DATA_PATH points to file containing
      the raw data as CSV.

    Reads LOCAL_DATA_PATH and deserializes into a list
      of dictionary using csv.DictReader

    Return value:
        A list (of dictionaries)

    """
    fetch_and_save_from_data_source()
    f = open(LOCAL_DATA_PATH, 'r')
    datarecords = list(DictReader(f))
    f.close()

    return datarecords


def is_object_valid(obj):
    """
    `obj` is a dictionary, ostensibly a single record as deserialized from
       the raw data

    This function encapsulates the logic of whether the object is "valid",
      that is, whether it has the minimum data values needed to be "useful".

    For the most part, this means checking whether it has a valid/existing
      latitude and longitude value

    Return value:
        A boolean, i.e. either True or False

    """
    latstr = obj.get('Latitude')
    lngstr = obj.get('Longitude')

    if latstr and lngstr:
        return True
    else:
        return False

def wrangle_object(obj):
    """
    `obj` is a dictionary, ostensibly the representation of a single
      record from the raw data

    `obj` is assumed to be a "valid" object to be wrangled, i.e has the
       minimum fields needed to produce a worthwhile record

    Return value:
        A dictionary

        The returned dictionary is a new object derived
          from the "raw" obj. Think of it as a "standardized"
          version of the raw data dict, with the keys:

          latitude, longitude, location, details

        e.g.

        {
            'latitude': 99.999,
            'longitude': -42.0123,
            'location': 'Some human readable string describing location',
            'details': {
                 'extra': 'human-readable strings',
                 'specific: 'to this data object'
            }
        }

        (note that the "details" key should, at the very least point,
         to an empty dictionary)
    """
    wrangled_obj = {}
    wrangled_obj['details'] = {}
    # standard data fields
    wrangled_obj['latitude'] = float(obj['Latitude'])
    wrangled_obj['longitude'] = float(obj['Longitude'])

    locparts = [obj['Street Combined'], obj['City'],
                obj['Country Subdivision'], obj['Country']]

    wrangled_obj['location'] = " ".join(locparts)

    # extra details specific to Starbucks locations
    detailsobj = {}
    detailsobj['Phone'] = obj['Phone Number']

    # add details dict to the dict that we intend to return
    wrangled_obj['details'] = detailsobj

    return wrangled_obj



def produce_records():
    """
    A convenient wrapper function that runs all of the other functions
      in this file, to do the following:

    - Downloads the source data file if it isn't already downloaded
    - Parses it
    - Runs `wrangle_data_object` on each row of the raw data to
       produce a filtered, more usable version of the data

    Return value:
        A list (of dictionaries)
    """

    fetch_and_save_from_data_source()
    raw_records = read_and_parse_data()
    final_records = []
    for r in raw_records:
        if is_object_valid(r):
            x = wrangle_object(r)
            final_records.append(x)
        else:
            pass # we just skip any records that aren't valid

    return final_records




def default_foo():
    """
    Just a wrapper for the boring, default functionality
        if this script is executed from the command-line instead
        of imported as a module, e.g.

    $ python starbucks_finder.py

    Return value:
      Nothing
    """

    records = produce_records()
    print("There are", len(records), "produced records.")
    print("-----")
    print("Here is the first record:")
    print("")
    print(records[0])


if __name__ == '__main__':
    default_foo()



