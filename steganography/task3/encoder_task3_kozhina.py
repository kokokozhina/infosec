information_to_hide = open('information_to_hide_task3.txt', 'r', encoding='cp1251').read()  # файл со скрываемой информацией
container = open('container_task3.txt', 'r', encoding='cp1251')  # файл-контейнер
encoded_container = open('encoded_task3.txt', 'w', encoding='cp1251')  # контейнер со скрытой информацией

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
