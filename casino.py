import configparser
from game_logic import play_game, check_balance

# Чтение начального капитала из файла настроек
config = configparser.ConfigParser()
config.read('settings.ini')
initial_balance = int(config['Settings']['MY_MONEY'])

# Инициализация переменных
balance = initial_balance
play_again = True

while play_again:
    # Получение ставки и выбранного слота от пользователя
    bet = int(input(f"Your balance: ${balance}. Enter your bet: "))
    chosen_slot = int(input("Choose a slot (1-30): "))

    # Игра и проверка результата
    win, result, winning_slot = play_game(bet, chosen_slot)

    print(f"Winning slot: {winning_slot}")
    if win:
        print(f"Congratulations! You won ${result}.")
    else:
        print(f"Sorry, you lost ${abs(result)}.")
        balance = check_balance(balance, result)

    # Проверка баланса и предложение сыграть еще
    if balance <= 0:
        print("Game over. You're out of money.")
        play_again = False
    else:
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input.lower() in ('yes', 'y'):
            play_again = True
            print("Let's play again!\n")
        else:
            play_again = False

# Вывод итогового баланса
print(f"Your final balance: ${balance}")
