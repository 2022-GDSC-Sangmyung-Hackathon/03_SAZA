var map;
var button = document.getElementById('map_button');

function initMap() {
  //지도 중심 좌표 입력
  var gyeongbokgung = { lat: 37.57979553563185, lng: 126.97706245552442 };
  map = new google.maps.Map( document.getElementById('map'), {
      zoom: 15,
      center: gyeongbokgung
    });
  //이곳에 사용자 위치를 넣어주면 됨
  var MarkerPoint = { lat: 37.57956596361732, lng: 126.9803240214433};
  var Marker = new google.maps.Marker({
      position: MarkerPoint,
      map: map,
      label: "내 위치",
      icon: {
        url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png",
      }
    });
}
