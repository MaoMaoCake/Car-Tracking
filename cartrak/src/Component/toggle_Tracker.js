import React from "react";

export default function toggle(type){
    let trackers = document.getElementById(type).getElementsByClassName("tracker-elem")
    for (let i = 0; i < trackers.length; i++) {

        if (trackers[i].getAttribute("style") === "display: none;") {
            trackers[i].setAttribute("style", "display: block;")
        } else if (trackers[i].getAttribute("style") === "display: block;") {
            trackers[i].setAttribute("style", "display: none;")
        }
    }
}