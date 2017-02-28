import requests
import json

DEFAULT_DATA_URL = 'http://stash.compciv.org/2017/mapzen-search-stanford-university-single.json'

def get_data_and_extract_best_coordinates(url):
    """
    returns a dictionary with keypairs for 'latitude' and 'longitude'
    """

    resp = requests.get(url)
    data = json.loads(resp.text)

    features = data['features']
    best_feature = features[0] # this will break if features is empty
    coords = best_feature['geometry']['coordinates']
    lng = coords[0]
    lat = coords[1]

    return {'latitude': lat, 'longitude': lng}




if __name__ == '__main__':
    coords = get_data_and_extract_best_coordinates(DEFAULT_DATA_URL)

    print('Latitude:', coords['latitude'])
    print('Longitude:', coords['longitude'])

