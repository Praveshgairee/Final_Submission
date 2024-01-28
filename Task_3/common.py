import codecs

# Filepath for the password file
PASSWORD_FILE = 'passwd.txt'

# Function to read the password file
def read_password_file():
    with open(PASSWORD_FILE, 'r') as file:
        return [line.strip().split(':') for line in file]

# Function to write to the password file
def write_password_file(users):
    with open(PASSWORD_FILE, 'w') as file:
        for user in users:
            file.write(':'.join(user) + '\n')

# Function to encrypt and decrypt passwords (ROT-13)
def rot13(s):
    return codecs.encode(s, 'rot_13')

# Function to find a user in the password file
def find_user(username, users):
    for user in users:
        if user[0] == username:
            return user
    return None
