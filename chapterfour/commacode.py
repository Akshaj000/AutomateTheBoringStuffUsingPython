def commacode(list):
    if list==[]:
        return "''"
    string=''
    for i in list:
        string+=i
        if(i!=list[-1]):
            string+=', '
    return string


list = []
n = int(input('Enter no of element'))
for i in range(n):
    list.append(input())
print(commacode(list))