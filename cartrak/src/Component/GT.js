function httpGetTokensync(user_token)
{
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open("GET", "/api/trackers?token=" + user_token, false); // true for asynchronous
    xmlHttp.send(null);

    if (xmlHttp.status === 200) {
        return JSON.parse(xmlHttp.responseText);
    }
}

function GT(user_token){
    return httpGetTokensync(user_token);
}
export default GT