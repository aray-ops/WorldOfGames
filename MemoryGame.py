import random
import time
import os

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(int(difficulty))]

def get_list_from_user(difficulty):
    user_input = input(f"Enter {difficulty} numbers separated by spaces: ")
    return [int(x) for x in user_input.split()]

def is_list_equal(list1, list2):
    return list1 == list2

def play(difficulty):
    sequence = generate_sequence(difficulty)
    print("Memorize this sequence:", sequence)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    user_sequence = get_list_from_user(difficulty)
    return is_list_equal(sequence, user_sequence)