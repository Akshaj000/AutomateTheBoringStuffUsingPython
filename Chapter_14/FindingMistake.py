import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
# ss2 = ezsheets.createSpreadsheet('CorrectedData')
# sheet2 = ss2[0]
for i in range(2,15001):
    bpj = ss[0].get(1,i)
    jars = ss[0].get(2,i)
    total = ss[0].get(3,i)
    if int(total) != int(bpj)*int(jars):
        print(False)
        print(bpj+" * "+jars+" != "+total)
        print(bpj+" * "+jars+" == ",int(bpj)*int(jars))
        print("Row = ",i)
        # sheet2[1,i]= bpj
        # sheet2[2,i]= jars
        # sheet2[3,i]= total
    # else:
    #     print(False)
    #     sheet2[1,i]= bpj
    #     sheet2[2,i]= jars
    #     sheet2[3,i]= int(bpj*jars)
# ss2.downloadAsExcel()


