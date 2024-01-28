import common

def login():
    users = common.read_password_file()
    username = input("User: ")
    password = input("Password: ")

    user = common.find_user(username, users)
    if user and user[2] == common.rot13(password):
        print("Access granted.")
    else:
        print("Access denied.")

if __name__ == '__main__':
    login()
