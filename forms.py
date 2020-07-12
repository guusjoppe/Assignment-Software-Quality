from validation import Validator

class Form:

    def newClientForm(self):
        fullname = input("What's the clients fullname?")
        print("What's the clients address?")
        street = input("What's the clients streetname?")
        number = input("What's the housenumber?")
        zipCode = input("What's the ZIP code?")
        cnt = 0
        for city in Cities:
            print(cnt + " : " + city)
            cnt+=1
        city = input("What's the index of the city of the client?")

        validator = Validator()
        if validator.validateClientName(fullname):
            if validator.validateAddress(street, number, zipCode):
                if validator.validateCity(city, Cities):
                    return
                else:
                    print("You've entered an unvalid input. The program will end now.")
                    exit()
            else:
                print("some inputs in the address where unvalid. Please try again.")
                self.newClientForm()
        else:
            print("You've entered a unvalid name. Please try again.")
            self.newClientForm()


    def logOut(self):
        return