from logindal import get_user_credentials

def authenticate_user(username, password):

    stored_username, stored_password = get_user_credentials()
    
    if username == stored_username and password == stored_password:
        return True
    else:
        return False