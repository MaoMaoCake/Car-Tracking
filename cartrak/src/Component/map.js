import React, { useRef, useEffect, useState } from 'react';
import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import './map.css';

mapboxgl.accessToken = 'pk.eyJ1Ijoia2FnZXJvdS1tYXRjaGEtbGF0dGUiLCJhIjoiY2t2cXFlNmhmMDBpajJ1bHlkeHVxdDFpOCJ9.kzvIYDL7iAoiwrp4Qi_6Kg';

export default function Map() {
    const mapContainer = useRef(null);
    const map = useRef(null);
    const [lng] = useState(-70.9);
    const [lat] = useState(42.35);
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