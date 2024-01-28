import common

def delete_user():
    users = common.read_password_file()
    username = input("Enter username to delete: ")

    user = common.find_user(username, users)
    if user is None:
        print("User not found.")
        return

    users.remove(user)
    common.write_password_file(users)
    print("User Deleted.")

if __name__ == '__main__':
    delete_user()
