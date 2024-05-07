def clear_spreadsheet_tab(sheets_service, spreadsheet_id, tab_name):
    range_ = tab_name
    request = sheets_service.values().clear(
        spreadsheetId=spreadsheet_id,
        range=range_,
        body={}
    )
    response = request.execute()
    return response