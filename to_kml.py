# creates the KML file
def template(markers): 
  return f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>test5.kml</name>
	<StyleMap id="m_ylw-pushpin">
		<Pair>
			<key>normal</key>
			<styleUrl>#s_ylw-pushpin</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#s_ylw-pushpin_hl</styleUrl>
		</Pair>
	</StyleMap>
	<Style id="s_ylw-pushpin">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
	<Style id="s_ylw-pushpin_hl">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
  f{markers}
</Document>
</kml>
'''

#creates a single marker
def create_marker(attributes):
  return f'''
    <Placemark>
      <name>Untitled Placemark</name>
      <LookAt>
        <longitude>{attributes['lon']}</longitude>
        <latitude>{attributes['lat']}</latitude>
        <altitude>0</altitude>
        <heading>-0.03339063639233215</heading>
        <tilt>0</tilt>
        <range>23947.66089891575</range>
        <gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>
      </LookAt>
      <styleUrl>#m_ylw-pushpin</styleUrl>
      <Point>
        <gx:drawOrder>1</gx:drawOrder>
        <coordinates>{attributes['lon']},{attributes['lat']},0</coordinates>
      </Point>
      <atom:link rel="app" href="https://www.google.com/earth/about/versions/#earth-pro" title="Google Earth Pro 7.3.6.10201"></atom:link>
    </Placemark>
  '''