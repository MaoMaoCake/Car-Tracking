import React from "react";
import Trackers from "./Tracker";

function NavBar(){
    return(
        <div id="nav">
            <div id="greet"/>
            <Trackers />
            {/*all logout does is just delete the cookie and reset to login page*/}
            <div id="logout"/>
        </div>
    )
}
export default NavBar