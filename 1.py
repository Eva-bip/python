import random
from colorama import init, Fore

#инициализация colorama
init(autoreset=True)

print("Я загадал число от 1 до 100. Попробуй угадать!")

secret_number = random.randint(1,100) #рандомное целое число
attempts = 0 #для попыток

while True:
    user_input = int(input("Введи число: "))#ввёл число
    attempts += 1 #прибавили +1 к попыткам


    if user_input > secret_number:
        print(Fore.RED + "Слишком много!")
    elif user_input < secret_number:
        print(Fore.BLUE + "Слишком мало!")
    else:
        print(Fore.GREEN + "Поздравляю! Ты угадал:)")
        print(f"Количество попыток = {attempts}")
        break