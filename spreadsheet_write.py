import os
from Google import Create_Service

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

spreadsheet_id = '1UmE07qORUPJClXwRTP_oUAsXWQPC0HPMQFRTwonM-7Y'
mySpreadsheets = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()


def spreadsheets(val,clas):
  worksheet_name = 'Sheet1!'
  cell_range_insert = 'B2:Z'
  values = (
      (val, clas ),
  )
  value_range_body = {
      'majorDimension': 'ROWS',
      'values': values
  }

  service.spreadsheets().values().append(
      spreadsheetId=spreadsheet_id,
      valueInputOption='USER_ENTERED',
      range=worksheet_name + cell_range_insert,
      body=value_range_body
  ).execute()



