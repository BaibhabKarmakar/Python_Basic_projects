import random

computer_value = random.randint(1 , 100)
no_of_guess = 1
def takeUserInput():
    return int(input("Enter the guess from 1 to 1000 : "))


while(True):
    user = takeUserInput()
    if(user == computer_value):
        print(f"Wow ! You have guessed it right ! , You have tried for {no_of_guess} times to guess it correct!")
        break
    elif(user > computer_value):
        print("Guess it lower!")

    else:
        print("Guess it higher!")

    no_of_guess += 1

