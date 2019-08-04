import Sign_up_to_Journal as Login
import Journal_Retrieval as Journal

''' Login/Sign Up to Journal '''


def login_or_signup():

    username = Login.login_or_signup()

    ''' Check if username exists '''
    if username is False:
        ''' Check again if username fails '''
        login_or_signup()

    else:
        print("Welcome to you Journal", username)

        ''' Read/Write Journal '''
        Journal.journal_read_write(username)


''' Starting the Application '''

login_or_signup()