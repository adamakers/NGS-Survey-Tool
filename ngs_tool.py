import requests, to_kml

ngs_monuments = ''
markers = ''
count = 0
# user_lat = input('Enter a latitude for the area: ')
# user_lon = input('Enter a longitude for the area: ')
# user_rad = input('Enter a radius for the area: ')

user_lat = '38.921944'
user_lon = '-104.754167'
user_rad = '10'

api_url_rad = f'https://geodesy.noaa.gov/api/nde/radial?lat={user_lat}&lon={user_lon}&radius={user_rad}'

response = requests.get(api_url_rad)

if response.status_code == 200:
    data = response.json()
    print('Data has been recieved')
    ngs_monuments = data;
    print('Monuments gathered')
else:
    print(f'Error downloading data.  See error: {response.status_code}')

for mon in ngs_monuments:
    count += 1
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

print(f'{count} monuments gathered and recorded')

with open('test.kml', 'w') as f:
    f.write(to_kml.template(markers))


#information that is needed
# pid
# name
# stCounty
# lat
# lon
# vertDatum
# vertSource
# posSource
# condition
# setting
# string for url https://geodesy.noaa.gov/datasheets/passive-marks/index.html?PID={}


##TODO:
#### different symbols for different types of desireable points
    #dictionary matching the marker?

#### add input to determine what level of accuracy
### Convert DMS to decimal



