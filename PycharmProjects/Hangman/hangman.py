import random
from hangman_logo import logo
from hangman_words import word_list
from stages import stages

print(logo)
lives = 6
chosen_word = random.choice(word_list)
# print(chosen_word) for hint
display = []
end_of_game = False  # for keeping while true
for item in chosen_word:
    display += '_'
word_length = len(chosen_word)
while not end_of_game:
    guess = input("Guess a word").lower()
    if guess in display:
        print("you already gussed it")
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    if guess not in chosen_word:
        lives -= 1
        print("OOPS,your guess wrong")
        print(display)
        if lives == 0:
            end_of_game = True
            print("You lost")
    print(stages[lives])
    print(display)
    if '_' not in display:
        print("you won")
