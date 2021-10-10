import React from "react";

export default function track(nickname,id){
    console.log(nickname,id)
    document.getElementById("device_name").innerText = nickname
    // this will connect with the server here to get the data points
}