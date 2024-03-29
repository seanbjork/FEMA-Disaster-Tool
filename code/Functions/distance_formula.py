# Distance between to latitude and longitude points
# Haversine formula example in Python
# Author: Wayne Dyck

def distance(origin, destination):
    """ Takes in two (lat,long) tuples and returns the distance in kilometers between them. """

    import math

    lat1, lon1 = origin
    lat2, lon2 = destination
    #radius = 3959 # miles
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d
