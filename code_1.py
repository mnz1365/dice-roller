import random

dice = [0, 0]
firstNumber = random.randrange(1,7)
secondNumber = random.randrange(1,7) 
 
dice[0] = firstNumber
dice[1] = secondNumber

print('your dice result is ',dice[0], ' and ',dice[1])