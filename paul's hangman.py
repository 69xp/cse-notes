import random
# import string
wrong_guesses_left = 10
guess_end = False
"""
this a guide of how to make hangman
1. make word bank 10 items.
2. select a random item to guess
3. take in the letters and add it to list of letters
5.hide and reveal letters based on input
6. create a win condition.
"""


word_bank = ["let the waves crash down", "giant arachnids consuming marsupials", "carnivorous baseballs from the sky",
             "thor is buying shawarma", "groot is a dancing baby", "cheesy hotdogs with mustard",
             "live a happy life... eventually", "time to high-five the sky!", "koolaid muffins",
             "pikachoo is sneezing."]
guess_word = random.choice(word_bank)
letters_guessed = [' ', '.', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '-']
list_of_letters_in_word = list(guess_word)
while wrong_guesses_left != 0:
    current_guess = str(input("guess a letter A through Z."))
    letters_guessed.append(current_guess)
    print(letters_guessed)
    if current_guess not in guess_word:
        wrong_guesses_left -= 1
    output = []
    for letter in guess_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    output = ''.join(output)
    print(output)
    if '*' not in output:
        print("you win.")
    if wrong_guesses_left == 0:
        print("you lose")
    print(wrong_guesses_left)
