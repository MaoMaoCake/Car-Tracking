import React from "react";
import Trackers from "./Tracker";
import Logout from "./Logout";
import {getCookie} from "./cookie";
import {Link} from "react-router-dom";

function NavBar(){
    let Name = getCookie("username");
    if (Name !== ""){
        return(
            <div id="nav">
                <div id="greet">
                    Hello {Name}
                </div>
                <Trackers />
                {/*all logout does is just delete the cookie and reset to login page*/}
                <Logout />
            </div>
        )
    } else {
        return (
            <h2>Please <Link to="/login">Login</Link></h2>
        )
    }
}
export default NavBar