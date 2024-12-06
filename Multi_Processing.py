import multiprocessing
import time
import threading

counter = 0

def first_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(1)
        print('Первый работник изменил значение счетчика', counter)
    print('Первый работник изменил значение счетчика', counter)

def second_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(1)
        print('Второй работник изменил значение счетчика', counter)
    print('Второй работник изменил значение счетчика', counter)


thread1 = threading.Thread(target=first_worker, args=(10,))
thread2 = threading.Thread(target=second_worker, args=(5,))
thread1.start()
thread2.start()
#if __name__ == '__main__':

#    process1 = multiprocessing.Process(target=first_worker, args=(10, ))
 #   process2 = multiprocessing.Process(target=second_worker, args=(15, ))
  #  process1.start()
 #   process1.start()

