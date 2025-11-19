# create a Style element to create an id of what an icon should be.  reference that ID in the placemark.  similar to HTML and css

# creates the KML file
def template(markers):
  return f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
    <Document>
        <name>test.kml</name>

         <Style id="redPushpin">
            <IconStyle>
                <scale>1.2</scale>
                <Icon>
                    <href>http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png</href>
                </Icon>
            </IconStyle>
            <LabelStyle>
                <scale>1.3</scale>
            </LabelStyle>
        </Style>
        
        <Style id="greenCircle">
            <IconStyle>
                <scale>1.1</scale>
                <Icon>
                    <href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href>
                </Icon>
            </IconStyle>
            <LabelStyle>
                <scale>1.1</scale>
            </LabelStyle>
        </Style>
                
        <Style id="blueStar">
            <IconStyle>
                <scale>1.2</scale>
                <Icon>
                    <href>http://maps.google.com/mapfiles/kml/shapes/star.png</href>
                </Icon>
            </IconStyle>
            <LabelStyle>
                <scale>1.0</scale>
            </LabelStyle>
        </Style>

        <Style id="yellowSquare">
            <IconStyle>
                <scale>1.1</scale>
                <Icon>
                    <href>http://maps.google.com/mapfiles/kml/shapes/square.png</href>
                </Icon>
            </IconStyle>
            <LabelStyle>
                <scale>1.0</scale>
            </LabelStyle>
        </Style>

        <Style id="purpleDiamond">
            <IconStyle>
                <scale>1.1</scale>
                <Icon>
                    <href>http://maps.google.com/mapfiles/kml/shapes/placemark_diamond.png</href>
                </Icon>
            </IconStyle>
            <LabelStyle>
                <scale>1.1</scale>
            </LabelStyle>
        </Style>


        {markers}
    </Document>
</kml>
'''

def markerStyle():
   return '''
            <Style>
                <IconStyle>
                    <Icon>
                        <href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href>
                    </Icon>
                </IconStyle>
            </Style>
'''

#creates a single marker
def create_marker(attributes):
    return f'''
        <Placemark>
            <name>{attributes['pid']}</name>
            <styleUrl>#redPushpin</styleUrl>
            <description>
                stCounty: {attributes['stCounty']}<br/>
                vertDatum: {attributes['vertDatum']}<br/>
                vertSource: {attributes['vertSource']}<br/>
                condition: {attributes['condition']}<br/>
                setting: {attributes['setting']}<br/>
                View link below in web browser and not Firefox
                URL: https://geodesy.noaa.gov/datasheets/passive-marks/index.html?PID={attributes['pid']}
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