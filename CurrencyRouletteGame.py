import random
import requests


dollar = random.randint(1, 100)
URL = 'https://v6.exchangerate-api.com/v6/fd6de2ab3c500dfeabb006ac/latest/USD' # URL for API requests for USD rates
dollar_shekel_rate = requests.get(URL).json()["conversion_rates"]["ILS"]
total = dollar_shekel_rate * dollar

# for check:
# print(dollar)
# print(dollar_shekel_rate)
# print(total)


def get_money_interval(difficult):
    interval_range = (total - (5 - difficult), total + (5 - difficult))
    print('my current currency is: ', dollar, '$')
    return interval_range


def get_guess_from_user():
    guess = input('please guess the current currency rate from USD to ILS: ')
    guess_flag = True
    while guess_flag:
        if '.' in guess:
            guess_dot = guess
            guess_dot_remove = guess_dot.replace('.', '')
            if guess_dot_remove.isdigit():
                guess = float(guess)
                guess_flag = False
        else:
            print('this is not a valid option')
            guess = input('please try again: ')
    return guess



def play(difficult):
    internal = get_money_interval(difficult)
    user_guess = get_guess_from_user()
    if user_guess >= internal[0] and user_guess <= internal[len(internal)-1]:
        return True
    else:
        return False

