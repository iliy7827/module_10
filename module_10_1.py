'''Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов,
file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием
после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt

После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt

Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков.'''

import time
from time import sleep
from threading import Thread
from datetime import datetime

time_start1 = datetime.now()

def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding="utf-8") as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(f'Работа функций {time_res1}')

time_start2 = datetime.now()
f1 = Thread(target=wite_words, args=(10, "example5.txt"))
f2 = Thread(target=wite_words, args=(30, "example6.txt"))
f3 = Thread(target=wite_words, args=(200, "example7.txt"))
f4 = Thread(target=wite_words, args=(100, "example8.txt"))
# Запустите эти потоки методом start
f1.start()
f2.start()
f3.start()
f4.start()
# сделать остановку основного потока при помощи join.
f1.join()
f2.join()
f3.join()
f4.join()
time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(f'Работа потоков {time_res2}')