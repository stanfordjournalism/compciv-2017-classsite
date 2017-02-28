BASE_ENDPOINT = 'https://search.mapzen.com/v1/search'
BASE_QUERY_STRING = 'api_key={apikey}&text={loc}'

def sanitize_text(txt):
    """
    Arguments:

        txt: a String, e.g. "Stanford University"

    Return value:

        a String that has been "sanitized" and ready to insert into a URL

        e.g. 'Stanford+University'
    """
    return txt.replace(' ', '+')


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

    loctxt = sanitize_text(location_name)
    query_string = BASE_QUERY_STRING.format(apikey=api_key, loc=loctxt)
    mapzen_url = BASE_ENDPOINT + '?' + query_string

    return mapzen_url



if __name__ == '__main__':
    xkey = 'dummy-key'
    xloc = 'Stanford University'

    url = make_url(xkey, xloc)

    print(url)



