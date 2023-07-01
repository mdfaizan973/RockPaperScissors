import json

menu = []
orders = []

def add_dish(dish_id, dish_name, price):
    dish = {
        'dish_id': dish_id,
        'dish_name': dish_name,
        'price': price,
        'availability': True
    }
    menu.append(dish)
    print(f"Added '{dish_name}' to the menu.")
    print()

def remove_dish(dish_id):
    for dish in menu:
        if dish['dish_id'] == dish_id:
            menu.remove(dish)
            print(f"Removed dish with ID {dish_id} from the menu.")
            print()
            return
    print(f"No dish found with ID {dish_id}.")
    print()

def update_dish_availability(dish_id, availability):
    for dish in menu:
        if dish['dish_id'] == dish_id:
            dish['availability'] = availability
            if availability:
                print(f"'{dish['dish_name']}' is now available.")
            else:
                print(f"'{dish['dish_name']}' is no longer available.")
            print()
            return
    print(f"No dish found with ID {dish_id}.")
    print()

def display_menu():
    print("Current Menu:")
    print("-------------")
    for dish in menu:
        availability = "Available" if dish['availability'] else "Not available"
        print(f"{dish['dish_id']}. {dish['dish_name']} - ${dish['price']} - {availability}")
    print()

def search_dish_by_name(dish_name):
    found_dishes = []
    for dish in menu:
        if dish['dish_name'].lower() == dish_name.lower():
            found_dishes.append(dish)
    if found_dishes:
        print(f"Found {len(found_dishes)} dishes with the name '{dish_name}':")
        for found_dish in found_dishes:
            availability = "Available" if found_dish['availability'] else "Not available"
            print(f"{found_dish['dish_id']}. {found_dish['dish_name']} - ${found_dish['price']} - {availability}")
    else:
        print(f"No dishes found with the name '{dish_name}'.")
    print()

def take_order(customer_name, dish_ids):
    order_dishes = []
    total_price = 0
    for dish_id in dish_ids:
        for dish in menu:
            if dish['dish_id'] == dish_id and dish['availability']:
                order_dishes.append(dish)
                total_price += dish['price']
                break
        else:
            print(f"Dish with ID {dish_id} is not available.")
            print()
            return

    order = {
        'order_id': len(orders) + 1,
        'customer_name': customer_name,
        'dishes': order_dishes,
        'total_price': total_price,
        'status': 'received'
    }
    orders.append(order)
    print(f"Order {order['order_id']} received for {customer_name}.")
    print()

def update_order_status(order_id, status):
    for order in orders:
        if order['order_id'] == order_id:
            order['status'] = status
            print(f"Updated status of Order {order_id} to '{status}'.")
            print()
            return
    print(f"No order found with ID {order_id}.")
    print()

def display_orders(status_filter=None):
    print("Current Orders:")
    print("---------------")
    for order in orders:
        if status_filter is None or order['status'].lower() == status_filter.lower():
            print(f"Order {order['order_id']}: {order['customer_name']} - {order['status']}")
            print("Dishes:")
            for dish in order['dishes']:
                print(f"- {dish['dish_name']} - ${dish['price']}")
            print(f"Total Price: ${order['total_price']}")
            print()

def calculate_total_revenue():
    total_revenue = sum(order['total_price'] for order in orders)
    print(f"Total Revenue: ${total_revenue}")
    print()

def save_data(filename):
    data = {
        'menu': menu,
        'orders': orders
    }
    with open(filename, 'w') as file:
        json.dump(data, file)
    print("Data saved successfully.")
    print()

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            global menu
            menu = data['menu']
            global orders
            orders = data['orders']
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No existing data found. Starting with empty menu and orders.")
    print()

def validate_input(input_text, valid_choices):
    choice = input(input_text)
    while choice not in valid_choices:
        print("Invalid choice. Please try again.")
        choice = input(input_text)
    return choice

while True:
    print("Welcome to Zesty Zomato!")
    print("------------------------")
    print("1. Add a dish to the menu")
    print("2. Remove a dish from the menu")
    print("3. Update dish availability")
    print("4. Take a new order")
    print("5. Update order status")
    print("6. Review all orders")
    print("7. Display menu")
    print("8. Search dish by name")
    print("9. Calculate total revenue")
    print("10. Filter orders by status")
    print("11. Save data")
    print("12. Load data")
    print("13. Exit")

    choice = validate_input("Enter your choice (1-13): ", ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'])

    if choice == '1':
        dish_id = input("Enter the dish ID: ")
        dish_name = input("Enter the dish name: ")
        price = float(input("Enter the price: "))
        add_dish(dish_id, dish_name, price)
    elif choice == '2':
        dish_id = input("Enter the dish ID to remove: ")
        remove_dish(dish_id)
    elif choice == '3':
        dish_id = input("Enter the dish ID to update availability: ")
        availability = input("Enter 'yes' if the dish is available, 'no' otherwise: ").lower() == 'yes'
        update_dish_availability(dish_id, availability)
    elif choice == '4':
        customer_name = input("Enter the customer name: ")
        dish_ids = input("Enter the dish IDs (separated by commas): ").split(',')
        take_order(customer_name, dish_ids)
    elif choice == '5':
        order_id = int(input("Enter the order ID: "))
        status = input("Enter the new status: ")
        update_order_status(order_id, status)
    elif choice == '6':
        display_orders()
    elif choice == '7':
        display_menu()
    elif choice == '8':
        dish_name = input("Enter the dish name to search: ")
        search_dish_by_name(dish_name)
    elif choice == '9':
        calculate_total_revenue()
    elif choice == '10':
        status = input("Enter the status to filter orders: ")
        display_orders(status_filter=status)
    elif choice == '11':
        filename = input("Enter the filename to save data: ")
        save_data(filename)
    elif choice == '12':
        filename = input("Enter the filename to load data: ")
        load_data(filename)
    elif choice == '13':
        print("Thank you for using Zesty Zomato!")
        break
    print()
