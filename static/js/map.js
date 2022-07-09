function GpsGetCurrentPosition(){
    if (navigator.geolocation)
    {
        $("#latlng").html("");
        $("#errormsg").html("");
        navigator.geolocation.getCurrentPosition (function (pos)
        {
            lat = pos.coords.latitude; 
            lng = pos.coords.longitude;
            data = {
                'user_lat' : lat,
                'user_lng' : lng
            };
            $.ajax({
                type:'POST',
                url:'',
                data: JSON.stringify(data),
                success: function(json){
                    console.log('data pass success');
                    location.href='./templates/restaurantList.html'
                },
                error: function(json){
                    console.log('data pass failed');
                },
                complete: function(json){
                    console.log('complete');
                }
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
