babies=[]
def arambam(values):
        from datetime import datetime
        today=[]
        bcheck=[]
        check=[]
        bcheckl=[]
        now = datetime.now()
        
        datef= now.strftime("%m/%d")




        

        for i in range(0,5):
                if (i==0):
                        if (datef[i])!='0':
                                print(datef[i])
                                today.append(datef[i])
                elif (i==3):
                        if datef[i]!='0':
                                today.append(datef[i])
                else:
                        if datef[i]!="/":
                                today.append(datef[i])
          
        




        for m in values:
                
                if (len(m)==5):
                        bcheck=[]
                        check=[]
                        bcheck.append(m[4])
        
                        for j in bcheck:
        
                
                                for k in range(0,(len(j)-5)):
                                        if (j[k]!='/' and j[k]!='-'):
                                                check.append(j[k])
                
                                        if check==today:
                                                
                                                print(m[1],m[2])
                                                babies.append(m[2])
                                                return babies

        

from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE ="keys.json"
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID  spreadsheet.
SAMPLE_SPREADSHEET_ID = '1i4hCrcfJAUXK0GsAUOkJdUPW7dNWbM9wdeNP5AYcS5I' 
service = build('sheets', 'v4', credentials=creds)

 # Call the Sheets API
sheet = service.spreadsheets()
from datetime import datetime
today=[]
bcheck=[]
check=[]
bcheckl=[]
now = datetime.now()
print("special ones of",now.strftime("%d/%m/%Y"),";")
print("**************CSA***************")
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="CSA!A2:E65").execute()
valuesCSA = result.get('values', [])
arambam(valuesCSA)
print(babies)

print("**************CSB***************")
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="CSB!A2:E65").execute()
valuesCSB = result.get('values', [])
arambam(valuesCSB)
print(babies)
print("**************MECH***************")
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="ME!A2:E65").execute()
valuesME = result.get('values', [])
arambam(valuesME)

print("**************EBE***************")
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="EBE!A2:E65").execute()
valuesEBE = result.get('values', [])
arambam(valuesEBE)
print(babies)

print("**************EEE***************")
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="EEE!A2:E65").execute()
valuesEEE = result.get('values', [])
arambam(valuesEEE)

print("**************ECA***************")
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="ECA !A2:E65").execute()
valuesECA = result.get('values', [])
arambam(valuesECA)

print("**************ECB***************")
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="ECB !A2:E65").execute()
valuesECB = result.get('values', [])
arambam(valuesECB)

import pywhatkit
from datetime import datetime
hr=datetime.now()

import pywhatkit
from datetime import datetime
hr=datetime.now()
import os

#pywhatkit.sendwhatmsg('+919446891404','hai',00,8)
hrh=hr.hour
hrm=hr.minute+2
if (hrm>=60):
    hrm=(hrm-60)
    hrh=hrh+1
    if (hrh>=24):
        hrh=0

print(hrh)
print(hrm)
c=""
k="It's "

k+=now.strftime("%d/%m/%Y")

k=k+os.linesep +"so what's  Special today Yeee its their Birthday :"
for i in babies:
    c=c+os.linesep+i
k=k+c

print(k)
pywhatkit.sendwhatmsg('+919400234303',k,hrh,hrm)

