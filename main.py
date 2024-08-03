from random import randint

while True:
    n = randint(1, 100)
    a = -1
    guesses = 0

    while a != n:
        guesses += 1
        a = int(input("Guess a number: "))

        if a > n:
            print("Lower number please")
        else:
            print("Higher number please")

    print(f"You have guessed the number {n} in {guesses} attempts.")

    while True:
        play_again = input("Press 'y' to play again or 'n' to exit: ").lower()
        if play_again == 'y':
            break
        elif play_again == 'n':
            break
        else:
            print("Wrong input, please enter 'y' or 'n'.")

    if play_again == 'n':
        break