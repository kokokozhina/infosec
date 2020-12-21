encoded_container = open('encoded_task3.txt', 'r', encoding='cp1251')  # контейнер со скрытой информацией
secret_phrase_decoded = open('decoded_task3.txt', 'w', encoding='cp1251')  # раскодированная секретная фраза

current_letter = ""

while True:
    symbol = encoded_container.read(1)
    if symbol == ' ':
        next_symbol = encoded_container.read(1)
        current_letter += '1' if next_symbol == ' ' else '0'
    if len(current_letter) == 8:
        if current_letter == "00000000":
            break
        secret_phrase_decoded.write(bytes([int(current_letter, 2)]).decode('cp1251'))
        current_letter = ''

encoded_container.close()
secret_phrase_decoded.close()
