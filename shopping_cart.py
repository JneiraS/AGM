from dataclasses import dataclass

from src.client import Client
from src.products import Product


@dataclass
class ShoppingCart:
    client: Client
    products: list

    def add(self, article: Product):
        self.products.append(article)

    def remoeve(self, article: Product):
        self.products.remove(article)