from gspread_dataframe import get_as_dataframe

def fetch_participants(gc, spreadsheet_url, worksheet_name):
    sheet = gc.open_by_url(spreadsheet_url)
    worksheet = sheet.worksheet(worksheet_name)

    df = get_as_dataframe(worksheet)
    df = df.dropna(how='all')

    df = df.rename(columns={
        'Upload Passport Size Photo': 'Photo URL'
    })

    if 'Pass Generated' not in df.columns:
        df['Pass Generated'] = ''

    return df, worksheet
