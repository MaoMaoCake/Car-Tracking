function GetTracker(user_token, type){
    //connect to server using token
    // look in the user's ${type} field to see what devices we need
    // request the device info using device_id
    // return json list of devices { data: [ {device_id,color,nickname} ]
    if (type === "private") {
        return { data: [{device_id:"test-my",
                color:"#FF0000",
                nickname:"Testing-my"},
                {device_id:"test2-my",
                    color:"#00FF00",
                    nickname:"Testing2-my"},
                {device_id:"test3-my",
                    color:"#0000FF",
                    nickname:"Testing3-my"}]
        }
    } else if (type === "shared"){
        return { data: [{device_id:"test-shared",
                color:"#FF0000",
                nickname:"Testing-shared"},
                {device_id:"test2-shared",
                    color:"#00FF00",
                    nickname:"Testing2-shared"}]
        }
    }
}
export default GetTracker