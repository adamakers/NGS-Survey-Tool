import requests, json

## test coords
# N385226.67 W1044741.62

## official test request
#https://geodesy.noaa.gov/api/nde/radial?lat=38.954775&lon=-104.885727&radius=10.5

ngs_monuments = ''

hard_min_lat = '38.914018'
hard_max_lat = '38.954775'
hard_min_lon = '-104.821406'
hard_max_lon = '-104.885727'

api_url = 'https://geodesy.noaa.gov/api/nde/radial?lat=38.954775&lon=-104.885727&radius=10.5'

response = requests.get(api_url)

if response.status_code == 200:
  data = response.json()
  print('Data has been recieved')
  ngs_monuments = data;
  print(ngs_monuments[0])
else:
  print(f'Error downloading data.  See error: {response.status_code}')


