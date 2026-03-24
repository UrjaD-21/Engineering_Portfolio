def update_links(worksheet, df):
    links = df['Pass Generated'].fillna('').tolist()

    headers = worksheet.row_values(1)
    col_index = headers.index('Pass Generated') + 1

    values = [[link] for link in links]

    worksheet.update(
        f"{chr(64+col_index)}2:{chr(64+col_index)}{len(values)+1}",
        values
    )
