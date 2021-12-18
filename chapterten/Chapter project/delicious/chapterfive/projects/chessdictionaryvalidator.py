def isValidChessBoard(dictionary):
    pieces={'bpawn':2,'bknight':2,'bbishop':2,'brook':2,'bqueen':1,'bking':1,'wpawn':2,'wknight':2,'wbishop':2,'wrook':2,'wqueen':1,'wking':1}
    rows=['1','2','3','4','5','6','7','8']
    columns=['a','b','c','d','e','f','g','h']
    count={}
    space=[]
    checkspace=True
    checkcount=True
    for i in dictionary:
        space.append(i)
        if i in space:
            checkspace = False
            break
        if i[0] not in rows or i[1] not in columns:
            checkspace = False
            break
    for i in dictionary.values():
        if i not in count:
            count[i] = 1
        else:
            count[i]+=1

    for i in count:
        if count[i] <= pieces[i]:
            pass
        else:
            checkcount = False
            break
    return (checkcount and checkspace)
    


dictionary = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking','4e':'bbishop','6c': 'brook'}
print(isValidChessBoard(dictionary))