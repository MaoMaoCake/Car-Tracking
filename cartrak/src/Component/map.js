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

export default function Map(props) {
    // let device_id = useState({data : []});
    let loc_array = props.data.location
    console.log("clicked")
    const mapContainer = useRef(null);
    const map = useRef(null);
    const zoom = 17;

    useEffect(() => {
        map.current = new mapboxgl.Map({
        container: mapContainer.current,
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [loc_array[0].longitude, loc_array[0].latitude],
        zoom: zoom
        });
        for (let i = 0; i < loc_array.length; i++){
            new mapboxgl.Marker() // initialize a new marker
            .setLngLat([loc_array[i].longitude, loc_array[i].latitude]) // Marker [lng, lat] coordinates
            .addTo(map.current);
        }

        });
        return (
            <div>
              <div ref={mapContainer} className="map-container" />
            </div>
          );
}