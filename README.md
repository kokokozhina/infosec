## Методы защиты информации и информационная безопасность

Практическая работа студентки 273 группы фКНиИТ Кожиной Ольги

Проект содержит 6 заданий:
- Папка *antivirus* содержит задание 1
- Папка *steganography* содержит задание 2, 3 и 4
- Папка *encryption* содержит задание 5 и 6

Каждая папка с заданием имеет исполняемый файл. 

### Задача 1: поиск по сигнатуре заданного файла в указанной директории.

В папке *antivirus* в папке *task1* находится задача 1.

Файл с кодом на python3 - antivirus_task1_kozhina.py.

Выполнение программы происходит в диалоговом режиме. Программе
необходимо задать сдвиг (например, 5), длину сигнатуры (например, 16), полный путь к 
главному файлу - файлу, в котором содержится нужная сигнатура заданной длины 
на заданном сдвиге, а также полный путь к каталогу, в котором нужно найти файлы с заданной сигнатурой.

Для тестирования можно использовать файл *verify.txt* как главный и папку *verify* как директорию
для поиска файлов с заданной сигнатурой.

### Задача 2: задание по стенографии, метод 1

В папке *steganography* в папке *task2* находится задача 2.

Файл с кодом на python3 программы скрытия - encoder_task2_kozhina.py.
Файл с кодом на python3 программы получения скрытой информации - decoder_task2_kozhina.py.
Используемая кодировка - cp1251.

Выполнение программ происходит в файловом режиме.

encoder_task2_kozhina.py просит ввести:
- полный путь к файлу со скрываемой информацией (можно использовать файл information_to_hide_task2.txt из папки task2)
- полный путь к файлу-контейнеру (можно использовать файл container_task2.txt из папки task2)
- полный путь к каталогу, в который будет сохранен результат (файл-контейнер с скрываемой информацией) - файл с названием encoded_task2.txt

decoder_task2_kozhina.py просит ввести:
- полный путь к каталогу, в который сохранен файл с названием encoded_task2.txt
- полный путь к каталогу, в который будет сохранен результат (раскодированная секретная фраза) - файл с названием decoded_task2.txt

### Задача 3: задание по стенографии, метод 2

В папке *steganography* в папке *task3* находится задача 3.

Файл с кодом на python3 программы скрытия - encoder_task3_kozhina.py.
Файл с кодом на python3 программы получения скрытой информации - decoder_task3_kozhina.py.
Используемая кодировка - cp1251.

Выполнение программ происходит в файловом режиме.

encoder_task3_kozhina.py просит ввести:
- полный путь к файлу со скрываемой информацией (можно использовать файл information_to_hide_task3.txt из папки task3)
- полный путь к файлу-контейнеру (можно использовать файл container_task3.txt из папки task3)
- полный путь к каталогу, в который будет сохранен результат (файл-контейнер с скрываемой информацией) - файл с названием encoded_task3.txt

decoder_task3_kozhina.py просит ввести:
- полный путь к каталогу, в который сохранен файл с названием encoded_task3.txt
- полный путь к каталогу, в который будет сохранен результат (раскодированная секретная фраза) - файл с названием decoded_task3.txt


### Задача 4: задание по стенографии, метод 3

В папке *steganography* в папке *task4* находится задача 4.

Файл с кодом на python3 программы скрытия - encoder_task4_kozhina.py.
Файл с кодом на python3 программы получения скрытой информации - decoder_task4_kozhina.py.
Используемая кодировка - cp1251.

Выполнение программ происходит в файловом режиме.

encoder_task4_kozhina.py просит ввести:
- полный путь к файлу со скрываемой информацией (можно использовать файл information_to_hide_task4.txt из папки task4)
- полный путь к файлу-контейнеру (можно использовать файл container_task4.txt из папки task4)
- полный путь к каталогу, в который будет сохранен результат (файл-контейнер с скрываемой информацией) - файл с названием encoded_task4.txt

decoder_task4_kozhina.py просит ввести:
- полный путь к каталогу, в который сохранен файл с названием encoded_task4.txt
- полный путь к каталогу, в который будет сохранен результат (раскодированная секретная фраза) - файл с названием decoded_task4.txt


### Задача 5: cхема шифрования Вижинера

В папке *encryption* в папке *task5* находится задача 5.

Файл с кодом на python3 - vigenere_task5_kozhina.py.

Выполнение программы происходит в диалоговом режиме.

Программе необходимо задать режим: 1 для шифрования, 0 для дешифрования. Затем ввести ключ шифрования, а затем 
текст для шифрования\дешифрования. Результат работы программы будет выведен на экран.

### Задача 6: Шифрование каталога

В папке *encryption* в папке *task6* находится задача 6.

Файл с кодом на python3 - archive_encryption_task6_kozhina.py.

Выполнение программы происходит в диалоговом режиме.

Программе необходимо задать режим: 1 для шифрования, 0 для расшифрования. 
Затем ввести ключ шифрования, а затем указать полный путь к каталогу для его шифрования\ввести полный путь к файлу для дешифрования каталога.
В режиме шифрования также следует ввести полный путь к каталогу, в который будет сохранен результат - файл *encrypted_archive_task6.txt*.

Результатом шифрования каталога будет файл *encrypted_archive_task6.txt* в указанной папке.

Результатом дешифрования каталога будет восстановленный каталог (который был зашифрован ранее).




