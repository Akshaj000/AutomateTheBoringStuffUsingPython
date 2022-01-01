def printTable(table):
    maxstringlen = 0
    item = ""
    maxm=0;
    for i in table:
        maxm = max(maxm,len(i))

    for i in range(maxm):
        for j in range(len(table)):
            stringlen = len(table[j][i])
            maxstringlen=max(stringlen,maxstringlen)
            if maxstringlen == stringlen:
                item = table[j][i]  

    for i in range(maxm):
        for j in range(len(table)):
            print(table[j][i].rjust(maxstringlen), end = "")
        print("")

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)