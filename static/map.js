// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.

var map, infoWindow, latitude, longitude;
function initMap() {
	var initialPos = {lat: 28.621172915717676, lng: 77.21548676490784};
	map = new google.maps.Map(document.getElementById('map'), {
		center: initialPos,
		zoom: 10
	});

	infoWindow = new google.maps.InfoWindow;
	var marker = new google.maps.Marker({
		position: initialPos,
		map: map
	});

	google.maps.event.addListener(map,"click", function (event) {
		latitude = event.latLng.lat();
		longitude = event.latLng.lng();
		console.log( latitude + ', ' + longitude );
		var desiredPos = {
			lat: latitude,
			lng: longitude
		};
		//map.setCenter(desiredPos);
		marker.setPosition(desiredPos);
		document.getElementById("latitude").value=latitude;
		document.getElementById("longitude").value=longitude;
	});

	/*
	uluru = {lat: latitude, lng: longitude};
	//uluru = {lat: -34.47282939083207, lng: 150.56927919387817};
	var map = new google.maps.Map(document.getElementById('map'), {
	  zoom: 12,
	  center: uluru
	});
	var marker = new google.maps.Marker({
	  position: uluru,
	  map: map
	});
	*/

	// Try HTML5 geolocation.
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function(position) {
		var geoLocation = {
			lat: position.coords.latitude,
			lng: position.coords.longitude
		};

		document.getElementById("latitude").value=position.coords.latitude;
		document.getElementById("longitude").value=position.coords.longitude;

		//infoWindow.setPosition(geoLocation);
		//infoWindow.setContent('Location found.');
		//infoWindow.open(map);
		map.setCenter(geoLocation);
		marker.setPosition(geoLocation);
		console.log('Got ur location')
		}, function() {
			handleLocationError(true, infoWindow, map.getCenter());
		});
	} else {
		// Browser doesn't support Geolocation
		handleLocationError(false, infoWindow, map.getCenter());
	}
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
	alert(browserHasGeolocation ?
		'Error: The Geolocation service failed.' :
		'Error: Your browser doesn\'t support geolocation.');
	infoWindow.open(map);
}
/*
$(document).ready(function () {
	$('#map').hide("800");

	$('#show_map').on('click',function(){
	    $('#map').slideToggle('800');
	});

});
*/
