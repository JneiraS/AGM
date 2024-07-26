# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Product:
    """
    Représente un produit.
    """
    name: str
    stock: float
    unit: str
    price_unit: float

    def subtract_to_stock(self, amount: float):
        self.stock -= amount


@dataclass
class Fruit(Product):
    """
    Représente un fruit.
    Hérite de la classe Product et ajoute des fonctionnalités spécifiques aux fruits si nécessaire.
    """
    ...


@dataclass
class Legume(Product):
    """
    Représente un légume.
    Hérite de la classe Product et ajoute des fonctionnalités spécifiques aux fruits si nécessaire.
    """
    ...


class Creator(ABC):
    """
    Classe abstraite qui définit une interface pour créer des objets Product.
    """
    @abstractmethod
    def factory_method(self, dataframe_line):
        """
        Méthode abstraite pour créer et retourner un objet Product à partir d'une ligne de données.
        """
        pass


class FruitCreator(Creator):
    """
    Implémente la méthode factory_method pour créer des objets Fruit.
    """

    def factory_method(self, dataframe_line: list) -> Fruit:
        """
        Crée et retourne un nouvel objet Fruit à partir d'une ligne de données.
        """
        return Fruit(dataframe_line[1], dataframe_line[2], dataframe_line[3], dataframe_line[4])


class LegumeCreator(Creator):
    """
    Implémente la méthode factory_method pour créer des objets Legume.
    """

    def factory_method(self, dataframe_line: list) -> Legume:
        """
        Crée et retourne un nouvel objet Legume à partir d'une ligne de données.
        """
        return Legume(dataframe_line[1], dataframe_line[2], dataframe_line[3], dataframe_line[4])
