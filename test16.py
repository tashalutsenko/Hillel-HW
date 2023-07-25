from datetime import datetime
import time


def dec_time_measure(func):
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"Время выполнение функции {func}: {end - start} секунд")

    return wrapper


@dec_time_measure
def testFunc1():
    print("Выполняется функция testFunc1")
    time.sleep(1)
    print("Функция testFunc1 выполнена")


@dec_time_measure
def testFunc2():
    print("Выполняется функция testFunc2")
    time.sleep(2)
    print("Функция testFunc2 выполнена")


testFunc1()
testFunc2()