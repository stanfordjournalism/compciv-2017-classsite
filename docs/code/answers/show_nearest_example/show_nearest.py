from argparse import ArgumentParser
from geocoder import geocode
from wrangle_quakes import wrangle_data





if __name__ == '__main__':
    parser = ArgumentParser(description='Find the nearest earthquakes and Starbucks near you')
    parser.add_argument('location', type='str',
                         help='A human-readable description of your location/address')

    parser.add_argument('api_key', type='str',
                         help='Your Mapzen API key')


    args = parser.parse_args()

    print("Location to geocode:", args.location)


