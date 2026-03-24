# Function to upload a file to Google Drive and get a shareable link
def upload_file_to_drive(filepath, filename, parent_folder_id=None):
    """Uploads a file to Google Drive, handles existing files, and sets shareable permissions.

    Args:
        filepath (str): Local path to the file to be uploaded.
        filename (str): Desired filename in Google Drive.
        parent_folder_id (str, optional): Google Drive ID of the parent folder. Defaults to None (root).

    Returns:
        str: Shareable webViewLink for the uploaded file, or None if upload fails.
    """
    try:
        # Check if a file with the same name already exists in the target folder.
        query = f"name='{filename}' and trashed=false"
        if parent_folder_id:
            query += f" and '{parent_folder_id}' in parents"

        response = drive_service.files().list(q=query, spaces='drive', fields='files(id, webViewLink)').execute()
        file_list = response.get('files', [])

        file_metadata = {
            'name': filename,
            'mimeType': 'image/png' # Set MIME type for PNG image.
        }
        if parent_folder_id:
            file_metadata['parents'] = [parent_folder_id] # Assign to the specified parent folder.

        media = MediaFileUpload(filepath, mimetype='image/png', resumable=True)

        if file_list:
            # If the file exists, update its content.
            file_id = file_list[0]['id']
            updated_file = drive_service.files().update(
                fileId=file_id,
                media_body=media,
                fields='id, webViewLink' # Request ID and link in response.
            ).execute()
            print(f"Updated existing file on Google Drive: {filename}")
            shareable_link = updated_file.get('webViewLink')
            target_file_id = file_id
        else:
            # If the file does not exist, create a new one.
            created_file = drive_service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id, webViewLink'
            ).execute()
            print(f"Uploaded new file to Google Drive: {filename}")
            shareable_link = created_file.get('webViewLink')
            target_file_id = created_file['id']

        # Set permissions to make the file shareable (Anyone with the link can view).
        drive_service.permissions().create(
            fileId=target_file_id,
            body={'type': 'anyone', 'role': 'reader'},
            fields='id'
        ).execute()

        return shareable_link
    except Exception as e:
        print(f"Error uploading {filename} to Google Drive: {e}")
        return None

