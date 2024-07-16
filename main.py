# main.py
from user import User
from user_file_manager import UserFileManager
import sqlite3

eop = False

def showMenu():
    print("0: Exit")
    print("1: Define User")
    print("2: Set password for user")
    print("3: Remove User")
    print("4: Get Users list")
    print("5: Reset User Password")
    print("6: Change User Name")

def defineUser():
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    role = input("Enter role: ")
    user = User(id, name, role)
    UserFileManager.saveUserToDB(user)

def setPasswordForUser():
    id = input("Enter user ID: ")
    user = UserFileManager.getUserFromDB(id)
    if user:
        password = input("Enter new password: ")
        user.setPassword(password)
        UserFileManager.updateUserInDB(user)
        print("Password set successfully.")
    else:
        print("User not found.")

def removeUser():
    id = input("Enter user ID: ")
    user = UserFileManager.getUserFromDB(id)
    if user:
        UserFileManager.removeUserFromDB(user)
        print("User removed successfully.")
    else:
        print("User not found.")

def showUserList():
    users = UserFileManager.getUsersFromDB()
    for user in users:
        print(user)

def resetUserPassword():
    id = input("Enter user ID: ")
    user = UserFileManager.getUserFromDB(id)
    if user:
        password = input("Enter new password: ")
        user.setPassword(password)
        UserFileManager.updateUserInDB(user)
        print("Password reset successfully.")
    else:
        print("User not found.")

def changeUserName():
    id = input("Enter user ID: ")
    user = UserFileManager.getUserFromDB(id)
    if user:
        new_name = input("Enter new name: ")
        user.name = new_name
        UserFileManager.updateUserInDB(user)
        print("Name changed successfully.")
    else:
        print("User not found.")

while not eop:
    showMenu()
    choice = input("Enter your choice: ")

    match choice:
        case "0":
            eop = True
        case "1":
            defineUser()
        case "2":
            setPasswordForUser()
        case "3":
            removeUser()
        case "4":
            showUserList()
        case "5":
            resetUserPassword()
        case "6":
            changeUserName()
        case _:
            print("Invalid choice. Please try again.")