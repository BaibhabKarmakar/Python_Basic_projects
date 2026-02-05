import random

computer_value = random.randint(1 , 100)
no_of_guess = 1
def takeUserInput():
    return input("Enter the guess from 1 to 1000 or Quit(Q): ")


while(True):
    user = takeUserInput()
    if(user == "Q"):
        break
    if(int(user) == computer_value):
        print(f"Wow ! You have guessed it right ! , You have tried for {no_of_guess} times to guess it correct!")
        break
    elif(int(user) > computer_value):
        print("Guess lower number please!")

    else:
        print("Guess higher number please!")

    no_of_guess += 1

