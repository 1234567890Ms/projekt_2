"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Michal Slabý
email: michalslaby1@gmail.com
discord: michals._68964
"""
from random import seed, randint
import os 
import sys

DEBUG = False

SEPARATOR = 50 * "-"
len_of_number = int(4)

def intro():
    print(" ")
    print("Hi there!")
    print(SEPARATOR)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(SEPARATOR)
    print("Enter a number:")
    print(SEPARATOR)

def generate_number(len_of_number):
    seed()
    game_numbers = []

    while len(game_numbers) < int(4):
        number = str(randint(0, 9))
        if number not in game_numbers:
            game_numbers.append(number)

    return game_numbers




def user_input(num_len):
    while True:

        user_number = input(">>> ")
        if user_number.isnumeric() == True:

            user_tips = list(user_number)

            if len(user_tips) < len_of_number:
                print(
                "You number is too short. Enter 4 digits number. Try it again."
                )
                continue
            elif len(user_tips) > len_of_number:
                print(
                "You number is too long. Enter 4 digits number. Try it again."
                )
                continue
            else:
                return user_tips

        else:
            print("This is not a number. Try i again.")


def clear_terminal():
    user_input = input("Zadej 'Y' pro vyčištění terminálu: ")
    if user_input == 'Y':
        os.system('cls' if os.name == 'nt' else 'clear')
        clear_terminal()
        sys.exit()
   




def check_conditions(user_num, game_num):
    score = {"bulls": 0, "cows": 0}
    for u, g in zip(user_num, game_num):

        if u == g:
            score["bulls"] += 1
        elif u in game_num:
            score["cows"] += 1

    return score


def game_loop():
    intro()
    number_length = len_of_number
    game_number = generate_number(len_of_number)

    user_attempt = 1
    while True:

        if DEBUG:
            print("Game number", game_number)

        user_number = user_input(len_of_number)

        if DEBUG:
            print("User number", user_number)

        user_score = check_conditions(user_number, game_number)

        print(f"{user_score['bulls']} bulls, {user_score['cows']} cows")

        if user_score["bulls"] == number_length:
            print(f"Correct, you've guessed the right number in {user_attempt} guesses!")

            if user_attempt <= (number_length):
                win_string = "Amazing game"
            elif number_length < user_attempt < (number_length + 2):
                win_string = "Average game"
            elif (number_length + 2) < user_attempt < (number_length + 3):
                win_string = "Could be better"
            else:
                win_string = "Not so good game"
            print("")
            print(10 * "*", win_string, 10 * "*")
            clear_terminal()
            break
        user_attempt += 1



if __name__ == "__main__":
    game_loop()

