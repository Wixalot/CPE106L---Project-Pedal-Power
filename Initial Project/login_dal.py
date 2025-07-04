def get_user_credentials():
    credentials = {}
    with open("user.txt", "r") as file:
        for line in file:
            user, pwd = line.strip().split(",")
            credentials[user] = pwd
    return credentials