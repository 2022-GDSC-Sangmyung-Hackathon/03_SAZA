function initMap() {

    const map = new google.maps.Map(document.getElementById("listMap"), {
        zoom: 14,
        center: { lat: 37.5407622, lng: 127.0706095 },
    });

    for (var i = 0; i < locations.length; i++) {
        var marker = new google.maps.Marker({
            map: map,
            label: locations[i].place,
            position: new google.maps.LatLng(locations[i].lat, locations[i].lng),
        });
    }
}
const locations = [
    { place:"건대입구역", address: " ", lat: 37.539922, lng: 127.070609 },
    { place:"어린이대공원역", address : " " , lat: 37.547263, lng: 127.074181 },
    { place:"건대입구역", address: " ", lat: 37.539922, lng: 127.070609 },
    { place:"어린이대공원역", address : " " , lat: 37.547263, lng: 127.074181 },
    { place:"건대입구역", address: " ", lat: 37.539922, lng: 127.070609 },
    { place:"어린이대공원역", address : " " , lat: 37.547263, lng: 127.074181 },
    { place:"건대입구역", address: " ", lat: 37.539922, lng: 127.070609 },
    { place:"어린이대공원역", address : " " , lat: 37.547263, lng: 127.074181 },
];