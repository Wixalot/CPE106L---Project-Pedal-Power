from login_dal import get_user_credentials


def authenticate_user(username, password):
    credentials = get_user_credentials()
    for cred in credentials:
        stored_username, stored_password = cred.split(",", 1)
        if username == stored_username and password == stored_password:
            return True
    return False