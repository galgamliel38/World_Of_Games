import random


def generate_number(difficult):
    secret_number = random.randint(1, difficult)
    return secret_number

def get_guess_from_user(difficult):
    print('please guess what number am i thinking between 1 to ', difficult)
    guess_flag = True
    guess = input('please enter your guess: ')
    while guess_flag:
        if guess.isdigit():
            guess = int(guess)
            guess_flag = False
        else:
            print('this is not a valid option')
            guess = input('please try again: ')
    return guess


def compare_results(secret, guess):
    if secret == guess:
        return True
    else:
        return False

def play(difficult):
    print(compare_results(generate_number(difficult), get_guess_from_user(difficult)))