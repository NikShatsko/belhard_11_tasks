import time


def wait_for_one(func):
    def wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper


@wait_for_one
def countdown(n):
    print(f"Функция {n} выполнена за одну секунду")

