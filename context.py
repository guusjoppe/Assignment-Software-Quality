import os
import json
from json import JSONEncoder

class Context :
    def __init__(self):
        self.Employees = {
            "SuperAdministrators" : [],
            "SystemAdministrators" : [],
            "Advisors" : []
        }
        self.Clients = []
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

class Address:
    def __init__(self, Street, Number, ZipCode, City):
        self.Street = Street
        self.Number = Number
        self.ZipCode = ZipCode
        self.City = City


class Client :
    def __init__(self, Fullname, Address, Email, Phone):
        self.Fullname = Fullname
        self.Address = Address
        self.Email = Email
        self.Phone = Phone

class Employee : 
    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

    def AddClient(self, context, fullname, address, email, phone):
        client = Client(fullname, address, email, phone)
        context.Clients.append(client)
        context.writeData()


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
