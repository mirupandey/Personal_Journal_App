Use main.py to run the appliaction.

The main file transfers control to Sign_up_to_Journal.py to choice the option out of Login, Sign Up or Exiting the application.

The Login function asks for username and checks if it exists, if it does then password is being checked and if matches the user logs in, else asks for re-logging option or exiting the application.
If user doesn't exist then asks for re-logging or exiting the application.

The Sign Up function asks for username and checks if it exists, if it does not then password is being asked, else asks for re-logging option or exiting the application.

The control is then transferred to Journal_Retrieval.py to choose to list all previous journal or create new journal or log out.

read_journal reads existing journals
write journal writes new journal
check length of journal