import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client1 = gspread.authorize(creds)

storageDBF = client1.open('PharmaDB').get_worksheet(1)


print("==============================================")
print("-----------------Prototype XBD----------------")
print("----------------------------------------------")
print("---------------Storage Menu: Data-------------")
print("----------------------------------------------")
print("----------------------------------------------")
print("---------------Insert Pill Number...----------")
print("==============================================")

response = input()
findPill = storageDBF.find(str(response))
if findPill == None:
    print("-------------------------")
    print("Pill Number Not Found")
    print("-------------------------")
    exec(open("storage\storage_data.py").read())
if findPill != None:
    findPillRow = findPill.row
    findPillValue = storageDBF.cell(findPillRow,2).value
    print("==============================================")
    print("-----------------Prototype XBD----------------")
    print("----------------------------------------------")
    print("---------------Storage Menu: Data-------------")
    print("----------------------------------------------")
    print(f"---------------Pill Number: {response}-------------")
    print(f"--------------Pill Quantity: {findPillValue}---------------")
    print("==============================================")
    print("-----------------1. Edit Quantity-------------")
    print("-----------------2. Edit Pill Number----------")
    print("-----------------3. Main Menu-----------------")
    print("==============================================")
    response2 = input()
    if int(response2) == 1:
        print("-------------------------")
        print("Insert New Quantity")
        print("-------------------------")
        newQuantity = input()
        findPillRow = findPill.row
        storageDBF.update(f"B{findPillRow}",str(newQuantity))
        print("-------------------------")
        print("Quantity Updated")
        print("-------------------------")
        exec(open("menu.py").read())

    if int(response2) == 2:
        while True:
            print("-------------------------")
            print("Insert New Pill Number")
            print("-------------------------")
            newNumb = input()
            newNumbFind = storageDBF.find(str(newNumb))
            if newNumbFind == None:
                newNumbFindRow = findPill.row
                storageDBF.update(f"A{newNumbFindRow}",str(newNumb))
                print("-------------------------")
                print("Pill Number Updated")
                print("-------------------------")
                exec(open("storage\storage_data.py").read())
            if newNumbFind != None:
                print("-------------------------")
                print("Change Fail, Duplicate ")
                print("-------------------------")
                print(newNumbFind)
                print("=========================")
                print("--------1. Return--------")
                print("-------2. Try Again------")
                print("=========================")
                awaitRep = input()
                if int(awaitRep) == 1:
                    exec(open("storage\storage_data.py").read())
                if int(awaitRep) == 2:
                    continue


    if int(response2) == 3:
        exec(open("menu.py").read())












