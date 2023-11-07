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
