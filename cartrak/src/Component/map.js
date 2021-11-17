import React, { useRef, useEffect, useState } from 'react';
import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import 'mapbox-gl/dist/mapbox-gl.css';

import './map.css';
import {getCookie} from "./cookie";
function get_map_key(){
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open("GET", "/api/map?token=" + getCookie("token"), false); // true for asynchronous
    xmlHttp.send(null);

    if (xmlHttp.status === 200) {
        return JSON.parse(xmlHttp.responseText);
    }
}
// get_map_key returns JSON with api_key key
mapboxgl.accessToken = get_map_key().api_key;

export default function Map() {
    const mapContainer = useRef(null);
    const map = useRef(null);
    const [lng] = useState(100.509177);
    const [lat] = useState(13.732571);
    const [zoom] = useState(9);

    useEffect(() => {
        if (map.current) return; // initialize map only once
        map.current = new mapboxgl.Map({
        container: mapContainer.current,
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [lng, lat],
        zoom: zoom
        });
        map.current = new mapboxgl.Marker() // initialize a new marker
        .setLngLat([lng, lat]) // Marker [lng, lat] coordinates
        .addTo(map.current);
        });
        return (
            <div>
              <div ref={mapContainer} className="map-container" />
            </div>
          );
}