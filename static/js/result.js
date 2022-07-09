var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

function initMap() {
    if (navigator.geolocation)
    {
        $("#latlng").html("");
        $("#errormsg").html("");
        navigator.geolocation.getCurrentPosition (function (pos)
        {
            lat = pos.coords.latitude;
            lng = pos.coords.longitude;
  
            $("#latlng").html("위도 : " + lat + ", 경도 : "+ lng);
  
            var mapOptions = {
                zoom: 16,
                mapTypeId: google.maps.MapTypeId.ROADMAP,
                center: new google.maps.LatLng(lat, lng)
            };
  
            map = new google.maps.Map(document.getElementById('map'),mapOptions);
            var myIcon = {
                url: "mapmarker.png", // url
                scaledSize: new google.maps.Size(50, 50), // scaled size
            };
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(lat,lng),
                map: map,
                icon: myIcon
            });
            },function(error)
        {
            switch(error.code)
            {
                case 1:
                    $("#errormsg").html("User denied the request for Geolocation.");
                    break;
                case 2:
                    $("#errormsg").html("Location information is unavailable.");
                    break;
                case 3:
                    $("#errormsg").html("The request to get user location timed out.");
                    break;
                case 0:
                    $("#errormsg").html("An unknown error occurred.");
                    break;
            }
        });
    }
    else
    {
        $("#errormsg").html("Geolocation is not supported by this browser.");
    }
  }
