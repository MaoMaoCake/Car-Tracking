import React from "react";
import ReactDOM from "react-dom"
import App from "./App"

// render the DOM
ReactDOM.render(<App />,document.getElementById("root"))

// renders Hello element
let Name =  "MaoMao" //get from server
document.getElementById("greet").innerText = `Hello ${Name}`

//add buttons to my trackers
let trackers = document.getElementById("my_tracker").getElementsByClassName("tracker-elem")
for (var i = 0; i < trackers.length; i++ ){
    // attach a event listener to each button
    trackers[i].addEventListener("click",function(){
        // send this request along with auth token to get datapoints
        // with the datapoints call the mapping api

        // get the device id from attribute tags
        console.log(this.getElementsByTagName("Button")[0].getAttribute("datafld"))
    })
}
//add and share buttons
document.getElementById("add_tracker").addEventListener("click",function() {
    console.log("Go to add page")
})

document.getElementById("share_tracker").addEventListener("click",function() {
    console.log("Go to share page")
})

// attach to shared trackers
// i could make these proper functions but im lazy
let s_trackers = document.getElementById("shared_tracker").getElementsByClassName("tracker-elem")
for (i = 0; i < s_trackers.length; i++ ){
    // attach a event listener to each button
    s_trackers[i].addEventListener("click",function(){
        // send this request along with auth token to get datapoints
        // with the datapoints call the mapping api

        // get the device id from attribute tags
        console.log(this.getElementsByTagName("Button")[0].getAttribute("datafld"))
    })
}





