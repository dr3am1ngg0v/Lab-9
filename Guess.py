import random
import logging

logging.basicConfig(level = logging.INFO, filename = "log.log", format = "%(asctime)s - %(levelname)s - %(message)s")


while True:     # Цикл обработки ввода границ диапазона
    try:
        number = int(input("Введите натуральное число больше единицы: "))
        if number <= 1:
            logging.error(f'ERROR: Incorrect enter.')
            print('Неверный ввод.\nПовторите попытку: ')
        else:
            logging.info(f'User has entered an array border: {number}')
            break
    except ValueError:
        logging.error(f'ERROR: Incorrect enter.')
        print("Неверный ввод.\nПовторите попытку: ")

while True:     # Цикл обработки ввода количества попыток
    try:
        try_number = int(input("Введите количество попыток: "))
        if try_number <= 0:
            logging.error(f'ERROR: Incorrect enter.')
            print('Неверный ввод.\nПовторите попытку: ')
        else:
            logging.info(f'User has entered an number of attempts: {try_number}')
            break
    except ValueError:
        logging.error(f'ERROR: Incorrect enter.')
        print("Неверный ввод.")

#генерация числа в диапазоне от 1 до num
randnum = random.randint(1, number)
logging.info(f'Generated number: {randnum}')

while try_number > 0: #цикл отгдаывания числа
    try:
        guess_num = int(input("Введите загаданное число: "))
        assert number >= 0
        if guess_num == randnum:
            logging.info(f'User did guess the number.')
            print("Поздравляем! Вы угадали!")
            break
        else:
            try_number -= 1
            if guess_num < randnum:
                logging.info(f'User has entered a smaller number than the hidden.')
                print("Загаданное число больше.")
            else:
                logging.info(f'User has entered a bigger number than the hidden.')
                print("Загаданное число меньше.")
            if try_number == 0:
                logging.info(f"User didn't guess the number")
                print("Ваши попытки закончились.\nЗагаданное число: ", randnum)
    except ValueError:
        logging.error(f'ERROR: Incorrect enter.')
        print("Неверный ввод.\nПовторите попытку: ")
    except AssertionError:
        logging.error(f'ERROR: Incorrect enter.')
        print('нНеверный ввод.\nПовторите попытку: ')
    
logging.info(f'Program finished')