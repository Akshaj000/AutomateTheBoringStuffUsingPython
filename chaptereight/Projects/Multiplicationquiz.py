
import random,time

numberOfQuestions = 10
correctAnswers = 0

def takeinput(a,b,correctAnswers):
    seconds=time.time()
    answerBefore = seconds+8
    try:
        answerEntered = int(input(prompt))
    except ValueError:
        print("Incorrect!")
    seconds2=time.time()
    if seconds2>answerBefore:
        if answerEntered == a*b:
            print("Correct!")
            print("Out of time!")
        else:
            print("Correct!")
            print("Out of time!")

    else:
        if answerEntered == a*b:
            print("Correct!")
            correctAnswers+=1
            time.sleep(1)
        else:
            print("Incorrect!")
    return correctAnswers


for qno in range(numberOfQuestions):
    count = 0
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s = ' % (qno+1,num1,num2)
    answerEntered=0;
    while True:
        seconds=time.time()
        answerBefore = seconds+8
        try:
            answerEntered = int(input(prompt))
        except ValueError:
            print("Incorrect!")
            cA = correctAnswers
            correctAnswers=takeinput(num1,num2,correctAnswers)
            if cA == correctAnswers:
                correctAnswers=takeinput(num1,num2,correctAnswers)
            if cA == correctAnswers:
                print("Out of tries!")
                time.sleep(1)
            break
       
        seconds2=time.time()
        if seconds2>answerBefore:
            if answerEntered == num1*num2:
                print("Correct!")
                print("Out of time!")
            else:
                print("Correct!")
                print("Out of time!")

        else:
            if answerEntered == num1*num2:
                print("Correct!")
                correctAnswers+=1
                time.sleep(1)
                break
            else:
                print("Incorrect!")
                cA = correctAnswers
                correctAnswers=takeinput(num1,num2,correctAnswers)
                if cA == correctAnswers:
                    correctAnswers=takeinput(num1,num2,correctAnswers)
                if cA == correctAnswers:
                    print("Out of tries!")
                    time.sleep(1)
                break
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
