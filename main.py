import products
import store


# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = store.Store(product_list)


def start(store_object):
    while True:
        print("\nWelcome to the store! Please choose an option:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # list all products in store
            print("\nProducts in the store:")
            for product in store_object.get_all_products():
                print(product.show())

        elif choice == "2":
            # show total amount in store
            total_quantity = store_object.get_total_quantity()
            print(f"\nTotal quantity of items in store: {total_quantity}")

        elif choice == "3":
            # make an order
            print(
                "\nEnter your order. Type the product name and quantity separated by a comma."
            )
            print("Type 'done' when you are finished.")
            shopping_list = []
            while True:
                order_input = input("Order item (or 'done'): ").strip()
                if order_input.lower() == "done":
                    break
                try:
                    name, quantity = order_input.split(",")
                    name = name.strip()
                    quantity = int(quantity.strip())
                    # find the product in the store
                    product = next(
                        (p for p in store_object.get_all_products() if p.name == name),
                        None,
                    )
                    if product:
                        shopping_list.append((product, quantity))
                    else:
                        print(f"Product '{name}' not found.")
                except ValueError:
                    print(
                        "Invalid input. Please enter in the format: product_name, quantity."
                    )

            if shopping_list:
                try:
                    total_price = store_object.order(shopping_list)
                    print(
                        f"\nOrder placed successfully! Total price: {total_price} dollars."
                    )
                except Exception as e:
                    print(f"Error placing order: {e}")

        elif choice == "4":
            # quit the program
            print("Thank you for visiting the store. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    start(best_buy)
