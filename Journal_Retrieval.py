import os
import datetime
import json
from collections import OrderedDict


''' List Previous Journal Function '''


def list_previous_journal(filename):

    string = open(filename, "r")
    your_dictionary = json.loads(string.read())
    read_journal(your_dictionary)
    string.close()
    ''' File closed '''


''' Check length of Journal Function '''


def check_len_journal(string, your_dictionary):

    # CHeck length of dictionary
    if len(your_dictionary) == 50:
        your_dictionary.popitem(last=False)
    write_journal(string, your_dictionary)


''' Write Journal Function '''


def write_journal(string, your_dictionary = None):

    # Check if dictionary exists
    if your_dictionary is None:
        ''' Create dictionary if doesn't exist'''
        your_dictionary = OrderedDict()

    today = datetime.datetime.now()
    date = today.strftime("%d %b %Y %H:%M%p")
    journal = input('Journal Entry:')

    ''' Update dictionary '''
    your_dictionary[date] = journal
    ''' Dumps dictionary in file'''
    string.write(json.dumps(your_dictionary))
    string.close()
    ''' File closed '''


''' Read Journal Function '''


def read_journal(your_dictionary):

    for key in your_dictionary.keys():
        print(key, " - ", your_dictionary[key])


''' Choice to read/write journal or log out'''


def journal_read_write(username):

    filename = username + ".txt"

    # If file exists
    if os.path.isfile(filename):

        choice = input("Choose one of the below options:\n"
                       "1. List all previous journals\n"
                       "2. Create a new entry\n"
                       "3. Log Out\t")

        if choice == '1':
            list_previous_journal(filename)
            journal_read_write(username)

        elif choice == '2':
            string = open(filename, "r")
            your_dictionary = json.loads(string.read())
            string.close()
            string = open(filename, "w")
            check_len_journal(string, your_dictionary)
            journal_read_write(username)

        elif choice == '3':
            import main
            main.login_or_signup()

        else:
            print("Invalid option")

    # If file doesn't exist

    else:
        string = open(filename, "w")
        write_journal(string)
        journal_read_write(username)