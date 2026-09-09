import random

answer=input("Ready to play? y/n ")
while answer=="y":
 number = random.randint(1, 10)
 print("I´m thinking of a number between 1-10")
 guess =int(input("Guess = "))

 while guess !=number:
    if guess <number:
        print("Too low")
    elif guess >number:
        print("Too high")
    else:
        print("???")

 guess = int(input("Guess again = "))
 answer=input("Correct! Wanna play again? y/n ")

if answer=="n":
    exit()

