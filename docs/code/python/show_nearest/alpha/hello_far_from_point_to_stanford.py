import argparse
from geo_utils import calculate_distance

STANFORD_LATITUDE =
STANFORD_LONGITUDE =


def calculate_distance_from_stanford(ref_longitude, ref_latitude):
    """
    Arguments:
       `records` is a list of dictionaries with `latitude` and `longitude` keypairs

        `ref_longitude` is a float representing the longitude coordinate of
            reference point

        `ref_latitude` is a float representing the latitude coordinate of
            reference point

    Return value:
        A list (of tuples), e.g.

            [
                (12.45, {'location': 'Somewhere', 'latitude': 55, 'longitude': -42}),
                (555.01, {'location': 'Elsewhere', 'latitude': -2, 'longitude': -82}),
            ]


        The first value of the tuple-pair is:
            a Float: the calculated distance of the record to the reference point
        The second value is:
            a dict: the record from which the distance was calculated
    """

    # this is an internal function in which we use to wrap up
    #   the work of calling calculate_distance on some object
    #   and using the ``ref_longitude`` and ``ref_latitude`` points
    #
    #  the `sorted` function's key parameter...
    #  note that this internal function
    #  "knows" about ref_longitude and ref_latitude
    def __calc_distance_from_obj(obj):
        lng = obj['longitude']
        lat = obj['latitude']
        return calculate_distance(lng, lat, ref_longitude, ref_latitude)



    s_records = sorted(records, key=__calc_distance_from_obj)
    return s_records

