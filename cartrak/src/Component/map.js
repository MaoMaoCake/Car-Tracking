import getLocation from "./getLocation";

export default function drawMap(device_id){
    let loc_array = getLocation(device_id)
    return (
        <div>
            {loc_array.toString()}
        </div>
    );
}