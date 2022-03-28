import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client1 = gspread.authorize(creds)

storageDBF = client1.open('PharmaDB').get_worksheet(1)
clientDBF = client1.open('PharmaDB').get_worksheet(3)
orderDBF = client1.open('PharmaDB').get_worksheet(4)
current_order = client1.open('PharmaDB').get_worksheet(5)


print("==============================================")
print("-----------------Prototype XBD----------------")
print("----------------------------------------------")
print("------------------Oder Process----------------")
print("==============================================")
print("--------------1. Batch Process----------------")
print("--------------2. Process Specific Order-------")
print("==============================================")
print("Awaiting Response...")
response = input()

if int(response) == 1:
    print('Batch Process Started')
if int(response) == 2:
    print("==============================================")
    print("Client ID...")
    print("==============================================")
    responseID = input()
    if int(responseID) >= 99:
        findID = clientDBF.find(str(responseID))
        if findID == None:
            print("==============================================")
            print("Client ID Not Found")
            print("==============================================")
        if findID != None:
            #data recognition
            findIDRow = findID.row
            orderNumb = clientDBF.acell(f'H{findIDRow}').value
            orderNumbData = orderDBF.find(str(orderNumb))
            orderNumbDataRow = orderNumbData.row
            orderData = orderDBF.batch_get([f'B{orderNumbDataRow}:O{orderNumbDataRow}'])
            days = (len(orderData[0][0]))/2
            x = 0
            sequence = []
            for i in range(int(days)*(2)):
                if orderData[0][0][i] == 'NONE':
                    x +=1
                    continue
                else:
                    days = ['M', '-', 'T', '-', 'W', '-', 'Th','-', 'F', '-', 'S', '-', 'Su', '-']
                    sequence.append(days[i])
                    continue

            print(f'sequence initial {sequence}')
            for i in range(int(len(sequence)/2)+1):
                if sequence[i] == '-':
                    sequence.remove('-')
                    continue
                else:
                    continue
            print(x/2)
            print(sequence)

            print('data rec')
            pills = []
            for i in range(len(orderData[0][0])):
                if ',' in orderData[0][0][i]:
                    day = orderData[0][0][i].split(',')
                    for i in range(len(day)):
                        try:
                            turn = int(day[i])
                            test = turn + 1
                            continue
                        except:
                            pills.append(day[i])
                        else:
                            continue

                if ',' not in orderData[0][0][i]:
                    continue
            print(f'pills are {pills}')
            if len(pills) > 0:
                pills = list(dict.fromkeys(pills))
                sequence.insert(0, "----")
                print(sequence)
                for i in range(len(pills)):
                    filler = []
                    filler.append(pills[i])
                    for i in range(len(sequence) - 1):
                        filler.append('X')
                    print(filler)
                width = len(sequence)
                length = len(pills)
                print("==============================================")
                print("-----------------Prototype XBD----------------")
                print("----------------------------------------------")
                print("------------------Oder Process----------------")
                print("==============================================")
                print(f"----length: {length}----width: {width}--------------")
                print("==============================================")
                print(f"--------------Inventory Status---------------")
                print(f"---------------------------------------------")
                for i in range(len(pills)):
                    inventorySearch = storageDBF.find(str(pills[i]))
                    invRow = inventorySearch.row
                    quantity = storageDBF.acell(f'B{invRow}').value
                    if int(quantity) == 0:
                        location = storageDBF.acell(f'C{invRow}').value
                        print("==============================================")
                        print(f"Tray {pills[i]} is empty")
                        print(f"Location: {location}")
                        print("==============================================")
                    print(f"---------------------{pills[i]}: {quantity}---------------------")
                print("==============================================")



            if len(pills) == 0:
                print('Patient Consumes 1 pill a day')
                width = len(sequence)
                length = 1
                print("==============================================")
                print("-----------------Prototype XBD----------------")
                print("----------------------------------------------")
                print("------------------Oder Process----------------")
                print("==============================================")
                print(f"----length: {length}----width: {width}----------------")

    else:
        print('Invalid Input')
        exec(open("Process\process_order.py").read())


