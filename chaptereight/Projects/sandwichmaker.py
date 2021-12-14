# Sandwich maker
import pyinputplus as pyip

def createSandwich():
    bread = pyip.inputMenu(['wheat','white','sourdough'])
    protein = pyip.inputMenu(['chicken','turkey','ham','tofu'])
    wantCheese = pyip.inputYesNo('Do you want cheese in ur sandwich? ')
    if wantCheese == 'yes':
        cheese = pyip.inputMenu(['cheddar','swiss','mozzerella'])
    wantMayo = pyip.inputYesNo('Do you want mayo in ur sandwich? ')
    wantMustard = pyip.inputYesNo('Do you want mustard in ur sandwich? ')
    wantLettuce = pyip.inputYesNo('Do you want lettuce in ur sandwich? ')
    wantTomato = pyip.inputYesNo('Do you want tomato in ur sandwich?')
    quantity = pyip.inputInt('How many sandwiches do u need? ')
    return bread,protein,cheese,wantMayo,wantMustard,wantLettuce,wantTomato,quantity

def viewPrice(bread,protein,cheese,wantMayo,wantMustard,wantLettuce,wantTomato,quantity):
    breadPrice = {'wheat': 150,'white':100,'sourdough':120}
    proteinPrice = {'chicken': 120,'turkey':140,'ham':150,'tofu':160}
    cheesePrice = {'cheddar':60 , 'swiss':100 , 'mozzerella':100}
    othersPrice = {'mayo':30 , 'mustard':40,'lettuce':40,'tomato':20}
    Total = 0

    print("---------------------BILL------------------------------")
    print("\n")
    print("Item\t\t\tType\t\t\tPrice")
    print("Bread\t\t\t{}\t\t\t{}".format(bread,breadPrice[bread]))
    Total+=breadPrice[bread]
    print("Protein\t\t\t{}\t\t\t{}".format(protein,proteinPrice[protein]))
    Total+=proteinPrice[protein]
    if cheese != None:
        print("Cheese\t\t\t{}\t\t\t{}".format(cheese,cheesePrice[cheese]))
        Total+=cheesePrice[cheese]
    if wantMayo == 'yes':
        print("Mayo\t\t\t{}\t\t\t{}".format(None,othersPrice['mayo']))
        Total+=othersPrice['mayo']
    if wantMustard == 'yes':
        print("Mustard\t\t\t{}\t\t\t{}".format(None,othersPrice['mustard']))
        Total+=othersPrice['mustard']
    if wantLettuce == 'yes':
        print("Lettuce\t\t\t{}\t\t\t{}".format(None,othersPrice['lettuce']))
        Total+=othersPrice['lettuce']
    if wantTomato == 'yes':
        print("Tomato\t\t\t{}\t\t\t{}".format(None,othersPrice['tomato']))
        Total+=othersPrice['tomato']
    print("-------------------------------------------------------")
    print('\nQuantity: {}'.format(quantity))
    print("TotalPrice: {}".format(Total*quantity))
    print("-------------------------------------------------------")
    

bread,protein,cheese,wantMayo,wantMustard,wantLettuce,wantTomato,quantity = None,None,None,'no','no','no','no',0
bread,protein,cheese,wantMayo,wantMustard,wantLettuce,wantTomato,quantity=createSandwich()
viewPrice(bread,protein,cheese,wantMayo,wantMustard,wantLettuce,wantTomato,quantity)

