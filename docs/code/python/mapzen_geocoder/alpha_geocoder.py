import requests
import sys

BASE_ENDPOINT = 'https://search.mapzen.com/v1/search'

def make_url(api_key, location_name):
    """
    Arguments:

        api_key: String, the Mapzen API key you get during registration
                e.g. 'search-blah'

        location_name: String, represents the human-readable name of the location to geocode
                e.g. 'Stanford University'

    Returns:

        String, a url formatted according to Mapzen Search API spec:

        e.g. https://search.mapzen.com/v1/search?api_key=search-blah&text=Stanford+University

    """
    my_params = {'text': location_name, 'api_key': api_key}
    p = requests.PreparedRequest()
    p.prepare_url(url=BASE_ENDPOINT, params=my_params)

    return p.url


def get_best_geocoded_result(data):
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



def geocode(apikey, location):

