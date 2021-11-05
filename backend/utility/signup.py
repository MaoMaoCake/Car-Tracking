from backend.utility.database import User_db

def check_user_not_exist(username):
    """
    Check if the user already exist in the database
    :param username:
    :return:
    """
    db = User_db()
    if db.get_user(username) is not None:
        return False
    else:
        return True

def check_email_not_exist(email):
    db = User_db()
    if db.get_email(email) is not None:
        return False
    else:
        return True

def add_user(username,email,password):
    """
    Add a new user to the database
    :param username:
    :param email:
    :param password:
    :return:

    password should have been hashed since frontend
    """
    # add user to database
    db = User_db()
    # this command will return a response
    return db.add_user(username, email, password)
