import React from "react";
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";

import Home from "./Pages/Home";
import Login from "./Pages/Login";
import Add from "./Pages/Add_tracker";
import Share from "./Pages/Share_tracker";
import SignUp from "./Pages/SignUp";


export default function App(){
    return(
        <div>
            <Router>
                <Switch>
                    <Route exact path="/">
                        <Home />
                    </Route>
                    <Route path="/login">
                        <Login />
                    </Route>
                    <Route path="/add_tracker">
                        <Add />
                    </Route>
                    <Route path="/share_tracker">
                        <Share />
                    </Route>
                    <Route path="/signup">
                        <SignUp />
                    </Route>
                </Switch>
            </Router>
        </div>
    )

}