import random

sides = [1,2,3,4,5,6]
myselection = int(input("Hey,welcome to the dice game/nPlease type in your number selection:"))

dicevalue = random.randint(1,6)
print("Dice value;",dicevalue)

computer_random_number = random.randint(1,6)
print("The computer has selected:",computer_random_number)
print("I selected:",myselection)

if dicevalue ==computer_random_number:
    print("The computer won !")
else:
    print("The computer failed!")

if dicevalue == myselection:
    print("You won the game!")
else:
    print("You lost!")
if dicevalue == myselection and dicevalue ==computer_random_number:
    print("A draw between you and the computer")