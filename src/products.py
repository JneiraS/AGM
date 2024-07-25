# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    stock: float
    unit: str
    price_unit: float

    def subtract_to_stock(self, amount: float):
        self.stock -= amount


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

