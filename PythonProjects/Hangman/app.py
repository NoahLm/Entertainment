from ast import While
import ui 
import read_write_files as rw 

import random

def letter_check(letter , word, support_list, lives):
    for i in range(len(word)):
        if letter == word[i]:
            if support_list[i] == 1:
                print("You already introduced that letter it")
                return True 

            elif support_list[i] == 0:
                print("Correct!")
                support_list[i] = 1
                return True

    print("U did not found a correct letter")
    return False

def choosing_random_word(file_words):
    index = random.randint(0, len(file_words))
    return file_words[index]

def creating_support_list(word):
    return [0 for i in range(len(word))]

def difficulty():
    pass

def game(difficulty_lives):
    word = choosing_random_word(rw.read_file())
    supp_list = creating_support_list(word)

    lives = 0

    while lives >= 0:
        pass



def main(): 
    ui.clear_scrn()
    ui.welcome_scrn()

    print("Welcome")

if __name__ == "__main__":
    main()