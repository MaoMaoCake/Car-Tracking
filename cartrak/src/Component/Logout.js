import React from "react";
import setCookie from "./cookie";

export default function Logout(){
    setCookie("username","");
    setCookie("token","");
    window.location.reload();

}