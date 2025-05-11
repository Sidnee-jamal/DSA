class ShoppingCart:
    def add_item(self, age, count):
        self.age = age
        self.count = count
        print(f"{age}, {count} added to cart")

obj1: ShoppingCart = ShoppingCart()
obj1.add_item(20, 2)

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item: str, qty: int, price: float):
        self.items.append({"item": item, "qty": qty, "price": price})

    def remove_item(self, item: str):
        for i in self.items:
            if i["item"] == item:
                self.items.remove(i)
                break  

    def calculate_total(self):
        total = 0
        for i in self.items:
            total += i["qty"] * i["price"]
        return total

    def summary(self):
        print("Item\tQty\tPrice")
        for i in self.items:
            print(f"{i['item']}\t{i['qty']}\tksh {i['price']}")
        print(f"Total: {self.calculate_total()}")

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("apple", 50, 7.5)
    cart.add_item("orange", 2, 2.5)
    cart.add_item("banana", 3, 3.2)
    cart.summary()      

    


    