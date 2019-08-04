import os
import json
from collections import OrderedDict

''' Username exists or not Function '''


def username_exists(your_dictionary, username):

    for key in your_dictionary.keys():
        if key == username:
            return True
    return False


''' Password Match Function '''


def password_match(your_dictionary, username, password):

    if your_dictionary[username] == password:
        return True
    else:
        return False


''' Store Username Password Function '''


def store_username_password(x, username, password, username_file):

    x[username] = password
    username_file.write(json.dumps(x))


''' Login Function '''


def login():

    while True:
        # If file exists
        if os.path.isfile('users.txt'):
            username_file = open('users.txt', 'r')
            your_dictionary = json.loads(username_file.read())
            username = input('Enter username:')

            ''' Length of username check'''
            if not len(username) > 0:
                print("Username can't be blank")
                continue
            else:
                username_existence = username_exists(your_dictionary, username)
                if username_existence:
                    while True:
                        while True:
                            password = input('Enter password:')

                            ''' Length of password check'''
                            if not len(password) > 0:
                                print("Password can't be blank")
                                continue
                            else:
                                break
                        password_matches = password_match(your_dictionary, username, password)
                        if password_matches:
                            print("Login Successful")
                            return username
                        else:
                            print("Password doesn't match")
                            choose = input('1. Try Again\n'
                                           '2. Exit\t')
                            if choose == 1:
                                continue
                            else:
                                break
                else:
                    print("User doesn't exist")
                    choose = input('1. Try Again\n'
                                   '2. Login/Sign Up Option\n'
                                   '2. Exit\t')
                    if choose == '1':
                        continue
                    elif choose == '2':
                        login_or_signup()
                    else:
                        break

        # If file doesn't exist
        else:
            print("There are no registered users.")
            return False
    username_file.close()
    return False


''' Sign Up Function'''


def sign_up():

    while True:

        # If file exists
        if os.path.isfile('users.txt'):
            username_file = open('users.txt')
            your_dictionary = json.loads(username_file.read())
            username_file.close()
            username_file = open('users.txt', 'w+')

        # If file doesn't exist
        else:
            username_file = open('users.txt', 'w+')
            your_dictionary = OrderedDict()
        while True:
            username = input('Enter username:')
            if not len(username) > 0:
                print("Username can't be blank")
                continue
            else:
                break

        username_existence = username_exists(your_dictionary, username)
        if username_existence:
            print("Username Already Exists")
            choose = input('1. Try Again\n'
                           '2. Login/Sign Up Option\n'
                           '2. Exit\t')
            if choose == '1':
                continue
            elif choose == '2':
                login_or_signup()
            else:
                break

        else:
            while True:
                password = input('Enter password')
                if not len(password) > 0:
                    print("Password can't be blank")
                    continue
                else:
                    break
            store_username_password(your_dictionary, username, password, username_file)
            username_file.close()
            print("Sign Up Successful.")
            return username
    return False


''' Login or SignUp Function '''


def login_or_signup():

    choice = input('Choose one of the below options:\n'
                   '1. Login\n'
                   '2. Signup\n'
                   '3. Exit\t')

    if choice == '1':
        login_value = login()
        return login_value
    elif choice == '2':
        sign_up_value = sign_up()
        return sign_up_value

    elif choice == '3':
        print("Successfully Exited")
        exit(0)