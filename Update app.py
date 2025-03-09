from GuessGame import play as guess_play
from MemoryGame import play as memory_play
from CurrencyRouletteGame import play as currency_play
from Utils import screen_cleaner
from Score import add_score

def welcome(username):
    return f"Hi {username} and welcome to the World of Games: The Epic Journey"

def start_play():
    print("Please choose a game to play:")
    print("    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("    2. Guess Game - guess a number and see if you chose like the computer")
    print("    3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    
    game_choice = input("Enter game number (1-3): ")
    difficulty = input("Please choose game difficulty (1-5): ")
    
    games = {
        '1': memory_play,
        '2': guess_play,
        '3': currency_play
    }
    
    screen_cleaner()
    result = games[game_choice](difficulty)
    if result:
        add_score(difficulty)
        print("You won!")
    else:
        print("You lost!")
    return result