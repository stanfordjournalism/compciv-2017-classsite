import requests
import sys

BASE_ENDPOINT = 'https://search.mapzen.com/v1/search'

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



if __name__ == '__main__':
    args = sys.argv

    if len(args) > 2:
        apikey = args[1]
        location = args[2]
        url = make_url(apikey, location)
        print(url)

    else:
        print('Not enough arguments')
        print('Expected usage:')
        print(""" $ python delta_url_maker.py YOUR_API_KEY 'Stanford University""")
