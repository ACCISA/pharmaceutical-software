from threading import Timer

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client1 = gspread.authorize(creds)

userDBF = client1.open('PharmaDB').sheet1

print("-------------------------")
print("Insert Username...")
print("-------------------------")
username = input()
findUser = userDBF.find(str(username))


if findUser == None:
    print('User Not Found')

if findUser != None:
    print("-------------------------")
    print("Insert Password...")
    print("-------------------------")
    password = input()

    findPass = userDBF.find(str(password))
    if findPass == None:
        print('Invalid Credentials')

    if findPass != None:
        exec(open("menu.py").read())
