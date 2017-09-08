from os import system
from time import sleep
class User:
    # Define the fields and methods for your object here.
    # Every user has a username and friends
    # You have to be able to get(show) the username and friends list
    def __init__(self): #initialize what every user has - constructor
        self.name = ""
        self.userID = ""        #A specific number for each user you have to generate
        self.friends = []       #friend list, initil. is empty
        
    def getName(self): #Getter method, private to the user
        print(self.name)
            
    def getUserID(self):
        print(self.userID)
            
    def assignUserName(self):
        self.name = input("What would you like your username to be? ")    
                  
class Network:
    # Constructor initializes an empty list of users
    def __init__(self):
        self.users = [] #The users index is their userID
        
    def getUsers(self): #Getter method
        for user in self.users:
            user.getName()
            
    def addUser(self):
        newUser = User()            
        newUser.assignUserName()
        self.users.append(newUser)            
            
    def getConnections(self):
        nameToSearch = input("What is the name of the user? ")
        
        
        print(self.findUser(nameToSearch).friends)
        
        
    def addFriends(self):
        user = input("What is the username of the first user? ")
        friend = input("What is the username of the second user? ")
        self.findUser(user).friends.append(self.findUser(friend).name)
        self.findUser(friend).friends.append(self.findUser(user).name)
        
    def removeConnection
    (self):
        
        user = input("What is the username of the first user? ")
        friend = input("What is the username of the second user? ")
        self.findUser(user).friends.remove(self.findUser(friend).name)
        self.findUser(friend).friends.remove(self.findUser(user).name)
    
    def findUser(self, nameToSearch): #userName because it's a string
        error = "There is an error, either this user does not exist or you suck."   
        for user in self.users:
            if user.name == nameToSearch: #user.name is the string, user is the User datatype
                return user
#            else:
#                return error

    def prompt(self):
        print("Hey, welcome to this really bad social network called BadChat, because you can't chat and this is really bad.")
        print("")
        print("Type (a) if you want to add a user")
        print("Type (ac) to add a connection")
        print("Type (p) to print the users")
        print("Type (pc) to print connections")
        print("Type (r) to remove a connection")
        print("Type (q) to exit")
            
        promptAnswer = input("What would you like to do? ")
        
        if promptAnswer == "a":
            self.addUser()
        elif promptAnswer == "ac":
            self.addFriends()
        elif promptAnswer == "p":
            self.getUsers()
        elif promptAnswer == "pc":
            self.getConnections()
        elif promptAnswer == "r":
            self.removeConnection()
        elif promptAnswer == "q":
            print("Goodbye!!")
            sleep(2)
            exit()

newSocialNetwork = Network()

while True:
    newSocialNetwork.prompt()
