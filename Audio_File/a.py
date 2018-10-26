{
'address_components': 
	[{'long_name': '1600', 'short_name': '1600', 'types': ['street_number']}, {'long_name': 'Amphitheatre Parkway', 'short_name': 'Amphitheatre Pkwy', 'types': ['route']}, {'long_name': 'Mountain View', 'short_name': 'Mountain View', 'types': ['locality', 'political']}, {'long_name': 'Santa Clara County', 'short_name': 'Santa Clara County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'California', 'short_name': 'CA', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, {'long_name': '94043', 'short_name': '94043', 'types': ['postal_code']}], 
'formatted_address': 
	'1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA', 
'geometry': 
	{
		'location': 
			{'lat': 37.4223827, 'lng': -122.0855566}, 
			'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 37.4237316802915, 'lng': -122.0842076197085}, 'southwest': {'lat': 37.4210337197085, 'lng': -122.0869055802915}}}, 'place_id': 'ChIJ2eUgeAK6j4ARbn5u_wAGqWA', 'plus_code': {'compound_code': 'CWC7+WQ Mountain View, California, United States', 'global_code': '849VCWC7+WQ'}, 'types': ['street_address']}


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Display markers</title>
</head>
    <style>
        /* Always set the map height explicitly to define the size of the div
         * element that contains the map. */
        #map {
          height: 100%;
        }
        /* Optional: Makes the sample page fill the window. */
        html, body {
          height: 100%;
          margin: 0;
          padding: 0;
        }
    </style>
<body>
    <div id="map"></div>
    <script>
        function initMap() {
            var locations = {{address|safe}};
            var marker, i;
            console.log(locations)
            var myLatLng = {lat:locations[0]['x'], locations[0]['y']};

            var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 10,
            center: myLatLng
            });
            for (i = 0; i < locations.length; i++) { 
                marker = new google.maps.Marker({
                    position: new google.maps.LatLng(locations[i]['x'], locations[i]['y']),
                    map: map,
                    title: locations[i]['Address']
                });
            }
        }
    </script>
        <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBdl9Xvi8Yipfx-ldaB9RtluwGEyuU1KHM&callback=initMap">
        </script>
</body>
</html>