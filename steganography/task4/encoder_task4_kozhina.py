information_to_hide = open('information_to_hide_task4.txt', 'r', encoding='cp1251').read()  # файл со скрываемой информацией
container = open('container_task4.txt', 'r', encoding='cp1251')  # файл-контейнер
encoded_container = open('encoded_task4.txt', 'w', encoding='cp1251')  # контейнер со скрытой информацией
map = {'Е': 'E', 'е': 'e', 'Т': 'T', 'Н': 'H', 'О': 'O', 'о': 'o', 'Р': 'P', 'Х': 'X',
       'В': 'B', 'С': 'C', 'с': 'c', 'М': 'M'}

bytes_of_hidden_information = information_to_hide.encode('cp1251')
for one_byte in bytes_of_hidden_information:
    bits = bin(one_byte)[2:].zfill(8)
    for bit in bits:
        symbol = ''
        while symbol not in map.keys():
            encoded_container.write(symbol)
            symbol = container.read(1)
        encoded_container.write(map.get(symbol) if bit == '1' else symbol)

while True:
    symbol = container.read(1)
    encoded_container.write(symbol)
    if not symbol:
        break

container.close()
encoded_container.close()
