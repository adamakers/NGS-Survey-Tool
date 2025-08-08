import requests, to_kml

## test coords
# N385226.67 W1044741.62

## official test request
#https://geodesy.noaa.gov/api/nde/radial?lat=38.954775&lon=-104.885727&radius=10.5

ngs_monuments = ''
markers = ''

hard_min_lat = '38.914018'
hard_max_lat = '38.954775'
hard_min_lon = '-104.821406'
hard_max_lon = '-104.885727'

api_url = 'https://geodesy.noaa.gov/api/nde/radial?lat=38.954775&lon=-104.885727&radius=3.5'

response = requests.get(api_url)

if response.status_code == 200:
  data = response.json()
  print('Data has been recieved')
  ngs_monuments = data;
  print(ngs_monuments)
else:
  print(f'Error downloading data.  See error: {response.status_code}')


for mon in ngs_monuments:
  attributes = {
    'pid': mon['pid'],
    'name': mon['name'],
    'stCounty': mon['stCounty'],
    'lat': mon['lat'],
    'lon': mon['lon'],
    'vertDatum': mon['vertDatum'],
    'vertSource': mon['vertSource'],
    'posSource': mon['posSource'],
    'condition': mon['condition'],
    'setting': mon['setting']
  }
  
  markers += to_kml.create_marker(attributes)


with open('test5.kml', 'w') as f:
  f.write(to_kml.template(markers))


#information that is needed
# pid
# name
# stCounty
# lat
# lon
# vertDatum
# verSource
# posSource
# condition
# setting
# string for url https://geodesy.noaa.gov/datasheets/passive-marks/index.html?PID={}
