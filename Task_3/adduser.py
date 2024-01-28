import common

def add_user():
    users = common.read_password_file()
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = input("Enter password: ")

    if common.find_user(username, users) is not None:
        print("Cannot add. Username already exists.")
        return

    encrypted_password = common.rot13(password)
    users.append([username, real_name, encrypted_password])
    common.write_password_file(users)
    print("User Created.")

if __name__ == '__main__':
    add_user()
