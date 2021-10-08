function GetTracker(user_token, type){
    //connect to server using token
    // look in the user's ${type} field to see what devices we need
    // request the device info using device_id
    // return json list of devices { data: [ {device_id,color,nickname} ]
    return { data: [{device_id:"test",
                      color:"#FF0000",
                      nickname:"Testing"},
                    {device_id:"test2",
                        color:"#00FF00",
                        nickname:"Testing2"}]
            }
}
export default GetTracker