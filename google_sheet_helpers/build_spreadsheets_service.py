from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def build_spreadsheets_service(path_to_token):
    creds = Credentials.from_authorized_user_file(path_to_token)
    service = build('sheets', 'v4', credentials=creds)
    sheets_service = service.spreadsheets()
    return sheets_service