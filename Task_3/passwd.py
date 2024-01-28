import common

def change_password():
    users = common.read_password_file()
    username = input("User: ")
    current_password = input("Current Password: ")
    new_password = input("New Password: ")
    confirm_password = input("Confirm New Password: ")

    user = common.find_user(username, users)
    if user is None or user[2] != common.rot13(current_password):
        print("Invalid username or password.")
        return

    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    user[2] = common.rot13(new_password)
    common.write_password_file(users)
    print("Password changed.")

if __name__ == '__main__':
    change_password()
