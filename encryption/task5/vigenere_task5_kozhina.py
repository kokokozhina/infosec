alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
index = 0
uppercase_letter = False

action = input("Введите 1, чтобы зашифровать, 0, чтобы расшифровать: ")
if action == '1':
    print("Шифрование!")
    key = input("Пожалуйста, введите ключ шифрования: ").lower()\
        .strip(' \0\1\2\3\4\5\6\a\b\t\n\v\f\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f')
    text = input("Пожалуйста, введите текст для шифрования: ")\
        .strip(' \0\1\2\3\4\5\6\a\b\t\n\v\f\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f')
    letter_in_key = key[index]

    encrypted_text = ""
    for letter in text:
        if letter.isupper():
            uppercase_letter = True
            letter = letter.lower()
        current_position = alphabet.find(letter)
        current_key = alphabet.find(letter_in_key)
        encrypted_letter = alphabet[(current_position + current_key) % len(alphabet)]
        if uppercase_letter:
            encrypted_text += encrypted_letter.upper()
            uppercase_letter = False
        else:
            encrypted_text += encrypted_letter
        index = (index + 1) % len(key)
        letter_in_key = key[index]

    print(f"Зашифрованный текст: {encrypted_text}")

elif action == '0':
    print("Дешифрование!")
    key = input("Пожалуйста, введите ключ шифрования: ").lower()\
        .strip(' \0\1\2\3\4\5\6\a\b\t\n\v\f\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f')
    text = input("Пожалуйста, введите текст для дешифрования: ")\
        .strip(' \0\1\2\3\4\5\6\a\b\t\n\v\f\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f')
    letter_in_key = key[index]

    decrypted_text = ""
    for letter in text:
        if letter.isupper():
            letter = letter.lower()
            uppercase_letter = True

        current_position = alphabet.find(letter)
        current_key = alphabet.find(letter_in_key)
        decrypted_letter = alphabet[(current_position + len(alphabet) - current_key) % len(alphabet)]
        if uppercase_letter:
            decrypted_text += decrypted_letter.upper()
            uppercase_letter = False
        else:
            decrypted_text += decrypted_letter

        index = (index + 1) % len(key)
        letter_in_key = key[index]

    print(f"Дешифрованный текст: {decrypted_text}")

else:
    print("Извините, непонятный символ. Давайте повторим заново.")

input("Нажмите Enter, чтобы завершить... ")
