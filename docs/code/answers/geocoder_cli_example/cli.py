from argparse import ArgumentParser
from geocoder import geocode
import json


if __name__ == '__main__':
    parser = ArgumentParser(description='Use Mapzen to geocode a location')

    parser.add_argument('location', type=str,
                           help='A human-readable description of your location/address')

    parser.add_argument('api_key', type=str, help='Your Mapzen API key')

    args = parser.parse_args()

    mapzen_result = geocode(api_key=args.api_key, location_name=args.location)

    if not mapzen_result:
        print("Sorry, could not geocode the location:", args.location)
    else:
        # print dictionary as a prettified JSON
        txt = json.dumps(mapzen_result, indent=2)
        print(txt)
