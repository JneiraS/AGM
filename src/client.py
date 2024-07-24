from src.shopping_cart import ShoppingCart


class Client:
    """Ce qui permet à un client de faire ses achats"""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.basket = ShoppingCart(name, [])

    def achat(self, product, quantity, unit_price):
        """La quantité est exprimée en kilo (float ou à la pièce"""
        self.basket += (product, quantity, unit_price)

    def facture(self):
        toll = 0
        for achat in self.basket:
            (product, quantity, unit_price) = achat
            toll += (quantity * unit_price)
            # stock (product) -= quantity
            # Ce n'est pas l'endroit pour le faire,
            # mais ça doit être fait
