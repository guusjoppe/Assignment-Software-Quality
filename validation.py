import re

class Validator:
    def __init__(self):
        self.is_valid_name = r'[a-zA-Z ]+'
        self.is_valid_zip = r'([0-9]){4}([a-z,A-Z]){2}'

    def validateUsername(self, username):
        if username.count >= 5 and username.count <= 20:
            #TODO: insert other if statements validating the username
            print("valid username")
            return True
        print("The username should have a length between 5 and 20 characters.")
        return False

    def validateClientName(self, fullname):
        return bool(re.match(fullname, self.is_valid_name))

    def validateEmail(self, email):
        #TODO: implement email validation
        return True

    def validatePhone(self, phone):
        #TODO: implement phone validation
        return True

    def validateAddress(self, street, number, zipCode):
        status = ""
        if not bool(re.match(street, self.is_valid_name)):
            status += "not a valid street \n"
        if not number.isdigit():
            status += "not a valid number \n"
        if not bool(re.match(zipCode, self.is_valid_zip)):
            status += "not a valid zipCode \n"
        if status != "":
            print(status)
            return False
        else:
            return True

    def validateCity(self, city, cities):
        is_valid_city = False
        if city.isdigit():
            for c in cities:
                if c == city:
                    is_valid_city = True
        return is_valid_city