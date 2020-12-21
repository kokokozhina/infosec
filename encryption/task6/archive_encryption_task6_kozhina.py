import os
import shutil


def vigenere(data, key, is_encrypt):
    key = bytearray(key, "utf-8")
    result = ""
    for i in range(len(data)):
        row = key[i % len(key)]
        column = data[i] if is_encrypt else ord(data[i])
        current_char = (row + column) % 256 if is_encrypt else (column + 256 - row) % 256
        result += chr(current_char)
    return result


def encrypt(folder, key, files, paths):
    for obj in os.listdir(folder):
        path = folder + os.sep + obj
        if os.path.isdir(path):
            encrypt(path, key, files, paths)
        else:
            file = open(path, mode='rb')
            content = file.read()
            files.append(vigenere(content, key, True))
            paths.append(vigenere(path.encode("utf-8"), key, True))
            file.close()


def write_lengths(output, num, paths, files):
    for i in range(num):
        output.write(vigenere(str(len(paths[i])).zfill(8).encode("utf-8"), key, True))
        output.write(vigenere(str(len(files[i])).zfill(8).encode("utf-8"), key, True))


def read_lengths(input, num, paths, files):
    for i in range(num):
        paths.append(int(vigenere(input.read(8), key, False)))
        files.append(int(vigenere(input.read(8), key, False)))


def write_arr(output, num, paths, files):
    for i in range(num):
        output.write(paths[i])
        output.write(files[i])


def encrypt_folder(path):
    files = []
    paths = []
    encrypted = open('encrypted_archive_task6.txt', 'w', encoding='utf-8')
    encrypt(path, key, files, paths)
    number_of_files = len(files)
    encrypted.write(vigenere(str(number_of_files).zfill(8).encode("utf-8"), key, True))
    write_lengths(encrypted, number_of_files, paths, files)
    write_arr(encrypted, number_of_files, paths, files)
    encrypted.close()


def decrypt_file(path, key):
    file = open(path, 'r', encoding="utf-8")
    number_of_files = int(vigenere(file.read(8), key, False))
    paths = []
    files = []
    read_lengths(file, number_of_files, paths, files)
    for i in range(number_of_files):
        p = vigenere(file.read(paths[i]), key, False)
        f = vigenere(file.read(files[i]), key, False)
        if not os.path.exists(os.path.dirname(p)):
            os.makedirs(os.path.dirname(p))
        extracted = open(p, 'w', encoding="utf-8")
        extracted.write(f)
        extracted.close()


action = input("Введите 1, чтобы зашифровать, 0, чтобы расшифровать: ")
key = input("Пожалуйста, введите ключ шифрования: ")
if action == "1":
    folder = input("Пожалуйста, введите полный путь к каталогу для его шифрования: ")
    encrypt_folder(folder)
    shutil.rmtree(folder)
elif action == "0":
    path = input("Пожалуйста, введите полный путь к файлу для его дешифрования: ")
    decrypt_file(path, key)
    os.remove(path)
else:
    print("Извините, непонятный символ. Давайте повторим заново.")
