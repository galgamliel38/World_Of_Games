import os
import random
from time import sleep

from Utils import Screen_cleaner


def generate_sequence(difficult):
    random_list = []
    for i in range(0, difficult):
        n = random.randint(1, 102)
        random_list.append(n)
    print(random_list)
    sleep(0.7)
    os.system('cls')
    return random_list


def get_list_from_user(difficult):
    print('please input ', difficult, 'numbers between 1 - 101 , press enter after every number')
    user_list = []
    for i in range(0, difficult):
        num = input('please enter number: ')
        num_flag = True
        while num_flag:
            if num.isdigit():
                num = int(num)
                if num in range(1, 102):
                    user_list.append(num)
                    num_flag = False
                else:
                    print('your number is not between 1 - 101')
                    num = input('please try again: ')
            else:
                print('this is not a number')
                num = input('please try again: ')
    return user_list


def is_list_equal(user_list, random_list):
    user_list.sort()
    random_list.sort()
    if user_list == random_list:
        return True
    else:
        return False

def play(difficult):
    print(is_list_equal(generate_sequence(difficult), get_list_from_user(difficult)))


