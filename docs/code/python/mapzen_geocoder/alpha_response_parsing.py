import requests
import json

SRC_URL = 'http://stash.compciv.org/2017/mapzen-search-stanford-university-single.json'


# Download and parse the data
resp = requests.get(SRC_URL)
txt = resp.text
jdata = json.loads(txt)

features = jdata['features']

best_feature = features[0]
geo = best_feature['geometry']
coords = geo['coordinates']
lng = coords[0]
lat = coords[1]


print("Longitude:", lng)
print("Latitude:", lat)












"""
requests.get(SRC_DATA_URL)
resp = json.loads(resp.text)

data = get_and_parse_data()
data.keys()

val = data['type']
type(val)
val


val = data['geocoding']
type(val)
val
val['query']


val = data['features']
type(val)
len(val)
thing = val[0]

# get geo
geo = thing['geometry']
geo.keys()

coords = geo['coordinates']
type(coords)
lng = coords[0]
lat = coords[1]


# get properties
props = thing['properties']
type(props)
props.keys()

props['confidence']
props['country']
props['country']
"""

