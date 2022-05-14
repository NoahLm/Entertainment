import ui 
import app


def main(): 
    ui.clear_scrn()
    ui.welcome_scrn()

    print("Welcome\n")
    print("1.- Easy, 2.- Mid 3.-Hard")

    while bool:
        try:
            diff = int(input("Choose a difficulty: "))
            if diff < 1 or diff > 3:
                print("Please select one of the options above")
                continue
            break

        except ValueError:
            print("Introduce only a number")

    lives = app.difficulty(diff)
    app.game(lives)


if __name__ == "__main__":
    main()