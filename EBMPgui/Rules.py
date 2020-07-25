import re

regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

def emailverification(email):
    match = re.match(regex, email)

    if match == None:
        return 2
    else:
        return 0

def passwordVerification(password):
    val = True

    if len(password) < 6 or len(password) > 20 or not any(char.isdigit() for char in password):
        return 1
    else:
        return 0

def verifier(email , password):
    if emailverification(email)+passwordVerification(password)==0:
        return 0
    elif emailverification(email)+passwordVerification(password)==1:
        return "Please enter a valid password between 6 to characters with atleast 1 digit"
    elif emailverification(email)+passwordVerification(password)==2:
        return "Please enter valid email"
    elif emailverification(email)+passwordVerification(password)==3:
        return "Please enter valid email and valid password between 6 to characters with atleast 1 digit"
