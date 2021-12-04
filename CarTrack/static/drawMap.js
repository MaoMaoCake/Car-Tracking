function getLocationAPI(){
    var xmlHttp = new XMLHttpRequest();
    // this can be synchronous because website will not function without this key
    xmlHttp.open("GET", "/api/map_key", false); // true for asynchronous
    xmlHttp.send(null);

    if (xmlHttp.status === 200) {
        return JSON.parse(xmlHttp.responseText);
    }
}
function getLocation(device_id){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "/api/get_location?device_id=" + device_id, false); // true for asynchronous
    xmlHttp.send(null);

    if (xmlHttp.status === 200) {
        return JSON.parse(xmlHttp.responseText);
    }
}
function display_map(device_id) {
    // get location using device id
    var locations = getLocation(device_id).locations;
    console.log(locations);
    // get api key from backend
    mapboxgl.accessToken = getLocationAPI().map_key;

    // parse Center using the first location
    let LngLat = locations[0].split(",");
    console.log(LngLat);
    let lat = parseFloat(LngLat[0]);
    let long = parseFloat(LngLat[1]);

    // create map
    var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/satellite-streets-v10',
    center: [long,lat],
    zoom: 16,
    bearing: -17.6,
    pitch:45
    });

    // Map controls
    map.addControl(new mapboxgl.FullscreenControl());
    for (let i = 0; i < locations.length; i++){
        let LngLat = locations[i].split(",");
        let lat = parseFloat(LngLat[0]);
        let long = parseFloat(LngLat[1]);
        // add marker
        new mapboxgl.Marker()
        .setLngLat([long,lat])
        .addTo(map);
    }

    // Navigation marker at top-left corner
    var nav = new mapboxgl.NavigationControl();
    map.addControl(nav, 'top-left');

    // The 'building' layer in the mapbox-streets vector source contains building-height
    // data from OpenStreetMap.
    map.on('load', function() {
        // Insert the layer beneath any symbol layer.
        var layers = map.getStyle().layers;
        var labelLayerId;
        for (var i = 0; i < layers.length; i++) {
            if (layers[i].type === 'symbol' && layers[i].layout['text-field']) {
                labelLayerId = layers[i].id;
                break;
            }
        }
        map.addLayer({
            'id': '3d-buildings',
            'source': 'composite',
            'source-layer': 'building',
            'filter': ['==', 'extrude', 'true'],
            'type': 'fill-extrusion',
            'minzoom': 15,
            'paint': {
                'fill-extrusion-color': '#aaa',
                // use an 'interpolate' expression to add a smooth transition effect to the
                // buildings as the user zooms in
                'fill-extrusion-height': [
                    "interpolate", ["linear"], ["zoom"],
                    15, 0,
                    15.05, ["get", "height"]
                ],
                'fill-extrusion-base': [
                    "interpolate", ["linear"], ["zoom"],
                    15, 0,
                    15.05, ["get", "min_height"]
                ],
                'fill-extrusion-opacity': .6
            }
        }, labelLayerId);
    });
}