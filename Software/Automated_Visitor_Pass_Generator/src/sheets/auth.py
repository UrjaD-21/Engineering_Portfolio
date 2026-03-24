import gspread
import google.auth

def authenticate_sheets():
    credentials, _ = google.auth.default()
    return gspread.authorize(credentials)
