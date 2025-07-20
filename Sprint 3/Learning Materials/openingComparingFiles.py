# This is a test to opena and compare files with the respective input

file_path = "Users.txt"

usernames = []
passwords = []

with open(file_path, "r") as file:
    for line in file:
        username, password = line.strip().split(",")
        usernames.append(username)
        passwords.append(password)

print(f"username list: {usernames}")
print(f"password list: {passwords}")


text = str(input('''
    Opening a file and compare its content if it matches with the input.\n
    Input: '''))

if text == username:
    print(f"Your input {text} matches with the file content {username}")
else:
    print(f"Your input {text} does not match with the file content {username}")
