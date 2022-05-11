from ast import While
import ui 
import read_write_files as rw 

import random

#This function searches for the user letter in the word. Return True if it is there, and False otherwise.
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

#From the list of words extracted from the file, returns one of them randomly
def choosing_random_word(file_words):
    index = random.randint(0, len(file_words))
    return file_words[index]

#Creates a support list, the list will register which letters have been found by changing its values
#from 0 to 1. 1 if it was found, 0 if not. 
def creating_support_list(word):
    return [0 for i in range(len(word))]

#Useful for selecting the difficulty of the game... Amount of lives 
def difficulty():
    pass

#The whole process of the game is going to be here. 
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