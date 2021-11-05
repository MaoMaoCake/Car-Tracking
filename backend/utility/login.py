def verify_user(username, password):
    if username == "admin" and password == "password":
        return True

def get_token(username):
    if username == 'admin':
        return '12345'