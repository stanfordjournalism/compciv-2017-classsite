import requests

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
    my_params = {}
    my_params['text'] = location_name
    my_params['api_key'] = api_key
    # let the PreparedRequest class handle the logic
    # of properly formatting the URL and its parameters:
    p = requests.PreparedRequest()
    p.prepare_url(url=BASE_ENDPOINT, params=my_params)

    return p.url

if __name__ == '__main__':
    xkey = 'dummy-key'
    xloc = 'Stanford University'
    url = make_url(xkey, xloc)

    print(url)
