import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client1 = gspread.authorize(creds)

userDBF = client1.open('PharmaDB').sheet1


print("==============================================")
print("-----------------Prototype XBD----------------")
print("----------------------------------------------")
print("-----------------User Database----------------")
print("----------------------------------------------")
userDBL = userDBF.get_all_records()
for i in range(len(userDBL)):
    print(f"{i + 1}. {userDBL[i]} ")
    print("----------------------------------------------")

print("==============================================")
print("-----------------1. Return to Menu------------")
print("-------------------2. Remove User-------------")
print("---------------------3. Add User--------------")
print("==============================================")


while True:
    returnMenu = input()
    if int(returnMenu) == 1:
        exec(open("menu.py").read())
    if int(returnMenu) == 2:
        print('Awaiting User Index...')
        userIndex = input()
        Id = int(userIndex)+1
        userDBF.delete_rows(Id)
        print('User Deleted')
        exec(open("menu.py").read())
    if int(returnMenu) == 3:
        print('Awaiting Username...')
        NewUser = input()
        print('Awaiting Password...')
        NewPassword = input()
        insertRow = [str(NewUser),str(NewPassword)]
        userDBF.append_row(insertRow)
        print('User Added')
        exec(open("menu.py").read())
    else:
        print("Invalid Input")
        continue
