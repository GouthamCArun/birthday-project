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
                            range="ECA !A2:E65").execute()
valuesCSA = result.get('values', [])
print(valuesCSA)
print(valuesCSA[2])