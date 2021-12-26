import ezsheets
ss = ezsheets.Spreadsheet('14jw_vdOndkCNed2vKa62PrGlFhv5_EZch4iHASOKz54')
sheet = ss['Form responses 1']
email = sheet.getColumn(3)
ss2 = ezsheets.createSpreadsheet('Email Addresses')
ss2.createSheet('EmailAddresses',0)
sheet2 = ss2['EmailAddresses']
sheet2.updateColumn(1,email)
ss2.downloadAsExcel()
