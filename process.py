import gspread
import pprint
from pprint import pprint
import asyncio
from asyncio import sleep
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client1 = gspread.authorize(creds)

quant = client1.open("PharmaDB").get_worksheet(1)
sheet = client1.open("PharmaDB").get_worksheet(2)
data = sheet.get_all_values()

demand = ['X123','X567','X908']


async def verification():
    while True:
        quantity = quant.col_values(2)
        print(quantity)
        x = 0
        if str(x) in quantity:
            print('empty tray')
            location = quant.findall(str(x))
            for i in location:
                locationRow = i.row
                locationCell = quant.acell(f'C{locationRow}').value
                locationCellNumb = quant.acell(f'A{locationRow}').value
                print(f"Pill Number: {locationCellNumb}; Location: {locationCell}")
            break
        else:
            print(1)
            await asyncio.sleep(5)
            print('awaited')
            continue

async def process(list):
    print('Process Started')
    print('=====================')
    print('Verifying Order')
    print('=====================')
    for i in range(len(list)):
        nameVer = quant.find(str(list[i]))
        if nameVer == None:
            print('=====================')
            print(f'{list[i]} Not Found')
            print('=====================')
            break
        if nameVer != None:
            continue
    for i in range(len(list)):
        x = 0
        pillFind = quant.find(str(list[i]))
        pillRow = pillFind.row
        pillQuant = quant.acell(f'B{pillRow}').value
        completion = range(len(list))
        if pillQuant == x or pillQuant == str(x):
            pillQuantLocation = quant.acell(f'C{pillRow}').value
            print('=====================')
            print(f'{list[i]} Empty Tray')
            print(f'Location: {pillQuantLocation}')
            print('=====================')
            print('Order Failed')
            break
        if pillQuant != x or pillQuant != str(x):
            if (i+1) == len(list):
                print('Order Complete')
            continue


# asyncio.run(verification())
asyncio.run(process(demand))