import os
import codecs

files_with_needed_signature = []


def scan_folder(folder):
    for item in os.listdir(folder):
        path = folder + os.sep + item
        if os.path.isdir(path):
            scan_folder(path)
        else:
            file = codecs.open(path, 'r', encoding='utf-8', errors='ignore')
            content = file.read()
            if content.find(signature) != -1:
                files_with_needed_signature.append(path)
            file.close()


offset = int(input("Пожалуйста, введите сдвиг (целое положительное число): "))
signature_length = int(input("Пожалуйста, введите длину сигнатуры (целое положительное число): "))
verify_file_path = input("Пожалуйста, введите полный путь к главному файлу - файл, "
                         "который содержит сигнатуру указанной длины на указанном сдвиге: ")\
    .strip(' \0\1\2\3\4\5\6\a\b\t\n\v\f\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f')

signature = ""
verify_file = codecs.open(verify_file_path, 'r', encoding="utf-8", errors='ignore')
for i in range(offset):
    verify_file.read(1)
for i in range(signature_length):
    signature += verify_file.read(1)
verify_file.close()

print(f"Заданная сигнатура = {signature}")

dir_path = input("Пожалуйста, введите полный путь к каталогу, в котором нужно найти файлы с заданной сигнатурой: ")\
    .strip(' \0\1\2\3\4\5\6\a\b\t\n\v\f\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f')
scan_folder(dir_path)

print("Вот пути к файлам с заданной сигнатурой: ")
for good_file in files_with_needed_signature:
    print(good_file)

input("Нажмите Enter, чтобы завершить... ")
