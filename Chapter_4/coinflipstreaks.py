import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    list = [];
    for i in range(100):
        if random.randint(0,1) == 0:
            list.append('T')
        else:
            list.append('H')
    count,streak,val=0,0,list[0]
    for i in list:
        if i==val:
            count+=1
            val=i
        else:
            count=0
            val=i
        if count==6:
            streak+=1
            count=0
    numberOfStreaks += streak

print('Chance of streak: %s%%' % (numberOfStreaks / 100))