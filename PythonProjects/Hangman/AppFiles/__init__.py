import ui 
import app


def main(): 
    ui.clear_scrn()
    ui.welcome_scrn()

    print("Welcome\n")
    print("1.- Easy, 2.- Mid 3.-Hard")

    diff = int(input("Choose a difficulty: "))
    lives = app.difficulty(diff)
    app.game(lives)


if __name__ == "__main__":
    main()