var map = L.map('map').setView([39.5, -8.0], 6);
var popup = L.popup();

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contribuidores'
}).addTo(map);

var marker = L.marker([40.0, -8.9]).addTo(map);


var circle = L.circle([41, -9.5], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 50000
}).addTo(map);


var polygon = L.polygon([
    [39.60992, -11.387329],
    [39.414977, -10.033264],
    [39.01705, -10.148621],
    [39.149233, -11.461487]
]).addTo(map);

polygon.bindPopup("Restrições Cabos no Fundo do Mar ");


// function onMapClick(e) {
//     alert("You clicked the map at " + e.latlng);
// }

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}


map.on('click', onMapClick);


var LeafIcon = L.Icon.extend({
    options: {
        shadowUrl: 'diana.png',
        iconSize:     [38, 95],
        shadowSize:   [50, 64],
        iconAnchor:   [22, 94],
        shadowAnchor: [4, 62],
        popupAnchor:  [-3, -76]
    }
});


var greenIcon = new LeafIcon({iconUrl: 'diana.png'}),
    redIcon = new LeafIcon({iconUrl: 'diana.png'}),
    orangeIcon = new LeafIcon({iconUrl: 'diana.png'});


L.icon = function (options) {
    return new L.Icon(options);
};

L.marker([51.5, -0.09], {icon: greenIcon}).addTo(map).bindPopup("I am a green leaf.");
L.marker([51.495, -0.083], {icon: redIcon}).addTo(map).bindPopup("I am a red leaf.");
L.marker([51.49, -0.1], {icon: orangeIcon}).addTo(map).bindPopup("I am an orange leaf.");



const ponto = L.latLng(38.7169, -9.1390, 100); // latitude, longitude, altitude em metros


L.marker(ponto).addTo(map)
    .bindPopup(`Estamos em Lisboa!<br>Altitude: ${ponto.alt} m`)
    .openPopup();

console.log(ponto); // {lat: 38.7169, lng: -9.139, alt: 100}