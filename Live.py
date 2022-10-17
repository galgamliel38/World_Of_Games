import CurrencyRouletteGame
import GuessGame
import MemoryGame
from flask import Flask
from GuessGame import play
from MemoryGame import play
from CurrencyRouletteGame import play
from Score import add_score


def welcome(name):
    print("Hello ", name, "and welcome to the World of Games (WoG).\n"
                          "Here you can find many cool games to play.")


def load_game():
    print("Please choose a game to play:\n1. Memory Game - a sequence of numbers "
          "will appear for 1 second and you have to guess it back.\n"
          "2. Guess Game - guess a number and see if you chose like the computer.\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    choose_flag = True
    while choose_flag:
        choose = input("My choose is: ")
        if choose.isdigit():
            choose = int(choose)
            if choose in range(1, 4):
                print("great choose :)")
                choose_flag = False
            else:
                print("your choose is not in range, please try again")
        else:
            print("this is not a number, please try again")
    difficult_flag = True
    difficult = input("Please choose game difficulty from 1 to 5: ")
    while difficult_flag:
        if difficult.isdigit():
            difficult = int(difficult)
            if difficult in range(1, 6):
                print("great choose :)")
                difficult_flag = False
            else:
                print("invalid option")
                difficult = input("Please try again, choose game difficulty from 1 to 5: ")
        else:
            print("invalid option")
            difficult = input("Please try again, choose game difficulty from 1 to 5: ")

    if choose == 1:
        MemoryGame.play(difficult)
    elif choose == 2:
        GuessGame.play(difficult)
    else:
        print(CurrencyRouletteGame.play(difficult))


