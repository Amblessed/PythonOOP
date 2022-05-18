class Item:
    pay_rate: float = 0.8 # The pay after 20% discount
    all_instances: list = []
    
    def __init__(self, name: str, price: float, quantity: int) -> None:
        
        # Run validations on the received arguments
        assert price > 0, f"Price {price} is not greater than zero"
        assert quantity > 0, f"Quantity {quantity} is not greater than zero"
        
        # Assign to self object 
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all_instances.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    def __repr__(self) -> str:
        return f'Item("{self.name}", {self.price}, {self.quantity})'


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 8)
item3 = Item("HDMI Cable", 10, 50)
item4 = Item("Mouse", 20, 100)
item5 = Item("Keyboard", 75, 5)
print(Item.all_instances)

