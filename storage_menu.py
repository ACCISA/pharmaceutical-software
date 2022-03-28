import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client1 = gspread.authorize(creds)

userDBF = client1.open('PharmaDB').get_worksheet(1)

print("==============================================")
print("-----------------Prototype XBD----------------")
print("----------------------------------------------")
print("-----------------Storage Menu-----------------")
print("----------------------------------------------")
print("------------------Total Units-----------------")
userDBFcol = userDBF.col_values(1)
userDBFrange = (len(userDBFcol))
print(f"---------------------[{userDBFrange}]---------------------")
print("==============================================")
print("-----------------1. Inventory-----------------")
print("-----------------2. Main Menu-----------------")
print("==============================================")
print("Awaiting Response...")
response = input()

if int(response) == 1:
    exec(open("storage\storage_inventory.py").read())

if int(response) == 2:
    exec(open("menu.py").read())
