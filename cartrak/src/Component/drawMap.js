import getLocation from "./getLocation";
import Map from "./map";

export default function drawMap(device_id){
    return (
        <Map data={getLocation(device_id)}/>
    );
}