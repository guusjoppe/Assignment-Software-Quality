import os
from os import listdir
from os.path import isfile, join
import json

from context import Context
from context import ContextEncoder
from context import Address
from context import Client
from context import Employee
from context import SuperAdministrator
from context import SystemAdministrator
from context import Advisor

from validation import validateUsername

global user, securityClearance

def enum(**enums):
    return type('Enum', (), enums)

SecurityClearance = enum(ONE="SuperAdministrator",TWO="SystemAdministrator", THREE="Advisor")
Cities = enum(ONE= "Rotterdam", TWO="Amsterdam", THREE="Utrecht", FOUR="Breda", FIVE="Delft",
                SIX="Leiden", SEVEN="Arnhem", EIGHT="Eindhoven", NINE="Nijmegen", TEN="Tilburg" )


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




