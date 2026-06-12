class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Cena produktu nie może być ujemna.")
        if quantity < 0:
            raise ValueError("Początkowa ilość w magazynie nie może być ujemna.")
            
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Ilość dodawana do magazynu nie może być ujemna.")
        self.quantity += amount

    def remove_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Ilość usuwana z magazynu nie może być ujemna.")
        if amount > self.quantity:
            raise ValueError("Nie można usunąć więcej niż jest w magazynie.")
        self.quantity -= amount

    def is_available(self) -> bool:
        return self.quantity > 0

    def total_value(self) -> float:
        return self.price * self.quantity