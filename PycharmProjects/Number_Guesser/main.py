from art import logo
import random

RANDOM_NUMBER = random.randint(0, 101)
# print(RANDOM_NUMBER)


def easy():
    global flag
    original_number = RANDOM_NUMBER
    for number in range(10, 0, -1):
        flag = 0
        print(f"You have {number} remaining to guess number ")
        user_guess = int(input("Make a guess "))
        if user_guess == original_number:
            flag = 1
            return f"You got it The answer is {original_number}"

        elif user_guess > original_number:
            print(f"Too High")
        elif user_guess < original_number:
            print(f"Too low")
    if flag != 1:
        print("You hoave run out of guess ! You lose")


def hard():
    global flag
    original_number = RANDOM_NUMBER
    for number in range(5, 0, -1):
        flag = 0
        print(f"You have {number} remaining to guess number ")
        user_guess = int(input("Make a guess "))
        if user_guess == original_number:
            flag = 1
            return f"You got it The answer is {original_number}"

        elif user_guess > original_number:
            print(f"Too High")
        elif user_guess < original_number:
            print(f"Too low")
    if flag != 1:
        print("You hoave run out of guess ! You lose")


print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
condition = True
while condition == True:
    choice = input("Choose the diffculty,type 'hard' or 'easy' : ")
    if choice == 'hard':
        print(hard())
    else:
        print(easy())
    condition = False
    again = input("Do wanna play again (y/n) ")
    if again == 'y':
        condition = True
    elif again == 'n':
        print("Have a nice day !!")
