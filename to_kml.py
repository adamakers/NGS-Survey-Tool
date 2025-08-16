# create a Style element to create an id of what an icon should be.  reference that ID in the placemark.  similar to HTML and css

# creates the KML file
def template(markers):
  return f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
    <Style id="redIcon">
        <IconStyle>
            <color>ff0000</color>
            <colorMode>normal</colorMode>
            <scale>5</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href>
            </Icon>
        </IconStyle>
    </Style>
    <name>test5.kml</name>
    {markers}
</Document>
</kml>
'''

#creates a single marker
def create_marker(attributes):
    return f'''
        <Placemark>
            <Style>
                <IconStyle>
                    <color>ff0000</color>
                    <colorMode>normal</colorMode>
                    <scale>5</scale>
                    <Icon>
                        <href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href>
                    </Icon>
                </IconStyle>
            </Style>
            <name>{attributes['pid']}</name>
            <description>
                stCounty: {attributes['stCounty']}
                vertDatum: {attributes['vertDatum']}
                vertSource: {attributes['vertSource']}
                condition: {attributes['condition']}
                setting: {attributes['setting']}
            </description>
            <LookAt>
                <longitude>{attributes['lon']}</longitude>
                <latitude>{attributes['lat']}</latitude>
                <altitude>0</altitude>
                <heading>0.0</heading>
                <tilt>0</tilt>
                <range>23947.66089891575</range>
                <gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>
            </LookAt>
            <Point>
                <gx:drawOrder>1</gx:drawOrder>
                <coordinates>{attributes['lon']},{attributes['lat']},0</coordinates>
            </Point>
            <atom:link rel="app" href="https://www.google.com/earth/about/versions/#earth-pro" title="Google Earth Pro 7.3.6.10201"></atom:link>
        </Placemark>'''