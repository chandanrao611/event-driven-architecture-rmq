from app.services.producer import publish_event
from app.events.event_types import ORDER_CREATED

class OrderService:
    def create_order(self, order_data):
        publish_event(
            ORDER_CREATED,
            order_data
        )
        return order_data

    def get_orders(self):
        publish_event(
            ORDER_CREATED,
            {
                "id": 1,
                "customer": "John",
                "product": "Laptop",
                "quantity": 1,
                "price": 50000,
                "status": "CREATED"
            }
        )
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