import os

information_to_hide_path = input("Пожалуйста, введите полный путь к файлу со скрываемой информацией "
                                 "(можно использовать файл information_to_hide_task3.txt из папки task3): ")
information_to_hide = open(information_to_hide_path, 'r', encoding='cp1251').read()

container_path = input("Пожалуйста, введите полный путь к файлу-контейнеру "
                       "(можно использовать файл container_task3.txt из папки task3): ")
container = open(container_path, 'r', encoding='cp1251')

encoded_container_folder = input("Пожалуйста, введите полный путь к каталогу, в который будет сохранен "
                                 "результат (файл-контейнер с скрываемой информацией) - файл с названием encoded_task3.txt: ")
encoded_container_path = encoded_container_folder + os.sep + 'encoded_task3.txt'
encoded_container = open(encoded_container_path, 'w', encoding='cp1251')

bytes_of_hidden_information = information_to_hide.encode('cp1251')
for one_byte in bytes_of_hidden_information:
    bits = bin(one_byte)[2:].zfill(8)
    for bit in bits:
        symbol = ''
        while symbol != ' ':
            symbol = container.read(1)
            encoded_container.write(symbol)
        if bit == '1':
            encoded_container.write(" ")

while True:
    symbol = container.read(1)
    encoded_container.write(symbol)
    if not symbol:
        break

container.close()
encoded_container.close()

print("Шифрование закончено!")
input("Нажмите Enter, чтобы завершить... ")
