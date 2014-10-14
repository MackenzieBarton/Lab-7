x = 1
while (x < 300):
    print x
    x = x + 2

        
mL = [5,12,4,8,6,1,3,9,7,10]
index = 0
while (index < len(mL)):
    print mL[index]
    index = index + 1



import random

keepGoing = True
rand = random.randint(0,50) 

while (keepGoing == True):
    print "Guess a random number between 0 and 50"
    userInput = int(raw_input())
    if userInput < rand:
        print "your number is too low"
    if userInput > rand:
        print "your number is too high"
    if userInput == rand:
        keepGoing = False
        print "you guessed the right number"
    




