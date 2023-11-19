import random

def play_game(bet, chosen_slot):
    winning_slot = random.randint(1, 30)
    if chosen_slot == winning_slot:
        return True, bet * 2, winning_slot
    else:
        return False, -bet, winning_slot

def check_balance(balance, result):
    return balance + result
