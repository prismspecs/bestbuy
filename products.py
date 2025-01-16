class Product:
    def __init__(self, name: str, price: float, quantity: int):
        # validate input and initialize instance variables
        if not name.strip():
            raise ValueError("name cannot be empty.")
        if price < 0:
            raise ValueError("price cannot be negative.")
        if quantity < 0:
            raise ValueError("quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        # getter for quantity
        return self.quantity

    def set_quantity(self, quantity: int):
        # setter for quantity, deactivate if quantity is 0
        if quantity < 0:
            raise ValueError("quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        # check if the product is active
        return self.active

    def activate(self):
        # activate the product
        self.active = True

    def deactivate(self):
        # deactivate the product
        self.active = False

    def show(self) -> str:
        # return a string representation of the product
        return f"{self.name}, price: {self.price}, quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        # handle the purchase of a given quantity
        if quantity <= 0:
            raise ValueError("quantity to buy must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("not enough stock to fulfill the purchase.")
        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


# testing the class
def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))  # expected: 12500
    print(mac.buy(100))  # expected: 145000
    print(mac.is_active())  # expected: false (because quantity is now 0)

    print(
        bose.show()
    )  # expected: "Bose QuietComfort Earbuds, price: 250, quantity: 450"
    print(mac.show())  # expected: "MacBook Air M2, price: 1450, quantity: 0"

    bose.set_quantity(1000)
    print(
        bose.show()
    )  # expected: "Bose QuietComfort Earbuds, price: 250, quantity: 1000"


if __name__ == "__main__":
    main()
