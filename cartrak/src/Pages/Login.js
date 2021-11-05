import React from "react";
import {Link} from "react-router-dom";
import setCookie from "../Component/cookie";

const appStyle = {
    height: '250px',
    display: 'flex'
};

const formStyle = {
    margin: 'auto',
    padding: '10px',
    border: '1px solid #c9c9c9',
    borderRadius: '5px',
    background: '#f5f5f5',
    width: '220px',
    display: 'block'
};

const labelStyle = {
    margin: '10px 0 5px 0',
    fontFamily: 'Arial, Helvetica, sans-serif',
    fontSize: '15px',
};

const inputStyle = {
    margin: '5px 0 10px 0',
    padding: '5px',
    border: '1px solid #bfbfbf',
    borderRadius: '3px',
    boxSizing: 'border-box',
    width: '100%'
};

const submitStyle = {
    margin: '10px 0 0 0',
    padding: '7px 10px',
    border: '1px solid #efffff',
    borderRadius: '3px',
    background: '#3085d6',
    width: '100%',
    fontSize: '15px',
    color: 'white',
    display: 'block'
};

const Field = React.forwardRef(({label, type}, ref) => {
    return (
        <div>
            <label style={labelStyle} >{label}</label>
            <input ref={ref} type={type} style={inputStyle} />
        </div>
    );
});

const Form = ({onSubmit}) => {
    const usernameRef = React.useRef();
    const passwordRef = React.useRef();
    const handleSubmit = e => {
        e.preventDefault();
        const data = {
            username: usernameRef.current.value,
            password: passwordRef.current.value,
            callback: function (response) {
                response = JSON.parse(response)
                if (response["token"] !== "None"){
                    setCookie("username",data.username)
                    setCookie("token",response["token"])
                    window.location.replace("/")
                } else {
                    alert("Invalid username or password")
                }
            }
        };
        onSubmit(data);
    };
    return (
        <form style={formStyle} onSubmit={handleSubmit} >
            <Field ref={usernameRef} label="Username:" type="text" />
            <Field ref={passwordRef} label="Password:" type="password" />
            <div>
                <button style={submitStyle} type="submit">Submit</button>
            </div>
            <p>Dont have an acccount?<Link to="/signup"> Sign Up</Link></p>
        </form>

    );
};

export default function Login(){
    const handleSubmit = data => {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState === 4 && xmlHttp.status === 200)
                data.callback(xmlHttp.responseText);
        }
    xmlHttp.open("GET", "/api/login?username="+ data.username + "&password=" + data.password, true); // true for asynchronous
    xmlHttp.send(null);
    };
    return (
        <div style={appStyle}>
            <Form onSubmit={handleSubmit} />
        </div>
    );
}

// function httpGetLoginAsync(username,password, callback)
// {
//     var xmlHttp = new XMLHttpRequest();
//     xmlHttp.onreadystatechange = function() {
//         if (xmlHttp.readyState === 4 && xmlHttp.status === 200)
//             callback(xmlHttp.responseText);
//     }
//     xmlHttp.open("GET", "/api/login?username="+ username + "&password=" + password, true); // true for asynchronous
//     xmlHttp.send(null);
// }
// <button onClick={function (){
//                     httpGetLoginAsync("admin", "password",function (response) {
//                         console.log(response);
//                     });
//                 }}>
//                     Click me
//                 </button>