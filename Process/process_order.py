import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client1 = gspread.authorize(creds)

storageDBF = client1.open('PharmaDB').get_worksheet(1)
clientDBF = client1.open('PharmaDB').get_worksheet(3)
orderDBF = client1.open('PharmaDB').get_worksheet(4)
tempDBF = client1.open('PharmaDB').get_worksheet(5)

def count(list):
    global listCount
    listCount = []
    for i in range(len(list[0][0])):
        if ',' in list[0][0][i]:
            tempDivide = list[0][0][i].split(',')
            for i in range(len(tempDivide)):
                try:
                    turn = int(tempDivide[i])
                    test = turn + 1
                    listCount.append(tempDivide[i])
                    continue
                except:
                    continue
        else:
            try:
                turn = int(list[0][0][i])
                test = turn + 1
                listCount.append(list[0][0][i])
                continue
            except:
                continue




print("==============================================")
print("-----------------Prototype XBD----------------")
print("----------------------------------------------")
print("------------------Oder Process----------------")
print("==============================================")
print("--------------1. Batch Process----------------")
print("--------------2. Process Specific Order-------")
print("--------------3. Main Menu--------------------")
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
                    try:
                        turn = int(orderData[0][0][i])
                        test = turn + 1
                        continue
                    except:
                        if orderData[0][0][i] == 'NONE':
                            continue
                        else:
                            pills.append(orderData[0][0][i])

            print(f'pills are {pills}')
            pillsOnly = pills
            count(orderData)
            if len(pills) > 0:
                pills = list(dict.fromkeys(pills))
                if len(pills) == 1:
                    oneTotal = 0
                    for i in range(len(listCount)):
                        oneTotal += int(listCount[i])
                    sequence.insert(0, "----")

                    filler = [pills[0]]
                    for i in range(len(sequence)-1):
                        filler.append('X')
                    print(sequence)
                    print(filler)
                    width = len(sequence)
                    print("==============================================")
                    print("-----------------Prototype XBD----------------")
                    print("----------------------------------------------")
                    print("------------------Oder Process----------------")
                    print("==============================================")
                    print("----------------Tray Dimensions---------------")
                    print(f"------------length: 2 ----width: {width}-----------")
                    print("==============================================")
                    print(f"--------------Inventory Status---------------")
                    print(f"---------------------------------------------")
                    searchPill = storageDBF.find(pills[0])
                    searchPillRow = searchPill.row
                    pillQuant = storageDBF.acell(f'B{searchPillRow}').value
                    location = storageDBF.acell(f'C{searchPillRow}').value
                    if int(pillQuant) == 0:
                        print(f"Tray {pills[0]} is empty")
                        print(f"Location: {location}")
                    else:
                        print(f"--------------{pills[0]}: {pillQuant}--------------------")
                        print("==============================================")

                    if int(pillQuant) - int(oneTotal) <= 0:
                        print(f"Tray {pills[0]}, insufficient quantity")
                        print(f"Location: {location}")
                        print("==============================================")
                        exec(open("Process\process_order.py").read())
                    if int(pillQuant) - int(oneTotal) > 0:
                        print("==============================================")
                        print("Order Processed")
                        print("==============================================")
                        newQuant = int(pillQuant) - int(oneTotal)
                        updateQuant = storageDBF.update(f'B{searchPillRow}', str(newQuant))
                        exec(open("Process\process_order.py").read())

                else:
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
                    print("----------------Tray Dimensions---------------")
                    print(f"----length: {length+1}----width: {width}---------------------")
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
                        print(f"--------------{pills[i]}: {quantity}--------------------")
                    print("==============================================")
                    # print(f'pills only: {pillsOnly}')
                    # print(f'quant only" {listCount}')
                    print(pills)
                    for i in range(len(pills)):
                        perm = pills[i]
                        totalCount = [pills[i]]
                        permI = i
                        for i in range(len(pillsOnly)):
                            if i == 0:
                                if pillsOnly[i] == totalCount[0]:
                                    totalCount.append(listCount[i])
                                    print(totalCount)
                                if pillsOnly[i] != totalCount[0]:
                                    for i in range(len(pillsOnly)):
                                        if pillsOnly[i] == totalCount[0]:
                                            totalCount.append(listCount[i])
                                            startingNumb = int(listCount[i])
                                            break
                                        else:
                                            continue
                                    continue
                            else:
                                if pillsOnly[i] == totalCount[0]:
                                    update = int(totalCount[1]) + int(listCount[i])
                                    totalCount.clear()
                                    totalCount.append(perm)
                                    totalCount.append(update)
                                    if i+1 == len(pillsOnly) and permI != 0:
                                        lastUpdate = int(totalCount[1]) - startingNumb
                                        totalCount.clear()
                                        totalCount.append(perm)
                                        totalCount.append(lastUpdate)
                                        print(totalCount)
                                        tempDBF.append_row(totalCount)
                                        for i in range(len(pills)):
                                            findPill = storageDBF.find(pills[i])
                                            if findPill == None:
                                                print('ERROR, Pill not Found')
                                            if findPill != None:
                                                findPillRow = findPill.row
                                                findPillQuant = storageDBF.acell(f'B{findPillRow}').value
                                                location = storageDBF.acell(f'C{findPillRow}').value
                                                if int(findPillQuant) <= 0:
                                                    print(f"Tray {pills[i]} is empty")
                                                    print(f"Location: {location}")
                                                if int(findPillQuant) > 0:
                                                    findPilli = tempDBF.find(str(pills[i]))
                                                    findPilliRow = findPilli.row
                                                    findPilliQuant = tempDBF.acell(f'B{findPilliRow}').value
                                                    if int(findPillQuant) - int(findPilliQuant) <= 0:
                                                        print(f'Tray {pills[i]}, insufficient quantity')
                                                        print(f'location: {location}')
                                                    if int(findPillQuant) - int(findPilliQuant) > 0:
                                                        print(f'{pills[i]} Processed')
                                                        newQuanti = int(findPillQuant) - int(findPilliQuant)
                                                        storageDBF.update(f'B{findPillRow}', newQuanti)
                                        print("==============================================")
                                        print("Order Processed")
                                        print("==============================================")
                                        tempDBF.clear()
                                        exec(open("Process\process_order.py").read())

                                    continue
                                else:
                                    print('not updated')
                                    print(f'at index{i}')
                                    print(totalCount)
                                    if i + 1 == len(pillsOnly) and permI != 0:
                                        print('this happend')
                                        lastUpdate = int(totalCount[1]) - startingNumb
                                        totalCount.clear()
                                        totalCount.append(perm)
                                        totalCount.append(lastUpdate)
                                        print(totalCount)
                                        tempDBF.append_row(totalCount)
                                        print(f'finished for {totalCount[permI]}')
                                        quantData = tempDBF.get_all_records()
                                        print(quantData)
                                        for i in range(len(pills)):
                                            searchQuant = storageDBF.find(pills[i])
                                            searchQuantRow = searchQuant.row
                                            QuantSearch = storageDBF.acell(f'B{searchQuantRow}').value
                                            location = storageDBF.acell(f'C{searchQuantRow}').value
                                            if int(QuantSearch) <= 0:
                                                print(f"Tray {pills[i]} is empty")
                                                print(f"Location: {location}")
                                            else:
                                                for i in range(len(pills)):
                                                    searchTemp = tempDBF.find(str(pills[i]))
                                                    searchTempRow = searchTemp.row
                                                    quantTemp = tempDBF.acell(f'B{searchTempRow}').value
                                                    if int(QuantSearch) - int(quantTemp) <= 0:
                                                        print(f'Tray {pills[i]}, insufficient quantity')
                                                        print(f'location: {location}')
                                                    elif int(QuantSearch) - int(quantTemp) > 0:
                                                        print('Order Processed')
                                                        newQuant = int(QuantSearch) - int(quantTemp)
                                                        storageDBF.update(f'B{searchTemp}', str(newQuant))
                                                        tempDBF.clear()
                                        print("==============================================")
                                        exec(open("Process\process_order.py").read())

                                    else:
                                        continue
                                    continue
                        if perm == pillsOnly[0]:
                            tempDBF.append_row(totalCount)


            if len(pills) == 0:

                print('Patient Consumes 1 pill a day')
                width = len(sequence)
                length = 1
                print("==============================================")
                print("-----------------Prototype XBD----------------")
                print("----------------------------------------------")
                print("------------------Oder Process----------------")
                print("==============================================")
                print("----------------Tray Dimensions---------------")
                print(f"----length: {length+1}----width: {width}---------------------")
                print("==============================================")
                print(f"--------------Inventory Status---------------")
                print(f"---------------------------------------------")
    else:
        print('Invalid Input')
        exec(open("Process\process_order.py").read())

if int(response) == 3:
    exec(open("menu.py").read())



