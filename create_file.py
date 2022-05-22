import gspread
import os
import pprint
from pprint import pprint
import asyncio
from asyncio import sleep
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client1 = gspread.authorize(creds)

clientDBF = client1.open('PharmaDB').get_worksheet(3)
rowSet = 3
for i in range(10):
    if i == 1 or i ==0:
        continue
    else:
        list = clientDBF.row_values(i)
        format = ['Client_ID: ','First_Name: ','Last_Name: ','Sex: ','Age: ','Address: ','Phone_Number: ','Order_Number: ','Validity: ']
        with open(f'Prescriptions/prescription_{i}.txt', 'w') as f:
            print(list)
            f.write(str(list))
    print('File Created')