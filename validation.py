import re

is_valid_name = r'[a-zA-Z ]+'
is_valid_zip = r'([0-9]){4}([a-z,A-Z]){2}'

def validateUsername(username):
    if username.count >= 5 and username.count <= 20:
        #TODO: insert other if statements validating the username
        print("valid username")
        return True
    print("The username should have a length between 5 and 20 characters.")
    return False

def validateClientName(fullname):
    return bool(re.match(fullname, is_valid_name))

def validateEmail(email):
    #TODO: implement email validation
    return True

def validatePhone(phone):
    #TODO: implement phone validation
    return True

def validateAddress(street, number, zipCode, city):
    status = ""
    if not bool(re.match(street, is_valid_name)):
        status += "not a valid street"
    if not number.isdigit():
        status += "not a valid number"
    if not bool(re.match(zipCode, is_valid_zip)):
        status += "not a valid zipCode"
    if status != "":
        print(status)
        return False
    else:
        return True