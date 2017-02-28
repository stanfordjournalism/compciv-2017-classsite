import requests
import json

DEFAULT_DATA_URL = 'http://stash.compciv.org/2017/mapzen-search-stanford-university-single.json'


def get_and_parse_response(url):
    resp = requests.get(url)
    return json.loads(resp.text)

def get_best_geocoded_result(data):
    """
    Arguments:

        data:
          Dictionary
          The data object from Mapzen's API result, after the
             raw text as been parsed and deserialized

    Returns:

        Dictionary or NoneType (None)
        If data object does not have any geocoded results, returns None

        Else, return a dictionary that represents the most relevant
          geocoded result, trimmed to its most useful fields:

           {'longitude': 99, 'latitude': -42,
            'label': 'Le Big Mac, France',
            'confidence': 0.7,
            'country': 'France',
            'region': 'Sacre Bleu',
            'county': 'Fromage'}

    """

    features = data['features']

    if len(features) == 0:
        return None
    else:
        # assuming the very first result i.e. feature is
        # the best one
        d = {}
        best_feature = features[0]

        # set coordinates
        geo = best_feature['geometry']
        d['longitude'] = geo['coordinates'][0]
        d['latitude'] = geo['coordinates'][1]

        # set other metadata
        properties = best_feature['properties']
        for att in ['label', 'confidence', 'country', 'region', 'county']:
            d[att] = properties.get(att)

        return d


if __name__ == '__main__':
    data = get_and_parse_response(DEFAULT_DATA_URL)
    result = get_best_geocoded_result(data)
    serialized_result = json.dumps(result, indent=2)

    print(serialized_result)
