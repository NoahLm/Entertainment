from ast import While
import read_write_files as rw 

import random

#This function searches for the user letter in the word. Return True if it is there, and False otherwise.
def letter_check(letter , word, support_list, lives):
    for i in range(len(word)):
        if letter == word[i]:
            if support_list[i] == 1:
                print("You already introduced that letter it")
                return True, support_list

            elif support_list[i] == 0:
                print("Correct!")
                support_list[i] = 1
                return True, support_list

    print("U did not found a correct letter")
    return False, support_list

def print_word(word, support_list):
    for i in support_list:
        if i == 1:
            print(word[i] + " ")

        else:
            print("_ ")
            

#From the list of words extracted from the file, returns one of them randomly
def choosing_random_word(file_words):
    index = random.randint(0, len(file_words))
    return file_words[index]

#Creates a support list, the list will register which letters have been found by changing its values
#from 0 to 1. 1 if it was found, 0 if not. 
def creating_support_list(word):
    return [0 for i in range(len(word))]

#Useful for selecting the difficulty of the game... Amount of lives 
def difficulty(choice):
    if choice == 1:
        return 9

    elif choice == 2:
        return 6

    elif choice == 3:
        return 3

    else: 
        return False

#The whole process of the game is going to be here. 
def game(difficulty_lives):
    word = choosing_random_word(rw.read_file())
    supp_list = creating_support_list(word)

    lives = difficulty_lives

    while lives > 0:

        print_word(word, supp_list)
        user = input("Introduce a letter: ")

        bool_check, supp_list = letter_check(user , word, supp_list, lives)

        if bool_check == True: 
            print("Correct!")
            continue
        
        else: 
            print("Incorrect!")
            lives -= 1
            continue
            

            