from math import radians, cos, sin, asin, sqrt
RADIUS_OF_EARTH_KM = 6371

def calculate_distance(x_longitude, x_latitude, y_longitude, y_latitude):
    """
    Arguments:
        `x_longitude` and `x_latitude` are floats representing
            decimal coordinates for a starting point, x

        `y_longitude` and `y_latitude` are floats representing
            decimal coordinates for a destination point, y

    Behavior:
        Uses Haversine function, adopted from here:
        http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points


    Return value:
        A float, representing the distance between x and y in kilometers,
          rounded to the nearest 2 decimal places

    """
    # convert the decimal coordinates to degrees
    x_lon = radians(x_longitude)
    x_lat = radians(x_latitude)
    y_lon = radians(y_longitude)
    y_lat = radians(y_latitude)

    # calculate difference in longitude and latitudes
    diff_lon = y_lon - x_lon
    diff_lat = y_lat - x_lat

    # Haversine time
    a = (sin(diff_lat / 2) ** 2) + (cos(x_lat) * cos(x_lon) * sin(diff_lon / 2) ** 2)
    c = 2 * asin(sqrt(a))

    return c * RADIUS_OF_EARTH_KM

