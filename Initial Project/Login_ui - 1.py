from loginbl import authenticate_user

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if authenticate_user(username, password):
        print("Login successful!")
    else:
        print("Login failed. Please check your username and password.")
if __name__ == "__main__":
    main()