var markerPlease = [
    {name:'SP06201220Z', lat:55.881891 ,lng:37.446278, fl: "t"},
    {name:'SP05701220Z', lat:55.601972 ,lng:37.484425, fl: "t"},
    {name:'SP05081220Z', lat:55.647387 ,lng:37.743965, fl: "t"},
    {name:'SP05051220Z', lat:55.581189 ,lng:37.465576, fl: "t"},
    {name:'SP04081120Z', lat:55.690575 ,lng:37.530481, fl: "t"},
    {name:'SP01351120Z', lat:55.596397 ,lng:37.479893, fl: "r"},
    {name:'SP00911120Z', lat:55.733404 ,lng:37.405937, fl: "r"},
    {name:'SP00871120Z', lat:55.703272 ,lng:37.508136, fl: "r"},
    {name:'SP00811120Z', lat:55.70109 ,lng:37.863719, fl: "r"},
    {name:'SP00461020Z', lat:55.546172,lng:37.584935, fl: "r"},
    {name:'SP00351020Z', lat:55.898174,lng:37.587782, fl: "r"},
];
let markers = [];
// var markerPlease2 = [];
// for (var i = 0; i <= markerPlease.length; i++) {
//   var latt = markerPlease[i].lat + 0.005;
//   var lngg = markerPlease[i].lng + 0.005;
//   markerPlease2.push({lat:latt, lng:lngg})
// }
// Initialize and add the map
function initMap() {
    this.markerInfoWindow = new google.maps.InfoWindow({ content: "" });
    this.bounds = new google.maps.LatLngBounds();
    // The location of Uluru
    const uluru = {lat: 55.755819, lng: 37.617644};
    // The map, centered at Uluru
    this.map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        mapTypeId: "terrain",
        center: new google.maps.LatLng(55.755819, 37.617644),
    });

    this.markers = [];

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };
                this.map.setCenter(pos);
            },
            () => {
                // could not fetch location
                setDefaultMapLocation()
            }
        );
    } else {
        setDefaultMapLocation()
    }

    addMarkers();
}

function setDefaultMapLocation() {
    this.map.setCenter(new google.maps.LatLng( 55.755819, 37.617644));
}

function addMarkers() {
    markerPlease.forEach(center => {
        markers.push(new google.maps.Marker({
            position: {lat: center.lat, lng: center.lng},
            map: null,
            title: center.name,
        }))
    });

    drawMarkerCluster();

}

function drawMarkerCluster() {
    let vaccinationCLuster = new MarkerClusterer(
        this.map,
        markers,
        { imagePath: `C:\\Users\\tania\\Учёба\\учебные проекты\\хакатон\\m1.png` }
    );
}
// for (var i = 0; i <= markerPlease.length; i++) {
//     for (var j = 0; j <= markerPlease.length; j++) {
//         if (markerPlease[i] !== markerPlease[j]) {
//             const markers = [markerPlease[i].lat, markerPlease[j].lng];
//             const flightPath = new google.maps.Polyline({
//                 path: markers,
//                 geodesic: true,
//                 strokeColor: markerPlease[i].fl === 'r' ? "#FF0000" : "#00FF00",
//                 strokeOpacity: 1.0,
//                 strokeWeight: 2,
//             });
//             flightPath.setMap(map);
//
//         }
//     }
//     var myPos = new google.maps.LatLng(markerPlease[i].lat, markerPlease[i].lng);
//     var marker = new google.maps.Marker({
//         position: myPos,
//         map: map,
//         title: markerPlease[i].name,
//         icon: {
//             labelOrigin: new google.maps.Point(5, 5),
//             scaledSize: new google.maps.Size(10, 10)
//         }
//     });
// }

window.initialiseMap = initMap;


// Для рисования геом фигур прям на карте
//var drawingManager = new google.maps.drawing.DrawingManager();
//drawingManager.setMap(map);