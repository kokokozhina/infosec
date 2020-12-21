import os

encoded_container_path = input("Пожалуйста, введите полный путь к каталогу, в который сохранен "
                               "файл с названием encoded_task4.txt: ")
path_to_encoded_container = encoded_container_path + os.sep + 'encoded_task4.txt'
encoded_container = open(path_to_encoded_container, 'r', encoding='cp1251')

decoded_container_path = input("Пожалуйста, введите полный путь к каталогу, в который будет сохранен "
                               "результат (раскодированная секретная фраза) - файл с названием decoded_task4.txt: ")
secret_phrase_decoded_path = decoded_container_path + os.sep + 'decoded_task4.txt'
secret_phrase_decoded = open(secret_phrase_decoded_path, 'w', encoding='cp1251')
map = {'E': 'Е', 'e': 'е', 'T': 'Т', 'H': 'Н', 'O': 'О', 'o': 'о', 'P': 'Р', 'X': 'Х',
       'B': 'В', 'C': 'С', 'c': 'с', 'M': 'М'}

current_letter = ''

while True:
    symbol = encoded_container.read(1)
    if symbol in map.keys():
        current_letter += '1'
    elif symbol in map.values():
        current_letter += '0'
    if len(current_letter) == 8:
        if current_letter == "00000000":
            break
        secret_phrase_decoded.write(bytes([int(current_letter, 2)]).decode('cp1251'))
        current_letter = ''
    if not symbol:
        break

encoded_container.close()
secret_phrase_decoded.close()

print("Дешифрование закончено!")
input("Нажмите Enter, чтобы завершить... ")
