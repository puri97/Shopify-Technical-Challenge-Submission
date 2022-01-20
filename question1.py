import os
import pandas as pd
from google import Create_Service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
spreadsheet_id = '16i38oonuX1y1g7C_UAmiK9GkY7cS-64DfiDMNiR41LM'

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

response = service.spreadsheets().values().get(
  spreadsheetId=spreadsheet_id,
  majorDimensions='ROWS',
  range='A1:G5'
).execute()

columns=response['values'][0]
data=response['values'][1:]
df= pd.DataFrame(data,columns=columns)

avg_val = df['order_amount'].mean()

#The total items is an important metric here since only 
#few users have purchased large number of items. The AOV 
#would reduce if we find a range of number of orders placed
# by most users and then calculate the average order value.