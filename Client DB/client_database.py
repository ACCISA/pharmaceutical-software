import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client1 = gspread.authorize(creds)

clientDBF = client1.open('PharmaDB').get_worksheet(3)

print("==============================================")
print("-----------------Prototype XBD----------------")
print("----------------------------------------------")
print("----------------Client Database---------------")
print("----------------------------------------------")
rangeData = clientDBF.col_values(1)
print(f"--------------Total Client: {(len(rangeData))-1}---------------")
print("==============================================")
print("-------------1. Search Client-----------------")
print("-------------2. Add Client--------------------")
print("-------------3. Remove Client-----------------")
print("==============================================")
response = input()

if int(response) == 1:
    print("==============================================")
    print("Awaiting Client ID...")
    print("==============================================")
    clientID = input()
    findID = clientDBF.find(str(clientID))
    if findID == None:
        print("==============================================")
        print("Client ID Not Found")
        print("==============================================")
    if findID != None:
        print("==============================================")
        print("-----------------Prototype XBD----------------")
        print("----------------------------------------------")
        print("------------------Client Info-----------------")
        print("----------------------------------------------")
        print("==============================================")

        findIDRow = findID.row
        clientData = clientDBF.row_values(findIDRow)
        print(f'Client Id: {clientData[0]}')
        print(f'Name: {clientData[1]}, {clientData[2]}')
        print(f'Sex: {clientData[3]}')
        print(f'Age: {clientData[4]}')
        print(f'Address: {clientData[5]}')
        print(f'Phone Number: {clientData[6]}')
        print(f'Order Number: {clientData[7]}')
        print("==============================================")
        print("-------------1. Remove Client-----------------")
        print("-------------2. Edit Info---------------------")
        print("-------------3. Process Order-----------------")
        print("-------------4. Return------------------------")
        print("==============================================")
        IDresponse = input()
        if int(IDresponse) == 1:

            first = clientDBF.acell(f'B{findIDRow}').value
            last = clientDBF.acell((f'C{findIDRow}')).value
            print("==============================================")
            print(f'Remove Client {first} {last}')
            print(f'ID: {clientID}')
            print("==============================================")
            print('Awaiting Confirmation, Press 1...')
            print("==============================================")
            confirmationRemoval = input()
            if int(confirmationRemoval) == 1:
                clientDBF.update(f'A{findIDRow}:H{findIDRow}', 'REMOVED')
                print("==============================================")
                print('Client Removed')
                print("==============================================")
                exec(open("Client DB\client_database.py").read())
            else:
                print("==============================================")
                print('Confirmation Failed')
                print("==============================================")
                exec(open("Client DB\client_database.py").read())
        if int(IDresponse) == 2:
            print("==============================================")
            print('-----------------Data Modifier----------------')
            print("==============================================")
            print("-----------------1. Name----------------------")
            print("-----------------2. Sex-----------------------")
            print("-----------------3. Age-----------------------")
            print("-----------------4. Address-------------------")
            print("==============================================")
            print("Awaiting Response...")
            editResponse = input()
            if int(editResponse) == 1:
                print("==============================================")
                print('First Name...')
                print("==============================================")
                first = input()
                print("==============================================")
                print('Last Name...')
                print("==============================================")
                last = input()
                clientDBF.update(f'B{findIDRow}', str(first))
                clientDBF.update(f'C{findIDRow}', str(last))
                print("==============================================")
                print('Client Name Changed')
                print("==============================================")
                exec(open("Client DB\client_database.py").read())
            if int(editResponse) == 2:
                while True:
                    print("==============================================")
                    print('Sex (M or F)...')
                    print("==============================================")
                    gender = input()
                    if str(gender) == 'M' or str(gender) == 'F':
                        print("==============================================")
                        print('Client Sex Changed')
                        print("==============================================")
                        clientDBF.update(f'D{findIDRow}', str(gender))
                        exec(open("Client DB\client_database.py").read())
                    else:
                        print("Wrong Input (M or F)")
                        continue
            if int(editResponse) == 3:
                while True:
                    print("==============================================")
                    print('Age...')
                    print("==============================================")
                    age = input()
                    if age.isdigit() == True:
                        print("==============================================")
                        print('Age Updated')
                        print("==============================================")
                        clientDBF.update(f'E{findIDRow}', str(age))
                        exec(open("Client DB\client_database.py").read())
                    else:
                        print("Wrong Input (Must be Integer)")
                        continue
            if int(editResponse) == 4:
                print("==============================================")
                print('Address...')
                print("==============================================")
                adress = input()
                clientDBF.update(f'F{findIDRow}', str(adress))
                print("==============================================")
                print('Address Address Updated')
                print("==============================================")
                exec(open("Client DB\client_database.py").read())

        if int(IDresponse) == 3:
            print('TBD, ')
        if int(IDresponse) == 4:
            exec(open("Client DB\client_database.py").read())

