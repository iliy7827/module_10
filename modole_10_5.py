# Задача "Многопроцессное считывание"
import time
import multiprocessing

def read_info(name):
    '''Функция должна:
Создавать локальный список all_data.
Открывать файл name для чтения.
Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
Во время считывания добавлять каждую строку в список all_data.'''
    all_data = []
    with open(name, 'r') as file:
        content = file.readline()
        while content:
            content = file.readline()
            all_data.append(content[0:-1])
            if not content:
                break
#filenames = [f'./file {number}.txt' for number in range(1, 5)]
filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
#Линейный вызов
start_time = time.time()
read_info(filenames[0])
read_info(filenames[1])
read_info(filenames[2])
read_info(filenames[3])
used_time = time.time() - start_time
print(f'Линейный вызов {used_time}')


# многопроцессный
if __name__ == '__main__':
    start_time2 = time.time()

    with multiprocessing.Pool(processes=4) as pool:
       pool.map(read_info, filenames)

    used_time2 = time.time() - start_time2
    print(f'Многопроцессный вызов: {used_time2}')