from game_data import data
from art import logo,vs
import random


def fromat_account(account):
    account_name = account['name']
    account_dec = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_dec}, from {account_country}"

def check_answer(guess,a_follower_count,b_follower_account):
    if a_follower_count>b_follower_account:
        return guess == "a"
    else:
        return guess == "b"

#print logo
print(logo)
score = 0
account_b = random.choice(data)
game_continue = True

while game_continue:
    # generate random account from random data
    account_a = account_b
    account_b = random.choice(data)
    print(f"Compare A: {fromat_account(account_a)}")
    print(vs)
    print(f"Compare B: {fromat_account(account_b)}")
    # Ask user for a guess

    guess = input("who has more follwers? Type 'A' or 'B'").lower()
    a_follower_account = account_a['follower_count']
    b_follower_account = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    #clear()

    if is_correct:
        score += 1
        print(f"You are right score :{score}")
    else:
        game_continue = False
        print(f"you are wrong score: {score}")
#make true aa postion A