import time
from threading import Thread, Event

def first_worker():
    print('Первый работник приступил к своей задаче')
    event.wait()
    print('Первый работник продолжил выполнять задачу')
    time.sleep(5)
    print('Первый работник закончил выполнять задачу')

def second_worker():
    print('Второй работник приступил к своей задаче')
    time.sleep(10)
    print('Второй работник закончил выполнять задачу')
    event.set()

event = Event() # создаем объект класса Event
event.set()
event.clear()
print(event.is_set())

thread1 = Thread(target=first_worker) #создадим 1 и 2 потоки
thread2 = Thread(target=second_worker)
thread1.start()
thread2.start()

