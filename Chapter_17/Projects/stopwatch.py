#! python3
# stopwatch.py - A simple stopwatch program.

import time, pyperclip
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
input()
print('Started.')

a = ''
startTime = time.time()   
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime,2)
        totalTime = round(time.time()-startTime,2)
        totalTime, lapTime = str(totalTime), str(lapTime)
        a = 'Lap #'+str(lapNum).rjust(4)+': '.rjust(4)+totalTime.center(4)+'('.ljust(5)+lapTime+')'
        print(a)
        lapNum+=1
        lastTime = time.time()
except KeyboardInterrupt:
    pyperclip.copy(a)
    print('\nDone.')
