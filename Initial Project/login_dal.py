def get_user_credentials():

    with open("users.txt", "r") as f:

        return [line.strip() for line in f if line.strip()]