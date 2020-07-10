import os
from os import listdir
from os.path import isfile, join
import json
from json import JSONEncoder

global user, securityClearance

def enum(**enums):
    return type('Enum', (), enums)

SecurityClearance = enum(ONE="SuperAdministrator",TWO="SystemAdministrator", THREE="Advisor")


class Context :
    def __init__(self):
        self.Employees = {
            "SuperAdministrators" : [],
            "SystemAdministrators" : [],
            "Advisors" : []
        }
        self.Customers = []
        self.Path = "./data/context.json"

    #Read Employees from json file
    def ReadEmployees(self):
        with open(self.Path) as f:
            if os.stat(self.Path).st_size != 0:
                d = json.load(f)
                self.Employees["SuperAdministrators"] = d["Employees"]["SuperAdministrators"]
                self.Employees["SystemAdministrators"] = d["Employees"]["SystemAdministrators"]
                self.Employees["Advisors"] = d["Employees"]["Advisors"]

    def ReadClients(self):
        with open(self.Path) as f:
            d = json.load(f)
            self.Clients = d.Clients
            print(d)

    def writeData(self):
        with open(self.Path, 'w', encoding='utf-8') as f:
            data = json.dumps(self, indent=4, cls=ContextEncoder)
            f.write(data)

class ContextEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Employee : 
    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

    def AddClient(self, fullname, address, email, phone):
        

class SystemAdministrator(Employee):
    def __init__(self, Username, Password):
        super().__init__(Username, Password)

    #Adding a new user should only be possible by the SuperAdministrator
    def AddNewAdvisor (self, context, employee):
        context.Employees["Advisors"].append(employee)
        context.writeData()

class SuperAdministrator(SystemAdministrator):
    def __init__(self, Username, Password):
        super().__init__(Username, Password)

    def AddNewSystemAdministrator(self, context, employee):
        context.Employees["SystemAdministrators"].append(employee)
        context.writeData()

class Advisor(Employee):
    def __init__(self, Username, Password):
        super().__init__(Username, Password)




def checkUsernameExists(context, username):
    global user, securityClearance, SecurityClearance
    for employee in context.Employees["SuperAdministrators"]:
        if employee["Username"] == username:
            securityClearance = SecurityClearance.ONE
            user = employee
            return True
    for employee in context.Employees["SystemAdministrators"]:
        if employee["Username"] == username:
            securityClearance = SecurityClearance.TWO
            user = employee
            return True
    for employee in context.Employees["Advisors"]:
        if employee["Username"] == username:
            securityClearance = SecurityClearance.THREE
            user = employee
            return True
    return False

def checkPassword(password):
    global user
    if password == user["Password"]:
        return True
    return False

def login(context):
    global securityClearance
    username = input("Username: ")
    if checkUsernameExists(context, username):
        password = input("Password: ")
        cnt = 1
        correctPassword = checkPassword(password)
        while not correctPassword  and cnt < 3:
            print("Wrong password! You have ", 3-cnt, " tries left.")
            password = input("Password: ")
            correctPassword = checkPassword(password)
            cnt = cnt + 1
        if correctPassword:
            return True
        else:
            exit            
    else:
        print("this username does not exist. Please check your spelling and try again.")
        login(context)

def validateUsername(username):
    if username.count >= 5 and username.count <= 20:
        #TODO: insert other if statements validating the username
        print("valid username")
    else:
        print("The username should have a length between 5 and 20 characters.")

def showMenu(context):
    global securityClearance,SecurityClearance
    if securityClearance == SecurityClearance.ONE:
        print("SuperAdministrators menu")
        #TODO: implement SuperAdministrators menu
    elif securityClearance == SecurityClearance.TWO:
        print("SystemAdministrators menu")
        #TODO: implement SystemAdministrators menu
    else:
        print("Advisors menu")
        #TODO: implement Advisors menu

def main():
    context = Context()
    context.ReadEmployees()
    if context.Employees["SuperAdministrators"] == []:
        init(context)
    if login(context):
        print("You have succesfully logged in.")
        print("Your securityLevel is ", securityClearance)
        showMenu(context)

def init(context):
    sa = SuperAdministrator("GuusJoppe", "Testje")
    sysadmin1 = SystemAdministrator("LaurensMaas", "Testje2")
    sysadmin2 = SystemAdministrator("JohnDoe", "Appelflap")
    advisor1 = Advisor("Bobage", "algoritms")
    context.Employees["SuperAdministrators"].append(sa)
    sa.AddNewSystemAdministrator(context, sysadmin1)
    sa.AddNewSystemAdministrator(context, sysadmin2)
    sysadmin1.AddNewAdvisor(context, advisor1)
    context.writeData()

if __name__ == "__main__":
    main()




