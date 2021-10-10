import React from "react";
import GetTracker from "./GetTrack";

function Trackers(){
    let user_token = "get_from_db"
    let my_trackers = GetTracker(user_token,"private")
    let shared_trackers = GetTracker(user_token,"shared")
    return (
        <div id="trackers">
            <div id="my_tracker">
                <button id='my_trak_btn'>My Trackers</button>
                {my_trackers.data.map((device) => (
                    <div className='tracker-elem' style={{display:"none"}}>
                        <button style={{color:device.color}} datafld={device.device_id}>{device.nickname}</button>
                    </div>
                ))}
                    <div className='tracker-elem' style={{display:"none"}}><button id="add_tracker">+ Add Tracker</button></div>
            </div>

            <div id="shared_tracker">
                <button id='shared_trak_btn'>Shared Trackers</button>
                {shared_trackers.data.map((device) => (
                    <div className='tracker-elem' style={{display:"none"}}>
                        <button style={{color:device.color}} datafld={device.device_id}>{device.nickname}</button>

                    </div>
                ))}
                <div className='tracker-elem' style={{display: "none"}}><button id="share_tracker">Share Tracker</button></div>
            </div>
        </div>
    )
}
export default Trackers