from google_auth_oauthlib.flow import InstalledAppFlow

def use_creds_to_refresh_access_token(path_to_credentials, path_to_token):    
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    flow = InstalledAppFlow.from_client_secrets_file(path_to_credentials, scopes)
    creds = flow.run_local_server(port=0)
    with open(path_to_token, 'w') as token:
        token.write(creds.to_json())