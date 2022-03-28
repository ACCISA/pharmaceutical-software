import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client1 = gspread.authorize(creds)

storageDBF = client1.open('PharmaDB').get_worksheet(1)

print("----------------------------------------------")
print("-----------------Prototype XBD----------------")
print("----------------------------------------------")
print("---------------Storage Menu: List-------------")
print("----------------------------------------------")
userDBFcol = storageDBF.col_values(1)
for i in range(len(userDBFcol)):
    print(f"------------------{i+1}. {userDBFcol[i]}---------------------")
    print("----------------------------------------------")
print("==============================================")
print("-----------------1. Remove -------------------")
print("-------------------2. Add --------------------")
print("--------------3. Storage Data ----------------")
print("-----------------4. Main Menu-----------------")
print("==============================================")
print("Awaiting Response...")
response = input()

if int(response) == 1:
    print("-------------------------")
    print("Insert Pill Number...")
    print("-------------------------")
    pillNumb = input()
    findPill = storageDBF.find(pillNumb)
    if findPill == None:
        print("-------------------------")
        print("Pill Number Not Found")
        print("-------------------------")
        exec(open("storage\storage_inventory.py").read())
    if findPill != None:
        findPillRow = findPill.row
        storageDBF.delete_rows(findPillRow)
        print("-------------------------")
        print("Pill Successfully Removed")
        print("-------------------------")
        exec(open("storage\storage_inventory.py").read())

if int(response) == 2:
    print("-------------------------")
    print("Insert Pill Number...")
    print("-------------------------")
    pillNumb = input()
    findPill = storageDBF.find(str(pillNumb))
    if findPill == None:
        print("-------------------------")
        print("Insert Pill Quantity...")
        print("-------------------------")
        pillQuant = input()
        insertRow = [str(pillNumb), str(pillQuant)]
        storageDBF.append_row(insertRow)
        print("-------------------------")
        print("Data Successfully Added, Returning to Menu")
        print("-------------------------")
        exec(open("storage\storage_inventory.py").read())
    if findPill != None:
        print("-------------------------")
        print("Pill Already Stored")
        print("-------------------------")
        print(findPill)
        print("-------------------------")

if int(response) == 3:
    exec(open("storage\storage_data.py").read())

if int(response) == 4:
    exec(open("menu.py").read())


