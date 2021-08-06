import time


def wait_for_two(func):
    def wrapper(*args, **kwargs):
        time.sleep(2)
        return func(*args, **kwargs)

    return wrapper


def wait_for_three(func):
    def wrapper(*args, **kwargs):
        time.sleep(3)
        return func(*args, **kwargs)

    return wrapper


@wait_for_two
def countdown2(a):
    print(f"Функция {a} выполнена за две секунды")


@wait_for_three
def countdown3(a):
    print(f"Функция {a} выполнена за три секунды")
