from requests import PreparedRequest
from argparse import ArgumentParser

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

        String
        A url formatted according to Mapzen Search API spec.

        e.g. https://search.mapzen.com/v1/search?api_key=MY_API_KEY&text=Stanford+University

    """
    my_params = {'text': location_name, 'api_key': api_key}
    p = PreparedRequest()
    p.prepare_url(url=BASE_ENDPOINT, params=my_params)

    return p.url



if __name__ == '__main__':
    parser = ArgumentParser(description='Make a Mapzen Search URL')
    parser.add_argument('apikey', type=str,
                         help='Mapzen Search API key')
    parser.add_argument('location', type=str,
                         help="The (human-readable) name of the location to geocode")

    args = parser.parse_args()
    url = make_url(args.apikey, args.location)
    print(url)

