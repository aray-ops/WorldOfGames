import random
import requests

def get_money_interval(difficulty):
    amount = random.randint(1, 100)
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    rate = response.json()['rates']['ILS']
    total = amount * rate
    margin = 10 - difficulty
    return (total - margin, total + margin), amount

def get_guess_from_user(amount):
    return float(input(f"Guess the value of {amount} USD in ILS: "))

def compare_results(interval, user_guess):
    return interval[0] <= user_guess <= interval[1]

def play(difficulty):
    interval, amount = get_money_interval(difficulty)
    user_guess = get_guess_from_user(amount)
    return compare_results(interval, user_guess)