if int(response) == 2:
    print("==============================================")
    print('-----------------Add Client-------------------')
    print('-----------------Data Needed:-----------------')
    print("==============================================")
    print("--------------------Name----------------------")
    print("--------------------Sex-----------------------")
    print("--------------------Age-----------------------")
    print("--------------------Address-------------------")
    print("--------------------Phone Number--------------")
    print("==============================================")
    print("Press 1 to confirm...")
    print("==============================================")
    confirmation = input()
    if str(confirmation) == '1':
        print("==============================================")
        print('First Name...')
        print("==============================================")
        first = input()
        print("==============================================")
        print('Last Name...')
        print("==============================================")
        last = input()
        while True:
            print("==============================================")
            print('Sex...(M or F)')
            print("==============================================")
            gender = input()
            if str(gender) == 'M' or str(gender) == 'F':
                print("==============================================")
                print('Age...')
                print("==============================================")
                age = input()
                print("==============================================")
                print('Address...')
                print("==============================================")
                address = input()
                print("==============================================")
                print('Phone Number...')
                print("==============================================")
                pn = input()
                colVal = clientDBF.col_values(1)
                generateID = len(colVal)+99
                insertRow = [str(generateID),str(first), str(last), str(gender), str(age), str(address), str(pn)]
                clientDBF.append_row(insertRow)
                print("==============================================")
                print('-----------------Client Added-----------------')
                print("==============================================")
                print(f"             Name: {first}, {last}")
                print(f"             Sex: {gender}")
                print(f"             Age: {age}")
                print(f"             Address: {address}")
                print(f"             Phone Number: {pn}")
                print("==============================================")
                exec(open("Client DB\client_database.py").read())
            else:
                print('Invalid Input')
                continue




    else:
        exec(open("Client DB\client_database.py").read())

if int(response) == 3:
    print("==============================================")
    print('Client ID...')
    print("==============================================")
    requestID = input()
    findRequest = clientDBF.find(str(requestID))
    if int(requestID) >= 100:
        if findRequest == None:
            print("==============================================")
            print('Client ID Not Found')
            print("==============================================")
            exec(open("Client DB\client_database.py").read())
        if findRequest != None:
            row = findRequest.row
            first = clientDBF.acell(f'B{row}').value
            last = clientDBF.acell((f'C{row}')).value
            print("==============================================")
            print(f'Remove Client {first} {last}')
            print(f'ID: {requestID}')
            print("==============================================")
            print('Awaiting Confirmation, Press 1...')
            print("==============================================")
            confirmationRemoval = input()
            if int(confirmationRemoval) == 1:
                clientDBF.update(f'A{row}:H{row}', 'REMOVED')
                print("==============================================")
                print('Client Removed')
                print("==============================================")
                exec(open("Client DB\client_database.py").read())
            else:
                print("==============================================")
                print('Confirmation Failed')
                print("==============================================")
                exec(open("Client DB\client_database.py").read())
    else:
        print("==============================================")
        print('Client ID Not Found')
        print("==============================================")
        exec(open("Client DB\client_database.py").read())



