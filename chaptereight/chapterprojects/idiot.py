import pyinputplus as pyip

while True:
    prompt = "Want to know how to keep an idiot busy for hours?\n"
    response = pyip.inputYesNo(prompt)
    print(response)
    if response == 'no':
        print('Thank you. Have a nice day.')
        break