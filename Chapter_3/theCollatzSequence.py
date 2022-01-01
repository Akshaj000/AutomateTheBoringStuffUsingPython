def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1

try:
    num = int(input())
    a=collatz(num)
    while a != 1:
       a=collatz(a)

except ValueError:
    print("Input must be an integer")
