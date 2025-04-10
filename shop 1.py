class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Пустой словарь для товаров

    def add_item(self, item_name, price):
        """Добавление товара в ассортимент"""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаление товара из ассортимента"""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Получение цены товара"""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновление цены товара"""
        if item_name in self.items:
            self.items[item_name] = new_price

    def show_inventory(self):
        """Показать все товары"""
        return self.items

# Создание объектов магазинов
store1 = Store("Фруктовый рай", "ул. Садовая, 12")
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2 = Store("Молочная лавка", "пр. Молочный, 3")
store2.add_item("молоко", 1.2)
store2.add_item("сыр", 2.5)

store3 = Store("Хлебный дом", "ул. Пекарская, 18")
store3.add_item("хлеб", 0.8)
store3.add_item("булочка", 1.1)

# Пример использования
print("Ассортимент магазина 1:", store1.show_inventory())
print("Цена бананов:", store1.get_price("бананы"))

store1.update_price("яблоки", 0.55)
print("Новая цена яблок:", store1.get_price("яблоки"))

store1.remove_item("бананы")
print("Ассортимент после удаления бананов:", store1.show_inventory())
