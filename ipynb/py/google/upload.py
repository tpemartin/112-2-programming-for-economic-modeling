from __future__ import print_function

import io
from googleapiclient.http import MediaIoBaseUpload
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def getwd():
    return os.getcwd()

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def auth():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def upload_file_to_folder(localfile="ipynb/gameInfo.json", remotefile="gameInfo-2.json", folder_id="1EdMkDrkSRATLiYMhjnn0Mk2_JFRzsx46"):
    """Insert new file.
    Returns : Id's of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    creds = auth()
    
    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': remotefile,
            'parents': [folder_id]
        }
        media = MediaFileUpload(localfile,
                                mimetype='application/json')
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()
        print(F'File ID: {file.get("id")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file

def create_folder_with_parentFolder(folder_name="game-id", parent_folder_id="1Z4Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z1Z"):
    """Insert new file.
    Returns : Id's of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    creds = auth()
    
    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parent_folder_id]
        }
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata,
                                      fields='id').execute()
        print(F'File ID: {file.get("id")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file

def upload_string_to_file(string="Hello World", remotefile="gameInfo-2.json", folder_id="1EdMkDrkSRATLiYMhjnn0Mk2_JFRzsx46"):
    """Insert new file.
    Returns : Id's of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    creds = auth()
    
    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': remotefile,
            'parents': [folder_id]
        }
        
        media = MediaIoBaseUpload(io.BytesIO(string.encode('utf-8')),
                                mimetype='application/json', resumable=True)

        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()
        print(F'File ID: {file.get("id")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file
   

def create_folder(folder_name="game/id"):
    """Insert new file.
    Returns : Id's of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    creds = auth()
    
    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata,
                                      fields='id').execute()
        print(F'File ID: {file.get("id")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file


def list_files(folder_id = '1EdMkDrkSRATLiYMhjnn0Mk2_JFRzsx46'):
    creds = auth()
    
    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        
        # replace with your folder ID
        query = f"'{folder_id}' in parents"

        results = service.files().list(q=query, fields='files(id, name)').execute()
        items = results.get('files', [])

        if not items: # means folder is empty
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(f"{item['name']} ({item['id']})")
    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return items

if __name__ == '__main__':
    upload_basic()