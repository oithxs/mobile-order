import gspread
import datetime
from pytz import timezone
import random
import os
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv()

CREDENTIAL_JSON = {
  "type": "service_account",
  "project_id": os.environ['SHEET_PROJECT_ID'],
  "private_key_id": os.environ['SHEET_PRIVATE_KEY_ID'],
  "private_key": os.environ['SHEET_PRIVATE_KEY'],
  "client_email": os.environ['SHEET_CLIENT_EMAIL'],
  "client_id": os.environ['SHEET_CLIENT_ID'],
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.environ['SHEET_CLIENT_X509_CERT_URL']
}

def get_time():
  now = datetime.datetime.now(timezone('Asia/Tokyo'))
  return now.time().strftime('%X')

def next_available_row(worksheet):
  str_list = list(filter(None, worksheet.col_values(2)))
  return str(len(str_list)+1)

def main(order_item):
  # ランダム生成されるID
  ORDER_ID = random.randint(100,999)
  SPREADSHEET_ID = os.environ['SPREADSHEET_ID']

  scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_dict(CREDENTIAL_JSON, scope)

  # 認証情報を使ってスプレッドシートの操作権を取得
  gs = gspread.authorize(credentials)
  worksheet = gs.open_by_key(SPREADSHEET_ID).sheet1

  # 書き込み可能な行を取得
  next_row = next_available_row(worksheet)

  # IDを書き込む
  worksheet.update_cell(next_row,1,ORDER_ID)
  # 個数を書き込む
  worksheet.append_row(order_item,table_range='B'+ next_row)
  # 時間を書き込む
  worksheet.update_cell(next_row,8,get_time())

  # 降順にソート
  worksheet.sort((8,'des'))

  return ORDER_ID