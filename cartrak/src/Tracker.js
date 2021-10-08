import React from "react";
import GetTracker from "./GetTrack";

function Trackers(){
    let user_token = "get_from_db"
    let my_trackers = GetTracker(user_token,"private")
    let shared_trackers = GetTracker(user_token,"shared")
    return (
        <div id="trackers">
            <div id="my_tracker">
                {my_trackers.data.map((device) => (
                    <div class='tracker-elem'>
                        <button style={{color:device.color}} datafld={device.device_id}>{device.nickname}</button>
                    </div>
                ))}
                <button id="add_tracker">+ Add Tracker</button>
            </div>
            <div id="shared_tracker">
                {shared_trackers.data.map((device) => (
                    <div class='tracker-elem'>
                        <button style={{color:device.color}} datafld={device.device_id}>{device.nickname}</button>

                    </div>
                ))}
                <button id="share_tracker">Share Tracker</button>
            </div>
        </div>
    )
}
export default Trackers