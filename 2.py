import time
import os

while True:
    #очищаем экран
    os.system('cls' if os.name == 'nt' else 'clear')

    current_time = time.strftime("%H:%M:%S")
    print(current_time)

    time.sleep(1) #ждём 1 сек
    #программа работать будет в бесконечном цикле, поэтому останавливаем вручную