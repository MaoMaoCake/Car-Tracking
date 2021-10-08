import React from "react";
import ReactDOM from "react-dom"
import App from "./App"
import GetTracker from "./GetTrack";
// import DrawMap from "./DrawMap"

// render the DOM
ReactDOM.render(<App />,document.getElementById("root"))

// renders Hello element
let Name =  "MaoMao" //get from server
document.getElementById("greet").innerText = `Hello ${Name}`

//renders tracker element

let my_trackers = GetTracker()
let shared_trackers = GetTracker()
let my_trackers_dom = document.getElementById("mytrack")
let shared_trackers_dom = document.getElementById("sharedtrack")
// console.log(trackers.data)
for ( let i = 0 ; i < my_trackers.data.length; i++){
    // my_trackers_dom.append()
    console.log(my_trackers.data[i].nickname)
}




