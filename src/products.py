# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from dataclasses import dataclass

import pandas as pd

products_dataframe = pd.read_excel('products.xlsx')


@dataclass
class Product(ABC):
    name: str
    stock: int
    unit: str
    price_unit: float


@dataclass
class Fruit(Product):
    ...


@dataclass
class Legume(Product):
    ...


class Creator(ABC):

    @abstractmethod
    def factory_method(self, line):
        pass


class FruitCreator(Creator):

    def factory_method(self, line: list) -> Product:
        return Fruit(line[1], line[2], line[3], line[4])


class LegumeCreator(Creator):

    def factory_method(self, line: list) -> Product:
        return Legume(line[1], line[2], line[3], line[4])


