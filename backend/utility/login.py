def verify_user(username, password):
    db = {"admin": "password","maomao":"cake"}
    if username in db and db[username] == password:
        return True

def get_token(username):
    if username == 'admin':
        return '12345'
    if username == 'maomao':
        return 'abcde'