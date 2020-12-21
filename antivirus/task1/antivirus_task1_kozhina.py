import os

files_with_needed_signature = []


def scan_folder(folder):
    for item in os.listdir(folder):
        path = folder + os.sep + item
        if os.path.isdir(path):
            scan_folder(path)
        else:
            file = open(path, 'r', encoding="utf-8")
            content = file.read()
            if content.find(signature) != -1:
                files_with_needed_signature.append(path)
            file.close()


offset = int(input("Пожалуйста, введите сдвиг: "))
signature_length = int(input("Пожалуйста, введите длину сигнатуры: "))
verify_file_path = input("Пожалуйста, введите полный путь к главному файлу - файл, "
                         "который содержит сигнатуру указанной длины на указанном сдвиге.\n"
                         "Поиск файлов с нужной сигнатурой будет произведен в каталоге, где лежит главный файл: ")

signature = ""
verify_file = open(verify_file_path, 'r', encoding="utf-8")
for i in range(offset):
    verify_file.read(1)
for i in range(signature_length):
    signature += verify_file.read(1)
verify_file.close()

print(f"Заданная сигнатура = {signature}")

dir_path = verify_file_path.rsplit(os.sep, 1)[0]
scan_folder(dir_path)

print("Вот пути к файлам с заданной сигнатурой: ")
for good_file in files_with_needed_signature:
    print(good_file)
