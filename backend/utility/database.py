import boto3

class User_db:
    def __init__(self):
        self.db = boto3.resource('dynamodb',endpoints='http://localhost:8000')
        self.user = self.db.Table('users')

    def get_user(self, username):
        return self.user.get_item(Key={'username': username})

    def get_email(self, email):
        return self.user.get_item(Key={'email': email})

    def add_user(self, username, email, password):
        response = self.user.put_item(
            Item={
                'username': username,
                'email': email,
                'password': password
            }
        )
        return response