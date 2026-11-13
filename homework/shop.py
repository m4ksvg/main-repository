
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"Товар: {self.name}")
        print(f"Цена: {self.price} тг")
        print(f"Количество: {self.quantity}")


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product.price < 0 or product.quantity < 0:
            print("Ошибка: цена и количество не могут быть отрицательными!")
        else:
            self.products.append(product)
            print(f"{product.name} добавлен в корзину.")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} удалён из корзины.")
                return

        print(f"Товар {name} не найден в корзине.")

    def get_total(self):
        total = 0

        for product in self.products:
            total += product.price * product.quantity

        return total

    def show_cart(self):
        if len(self.products) == 0:
            print("Корзина пуста.")
        else:
            print("\nТовары в корзине:")

            for product in self.products:
                product.show_info()

            print(f"Итого: {self.get_total()} тг")


product1 = Product("Ноутбук", 300000, 2)
product2 = Product("Мышка", 5000, 3)
product3 = Product("Клавиатура", 12000, 1)

cart = Cart()

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

cart.show_cart()

cart.remove_product("Мышка")

cart.show_cart()
