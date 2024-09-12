class Graph:
    def __init__(self):
        # Graph structure represented as an adjacency list
        self.graph = {}

    # Add a table to the restaurant system
    def add_table(self, table_id, capacity):
        if table_id not in self.graph:
            self.graph[table_id] = {
                "type": "table",
                "capacity": capacity,
                "customers": [],
                "orders": []
            }
            print(f"Table {table_id} with capacity {capacity} added.")
        else:
            print(f"Table {table_id} already exists.")

    # Add a customer to a specific table
    def add_customer(self, customer_id, customer_name, table_id):
        if table_id in self.graph and self.graph[table_id]["type"] == "table":
            new_customer = {
                "customer_id": customer_id,
                "customer_name": customer_name,
                "orders": []
            }
            self.graph[table_id]["customers"].append(new_customer)
            self.graph[customer_id] = {
                "type": "customer",
                "name": customer_name,
                "table_id": table_id,
                "orders": []
            }
            print(f"Customer {customer_name} added to Table {table_id}.")
        else:
            print(f"Table {table_id} does not exist.")

    # Add a menu item
    def add_menu_item(self, item_id, item_name, price):
        if item_id not in self.graph:
            self.graph[item_id] = {
                "type": "menu_item",
                "name": item_name,
                "price": price
            }
            print(f"Menu Item '{item_name}' added with ID {item_id} and price {price}.")
        else:
            print(f"Menu Item '{item_name}' already exists.")

    # Place an order by connecting a customer to a menu item
    def place_order(self, customer_id, item_id, quantity):
        if customer_id in self.graph and self.graph[customer_id]["type"] == "customer":
            if item_id in self.graph and self.graph[item_id]["type"] == "menu_item":
                item = self.graph[item_id]
                customer = self.graph[customer_id]

                # Create an order dictionary
                order = {
                    "item_id": item_id,
                    "item_name": item["name"],
                    "quantity": quantity,
                    "total_price": item["price"] * quantity
                }

                # Add the order to the customer node
                customer["orders"].append(order)

                # Add the order to the customer's table node
                table_id = customer["table_id"]
                self.graph[table_id]["orders"].append(order)

                print(f"Order placed by {customer['name']} for {quantity}x {item['name']} (Total: ${order['total_price']:.2f}).")
            else:
                print(f"Menu Item with ID {item_id} does not exist.")
        else:
            print(f"Customer with ID {customer_id} does not exist.")

    # View all orders for a specific table
    def view_table_orders(self, table_id):
        if table_id in self.graph and self.graph[table_id]["type"] == "table":
            table = self.graph[table_id]
            if table["orders"]:
                print(f"Orders for Table {table_id}:")
                for order in table["orders"]:
                    print(f"- {order['quantity']}x {order['item_name']} (Total: ${order['total_price']:.2f})")
            else:
                print(f"No orders for Table {table_id}.")
        else:
            print(f"Table {table_id} does not exist.")

    # View all customers seated at a specific table
    def view_table_customers(self, table_id):
        if table_id in self.graph and self.graph[table_id]["type"] == "table":
            table = self.graph[table_id]
            if table["customers"]:
                print(f"Customers at Table {table_id}:")
                for customer in table["customers"]:
                    print(f"- {customer['customer_name']}")
            else:
                print(f"No customers at Table {table_id}.")
        else:
            print(f"Table {table_id} does not exist.")

    # View menu items
    def view_menu(self):
        print("Menu Items:")
        for node_id, node_data in self.graph.items():
            if node_data["type"] == "menu_item":
                print(f"- {node_data['name']} (ID: {node_id}, Price: ${node_data['price']:.2f})")

    # View all tables
    def view_all_tables(self):
        print("Tables in the restaurant:")
        for node_id, node_data in self.graph.items():
            if node_data["type"] == "table":
                print(f"- Table {node_id} (Capacity: {node_data['capacity']})")

    # View all orders in the restaurant
    def view_all_orders(self):
        print("All orders in the restaurant:")
        for node_id, node_data in self.graph.items():
            if node_data["type"] == "table":
                for order in node_data["orders"]:
                    print(f"- Table {node_id}: {order['quantity']}x {order['item_name']} (Total: ${order['total_price']:.2f})")


# Example Usage of the Restaurant Management System
if __name__ == "__main__":
    restaurant = Graph()

    # Add tables
    restaurant.add_table("T1", 4)
    restaurant.add_table("T2", 6)

    # Add menu items
    restaurant.add_menu_item("M1", "Pizza", 12.99)
    restaurant.add_menu_item("M2", "Pasta", 8.99)
    restaurant.add_menu_item("M3", "Salad", 5.99)

    # Add customers to tables
    restaurant.add_customer("C1", "Harish", "T1")
    restaurant.add_customer("C2", "Dev", "T1")
    restaurant.add_customer("C3", "Rutvik", "T2")

    # Place orders
    restaurant.place_order("C1", "M1", 2)  # Alice orders 2 Pizzas
    restaurant.place_order("C2", "M2", 1)  # Bob orders 1 Pasta
    restaurant.place_order("C3", "M3", 3)  # Charlie orders 3 Salads

    # View table orders
    restaurant.view_table_orders("T1")
    restaurant.view_table_orders("T2")

    # View customers at a table
    restaurant.view_table_customers("T1")
    restaurant.view_table_customers("T2")

    # View the full menu
    restaurant.view_menu()

    # View all orders in the restaurant
    restaurant.view_all_orders()

