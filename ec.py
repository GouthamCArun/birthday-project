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

result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="ECA !A2:E65").execute()
values=result.get('values', [])
print(values)
