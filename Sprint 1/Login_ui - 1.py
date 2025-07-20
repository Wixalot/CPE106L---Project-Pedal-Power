from loginbl import authenticate_user


def main():

    while True:

        username = input("Enter your username (or 0 to exit): ")

        if username == "0":

            break

        password = input("Enter your password (or 0 to exit): ")

        if password == "0":

            break


        if authenticate_user(username, password):

            print("Login successful!")

        else:

            print("Login failed. Please check your username and password.")

if __name__ == "__main__":

    main()