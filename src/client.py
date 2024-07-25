# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.products import Product


class Client:
    """Ce qui permet à un client de faire ses achats"""
    clients = []

    def __init__(self, name, surname):
        self.name: str = name
        self.surname: str = surname
        self.basket = ShoppingCart(name, [])
        Client.clients.append(self)

    def achat(self, product, quantity, unit_price):
        """La quantité est exprimée en kilo (float ou à la pièce"""
        self.basket += (product, quantity, unit_price)


@dataclass
class ShoppingCart:
    client: Client
    products: list

    def add(self, article: Product):
        self.products.append(article)

    def remoeve(self, article: Product):
        self.products.remove(article)
