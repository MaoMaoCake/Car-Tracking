export default function getLocation(device_id){
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open("GET", "/api/locations?device_id=" + device_id, false); // true for asynchronous
    xmlHttp.send(null);

    if (xmlHttp.status === 200) {
        return JSON.parse(xmlHttp.responseText);
    }
}