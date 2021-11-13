import json
import os
class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = list()
        self.isloggedin = False
        self.currentUser = {}

        self.loadUsers()
    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as fl:
                users = json.load(fl)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(newUser)
            print(self.users)
    def register(self,user:User):
        self.users.append(user)
        self.saveToFile()
        print("User saved.")

    def login(self,username,password):

        for user in self.users:
            if user.username == username and user.password == password:
                self.isloggedin = True
                self.currentUser = user
                print("Login Successful!")
                break
    def logout(self):
        self.isloggedin = False
        self.currentUser = {}
        print("Logout Successful!")

    def saveToFile(self):
        ls = list()
        for user in self.users:
            ls.append(json.dumps(user.__dict__))
        with open("users.json","w") as uf:
            json.dump(ls,uf)
    def identity(self):
        if self.isloggedin:
            print(f"Username:{self.currentUser.username}")
        else:
            print("Didn't login!")

repository = UserRepository()
while True:
    print("MENU".center(50,'*'))
    choice = input("1)REGISTER:\n2)LOGIN\n3)LOGOUT\n4)IDENTITY\n5)EXIT\nPlease make a choice:")
    if choice == '5':
        break
    else:
        if choice == '1':

            username = input("Username:")
            password = input("Password")
            email = input("Email")
            user = User(username=username,password=password,email=email)
            repository.register(user)

        elif choice == '2':
            if repository.isloggedin:
                print("Already login")
            else:
                username = input("Username:")
                password = input("Password")
                repository.login(username,password)
        elif choice == '3':
            repository.logout()
        elif choice == '4':
           repository.identity()
        else:
            print("Wrong choice!")

