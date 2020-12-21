information_to_hide = open('information_to_hide_task2.txt', 'r', encoding='cp1251').read()  # файл со скрываемой информацией
container = open('container_task2.txt', 'r', encoding='cp1251')  # файл-контейнер
encoded_container = open('encoded_task2.txt', 'w', encoding='cp1251')  # контейнер со скрытой информацией

bytes_of_hidden_information = information_to_hide.encode('cp1251')
for one_byte in bytes_of_hidden_information:
    bits = bin(one_byte)[2:].zfill(8)
    for bit in bits:
        string = container.readline().replace("\n", "")
        encoded_container.write(string + (" " if bit == '1' else "") + "\n")

while True:
    string = container.readline().replace("\n", "")
    if not string:
        break
    encoded_container.write(string + "\n")

container.close()
encoded_container.close()
