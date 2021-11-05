from flask import Flask,request

from backend.utility.login import verify_user,get_token
from backend.utility.location import get_locations

from backend.utility.testfunc import magic

app = Flask(__name__)


@app.route('/api/login',methods=['GET'])
def login():
    # set a default value to the user token if the token exist it will be overwritten
    user_token = {"token": "None"}
    if request.method == "GET":
        # get the username and password from the request
        username = request.args.get('username')
        password = request.args.get('password')
        # verify the user
        if verify_user(username,password):
            user_token = {"token":get_token(username)}
    return user_token

@app.route('/api/locations',methods=['GET'])
def locations():
    locations = get_locations(1)
    return locations

@app.route('/api/trackers',methods=['GET'])
def get_trackers():
    trackers = magic()
    return trackers

if __name__ == '__main__':
    app.run(debug=True)
