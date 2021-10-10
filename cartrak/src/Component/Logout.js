import React from "react";
import setCookie from "./cookie";

export default function Logout(){
    return (<button onClick={function (){setCookie("username","");window.location.reload();}}>Logout</button>)
}