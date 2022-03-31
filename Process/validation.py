import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client1 = gspread.authorize(creds)

validDBF = client1.open('PharmaDB').get_worksheet(6)

def validation_check(listPills):
    global validationRow
    for i in range(len(listPills)):
        findPill = validDBF.find(str(listPills[i]))
        if findPill == None:
            global valid
            valid = True
            pass
        if findPill != None:
            findPillRow = findPill.row
            validationRow = validDBF.row_values(findPillRow)
            target = 0
            for i in range(len(listPills)):
                if target == 1:
                    valid = False
                    break
                if listPills[i] in validationRow:
                    target += 1
                    continue
                else:
                    valid = True

