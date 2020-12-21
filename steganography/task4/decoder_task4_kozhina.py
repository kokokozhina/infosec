encoded_container = open('encoded_task4.txt', 'r', encoding='cp1251')  # контейнер со скрытой информацией
secret_phrase_decoded = open('decoded_task4.txt', 'w', encoding='cp1251')  # раскодированная секретная фраза
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
