import random
import logging

# Работа с логированием
logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)

# Создан файл для логирования
file_handler = logging.FileHandler("log.log")
# Создание форматера отображающего дату, время, имя логгера, уровень и сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

while True: # Проверка ввода
    try:
        n = int(input("Введите количество бочек: "))
        if  n<1: #проверка положительное ли число бочек
            logger.error("ValueError")
            print("Количество бочек должно быть положительным числом")
        else:
            break
    except ValueError:
        logger.error("ValueError")
        print("Некорректный ввод")
        pass

digits=list(range(1, n+1)) #создан список чисел

random.shuffle(digits)

logger.info("Started printing numbers")

for i in range(n): #вывод чисел
    k=input("Нажмите любую клавишу чтобы получить рандомное число")
    print("Число", digits[i])
logger.info("Stopped printing numbers")
x = input("Нажмите любую клавишу чтобы завершить программу")
logger.info("Programm is ended")

