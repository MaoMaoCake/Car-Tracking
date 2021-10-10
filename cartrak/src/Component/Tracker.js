import React from "react";
import GetTracker from "./GetTrack";
import {Link} from "react-router-dom";

import toggle from "./toggle_Tracker";
import track from "./Track_Tracker";

function Trackers(){
    let user_token = "get_from_db"
    let my_trackers = GetTracker(user_token,"private")
    let shared_trackers = GetTracker(user_token,"shared")
    return (
        <div id="trackers">
            <div id="my_tracker">
                <button id='my_trak_btn' onClick={function(){toggle("my_tracker")}}>My Trackers</button>
                {my_trackers.data.map((device) => (
                    <div className='tracker-elem' style={{display:"none"}}>
                        <button style={{color:device.color}} onClick={function(){track(device.nickname,device.device_id)}}>{device.nickname}</button>
                    </div>
                ))}
                    <div className='tracker-elem' style={{display:"none"}}> <Link to="/add_tracker">+ Add Trackers</Link></div>
            </div>

            <div id="shared_tracker">
                <button id='shared_trak_btn' onClick={function(){toggle("shared_tracker")}}>Shared Trackers</button>
                {shared_trackers.data.map((device) => (
                    <div className='tracker-elem' style={{display:"none"}}>
                        <button style={{color:device.color}} onClick={function(){track(device.nickname,device.device_id)}}>{device.nickname}</button>

                    </div>
                ))}
                <div className='tracker-elem' style={{display: "none"}}> <Link to="/share_tracker">Share Tracker</Link></div>
            </div>
        </div>
    )
}

export default Trackers