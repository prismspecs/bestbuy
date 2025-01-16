from typing import List, Tuple
import products  # assuming the Product class is in a module called products


class Store:
    def __init__(self, product_list: List[products.Product]):
        # initialize the store with a list of products
        self.products = product_list

    def add_product(self, product: products.Product):
        # add a product to the store
        self.products.append(product)

    def remove_product(self, product: products.Product):
        # remove a product from the store
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        # return the total quantity of all products in the store
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[products.Product]:
        # return a list of all active products in the store
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        # handle an order and return the total price
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


# testing the class
def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)

    # add a new product
    new_product = products.Product("Samsung Galaxy S23", price=800, quantity=300)
    store.add_product(new_product)

    # remove a product
    store.remove_product(product_list[2])  # removing "Google Pixel 7"

    # get all active products
    active_products = store.get_all_products()
    print(f"Active products: {[product.show() for product in active_products]}")

    # get total quantity
    print(f"Total quantity: {store.get_total_quantity()}")  # expected: 900

    # place an order
    order_total = store.order([(product_list[0], 2), (product_list[1], 3)])
    print(f"Order cost: {order_total} dollars.")  # expected: 1450*2 + 250*3 = 3950


if __name__ == "__main__":
    main()
