var map = L.map('map').setView([39.5, -8.0], 6);
var popup = L.popup();

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contribuidores'
}).addTo(map);

var polygon = L.polygon([
    [39.60992, -11.387329],
    [39.414977, -10.033264],
    [39.01705, -10.148621],
    [39.149233, -11.461487]
]).addTo(map);

polygon.bindPopup("Restrições Cabos no Fundo do Mar ");

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);