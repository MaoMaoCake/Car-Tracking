from flask import Flask,request

from backend.utility.login import verify_user,get_token
from backend.utility.location import get_locations
from backend.utility.signup import add_user,check_user_not_exist,check_email_not_exist
from backend.utility.trackers import getTrackers

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route('/api/login',methods=['GET'])
def login():
    # set a default value to the user token if the token exist it will be overwritten
    user_token = {"token": "None"}
    if request.method == "GET":
        # get the username and password from the request
        # get cookies from the request
        username = request.args['username']
        password = request.args['password']
        # verify the user
        if verify_user(username,password):
            user_token = {"token":get_token(username)}
    return user_token

@app.route('/api/locations',methods=['GET'])
def locations():
    if request.method == "GET":
        # get the token from the request
        device_id = request.args.get('device_id')
        locations = get_locations(device_id)
        return locations

@app.route('/api/trackers',methods=['GET'])
def get_trackers():
    if request.method == "GET":
        # get the token from the request
        token = request.args.get('token')
        trackers = getTrackers(token)
        return trackers

@app.route('/api/signup', methods=['POST'])
def signup():
    if request.method == "POST":
        # forms or args not sure which one to use
        email = request.args.get('email')
        username = request.args.get('username')
        password = request.args.get('password')
        # check if the user or email exist
        if check_user_not_exist(username):
            if check_email_not_exist(email):
                if add_user(username,email,password):
                    return {'status':'success',"message": "User added successfully"}
                else:
                    return {'status':'failed',"message": "User not added"}
            else:
                return {'status':'failed',"message": "Email already exist"}
        else:
            return {'status':'failed',"message": "Username already exist"}

# secure access to API keys from the frontend
@app.route('/api/map', methods=['GET'])
def get_map():
    if request.method == "GET":
        # get the token from the request
        token = request.args.get('token')
        if token != "":
            return {"api_key":os.getenv("MAP_API_KEY")}
        else:
            return {"api_key":""}
if __name__ == '__main__':
    app.run(debug=True)
