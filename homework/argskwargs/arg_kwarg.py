def logger(func):
    def wrapper(*args, **kwargs):
        print("Функция запущена")
        print("Аргументы:", args)
        print("Именованные аргументы:", kwargs)

        func(*args, **kwargs)

        print("Функция завершена")

    return wrapper


@logger
def user_info(name, age, city):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Город: {city}")


user_info("Макс", 15, city="Атырау")