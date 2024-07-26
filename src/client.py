# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.products import Product


class Client:
    """Ce qui permet à un client de faire ses achats"""
    clients: list = []

    def __init__(self, name, surname):
        self.name: str = name
        self.surname: str = surname
        self.basket = ShoppingCart(name, [])
        Client.clients.append(self)


@dataclass
class ShoppingCart:
    client: Client
    products: list

    def add(self, article: Product):
        self.products.append(article)

    def remove(self, article: Product):
        self.products.remove(article)
