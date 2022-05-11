import ui 
import read_write_files as rw 

def letter_check(letter , word, support_list, lives):
    for i in range(len(word)):
        if letter == word[i]:
            if support_list[i] == 1:
                print("You already introduced that letter it")
                return lives 

            elif support_list[i] == 0:
                print("Correct!")
                support_list[i] = 1
                return lives

    print("U did not found a correct letter")
    return lives - 1

    
    

        








def main(): 
    ui.clear_scrn()
    ui.welcome_scrn()

    print("Welcome")

if __name__ == "__main__":
    main()