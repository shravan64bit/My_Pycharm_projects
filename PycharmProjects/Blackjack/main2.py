from art import logo
import random

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def join():
    return card[random.randint(0, 10)]


def sum(n1, n2):
    return n1 + n2


user_random_list = [card[join()],card[join()]]
computer_random_list = [card[join()],card[join()]]
upadted_sum_user = sum(user_random_list[0],user_random_list[1])
upadted_sum_computer = sum(computer_random_list[0],computer_random_list[1])
updated_random_computer_list = []
ticket = input("Do you want to play Black jack (y/n) ? ")
if ticket == 'y':
    print(logo)
    print(f"Your cards {user_random_list},current score {upadted_sum_user}")
    print(f"Computer First card {computer_random_list[0]}")
    condition = True
    while condition == True:
        loop_input = input("Type 'y' to get another card,type 'n' to pass ")
        if loop_input == 'y':
            user_next_card = card[join()]
            upadted_sum_user = sum(upadted_sum_user, user_next_card)
            if user_next_card == 11:
                if upadted_sum_user > 21:
                    user_next_card = 1
                    upadted_sum_user -= 10
            user_random_list.append(user_next_card)
            if upadted_sum_user <= 21:
                print(f"Your cards{user_random_list},Current score {upadted_sum_user} \n Computer's First card :{computer_random_list[0]}")
            elif upadted_sum_user > 21:
                if computer_random_list[0] == 11:
                    if upadted_sum_computer > 21:
                        computer_random_list[0] = 1
                        upadted_sum_computer -= 10
                    computer_random_list.append(computer_random_list[0])
                elif computer_random_list[1] == 11:
                    if upadted_sum_computer > 21:
                        computer_random_list[1] = 1
                        upadted_sum_computer -= 10
                    computer_random_list.append(computer_random_list[1])
                print(f"Your final score {user_random_list},Final score {upadted_sum_user}")
                print(f"Computer's Final hand {computer_random_list},Final score {upadted_sum_computer}")
                print("computer wins")
                condition = False


        elif loop_input == 'n':
            for num in range(0, 5):
                if upadted_sum_computer <= 21 and upadted_sum_computer <= upadted_sum_user:
                    computer_next_card = card[join()]
                    upadted_sum_computer = sum(upadted_sum_computer, computer_next_card)
                    if computer_next_card == 11:
                        if upadted_sum_computer > 21:
                            computer_next_card = 1
                            upadted_sum_computer -= 10
                    computer_random_list.append(computer_next_card)
            print(f"Your final cards {user_random_list},Final score:{upadted_sum_user}")
            print(f"Computers final hand {computer_random_list},Final score {upadted_sum_computer}")
            if upadted_sum_computer > upadted_sum_user and upadted_sum_computer <= 21:
                print("Computer wins")
            else:
                print("User wins")
            condition = False
else:
    print("Come agin later")










