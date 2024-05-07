import pandas as pd

def get_dataframe_from_tab(sheets_service, spreadsheet_id, tab_name, skip_rows=[]):    
    
    result = sheets_service.values().get(
        spreadsheetId=spreadsheet_id,
        range = tab_name
    ).execute()

    values = result['values']
    data = [row for index, row in enumerate(values) if index not in skip_rows]

    return pd.DataFrame(data[1:], columns=data[0])