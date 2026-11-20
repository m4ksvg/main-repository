def logger(func):
    def wrapper():
        print("Функция запущена")
        func()
        print("Функция завершена")
    return wrapper


@logger
def greet():
    print("Привет! Добро пожаловать!")


greet()