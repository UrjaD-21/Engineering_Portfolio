from googleapiclient.discovery import build
import google.auth

def authenticate_drive():
    credentials, _ = google.auth.default()
    return build('drive', 'v3', credentials=credentials)
