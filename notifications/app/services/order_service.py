class OrderService:
    def create_order(self, order_data):
        return order_data

    def get_orders(self):
        return [
            {
                "id": 1,
                "customer": "John",
                "product": "Laptop",
                "quantity": 1,
                "price": 50000,
                "status": "CREATED"
            },
            {
                "id": 2,
                "customer": "Alice",
                "product": "Mouse",
                "quantity": 2,
                "price": 1000,
                "status": "SHIPPED"
            }
        ]