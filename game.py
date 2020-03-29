
import random


def guessinggame():
    try:
        answer = random.randint(1, 10)
        type_check = int(
            input("Enter 1 for play machine itself and 2 for Play Yourself"))
        run_game = True
        tries = 0
        while run_game:
            if type_check == 2:
                guess_num = random.randint(1, 10)
            else:
                guess_num = int(
                    input("Can you guess the random number between 1 and 10  Type it-> "))
            if(type(guess_num) in [int]):
                tries += 1
                # print(f"Answer {answer}")
                if(guess_num == answer):
                    run_game = False
                    print(f"Correct :) With {tries} attemp You Success")
                    continue_game = input("Play Again ? (Y/N) -> ")
                    if(continue_game not in ['y', 'Y', 'n', 'N']):
                        print("You Enter A Wrong Input")
                        break
                    else:
                        if(continue_game.lower() == 'y'):
                            guessinggame()
                        if(continue_game.lower() == 'n'):
                            print("See You Next Time :)")
                            break
                elif(guess_num > answer):
                    print("Too Higher")
                elif(guess_num < answer):
                    print("Too Lower")
                if(tries == 10):
                    print(f"You Attemp {tries} Looks like you failed!")
                    break

    except ValueError as err:
        raise ValueError("Value error")
