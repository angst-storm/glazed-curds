
let markers = [];

function initMap() {
    this.markerInfoWindow = new google.maps.InfoWindow({ content: "" });
    this.bounds = new google.maps.LatLngBounds();
    // The location of Uluru
    const uluru = {lat: 55.755819, lng: 37.617644};
    // The map, centered at Uluru
    this.map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        mapTypeId: "roadmap",
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


}//Создаем карту



function setDefaultMapLocation() {
    this.map.setCenter(new google.maps.LatLng( 55.755819, 37.617644));
}

function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}// Парсить json
let rrr = [{ "dispatch":"район Замоскворечье",   "arrival":"Басманный район",  'value':7},
    { "dispatch":"район Замоскворечье",   "arrival": "Пресненский район", 'value':8}]

function addMarkers() {
    readTextFile("scripts/districts.json", function (text) {
        var data = JSON.parse(text);
        data.forEach(center => {
            markers.push(new google.maps.Marker({
                position: {lat: center.lat, lng: center.lng},
                map: null,
                title: center.name,
            }))
        });

        rrr.forEach(el => {
            let el1 = {};
            let el2= {};
            data.forEach(value => {
                if(value.name === el.dispatch){
                    el1 = value;
                }
                if(value.name === el.arrival){
                    el2 = value;
                }
            });

           let ll1 = {lat: el1.lat, lng: el1.lng};
           let ll2 = {lat: el2.lat, lng: el2.lng};
           const makersPoly = [ll1, ll2];
            let trafic = {
                1: "#ffffff",
                2: "#75fdf3",
                3: "#00ff94",
                4: "#29de03",
                5: "#ffea00",
                6: "#e58900",
                7: "#fa9252",
                8: "#ff5900",
                9: "#ff0000",
                10: "#000000"
            }

            const flightPath = new google.maps.Polyline({
                path: makersPoly,
                geodesic: true,
                strokeColor: trafic[Math.round(el.value)],
                strokeOpacity: 1.0,
                strokeWeight: 3,
            });
            flightPath.setMap(map);
        })

        drawMarkerCluster();
    });
} // Добавляем маркеры и Polylines

function drawMarkerCluster() {
    let vaccinationCLuster = new MarkerClusterer(
        this.map,
        markers,
        { imagePath: `./assets/cluster/m` }
    );
} // Отрисовка кластера

window.initialiseMap = initMap;


// Для рисования геом фигур прям на карте
//var drawingManager = new google.maps.drawing.DrawingManager();
//drawingManager.setMap(map);