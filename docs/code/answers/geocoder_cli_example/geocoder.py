import requests
import json

BASE_ENDPOINT = 'https://search.mapzen.com/v1/search'

def download_and_parse_response(url):
    resp = requests.get(url)
    return json.loads(resp.text)

def make_url(api_key, location_name):
    """
    Arguments:

        api_key (String)
        The Mapzen API key you get during registration
            e.g. 'MY_API_KEY'

        location_name (String)
        Represents the human-readable name of the location to geocode
            e.g. 'Stanford University'

    Returns:

        String, a url formatted according to Mapzen Search API spec:

        e.g. https://search.mapzen.com/v1/search?api_key=MY_API_KEY&text=Stanford+University

    """
    my_params = {'text': location_name, 'api_key': api_key}
    p = requests.PreparedRequest()
    p.prepare_url(url=BASE_ENDPOINT, params=my_params)

    return p.url





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

        {'confidence': 0.945,
         'country': 'United States',
         'county': 'Santa Clara County',
         'label': 'Stanford University, Stanford, CA, USA',
         'latitude': 37.42716,
         'longitude': -122.17024,
         'region': 'California',
         'layer': 'venue'
         }
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
        for att in ['label', 'confidence', 'country', 'region', 'county', 'layer']:
            d[att] = properties.get(att)

        return d




def geocode(api_key, location_name):
    """
    Arguments:

        api_key (String)
        The key provided by the Mapzen Search API upon registration

        location_name (String)
        The human-readable name of the place to be geocoded

    Returns:

        (Dictionary) or (NoneType)
        If the Mapzen API did not return any geocoded results,
            then return None

        Else, return a dictionary representing a single geocoded result,
            and key/values for the relevant attributes, including
            'longitude', 'latitude', 'label', 'confidence'

    """
    m_url = make_url(api_key, location_name)
    m_data = download_and_parse_response(m_url)
    result = get_best_geocoded_result(m_data)

    return result
