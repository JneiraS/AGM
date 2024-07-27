# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame

from src.products import Product, LegumeCreator, FruitCreator


class Stock:
    """
    Classe représentant le stock de produits (fruits et légumes) disponible chez le primeur.
    """

    def __init__(self):
        """
        Constructeur de la classe Stock. Initialise la liste des éléments en stock en appelant la méthode
        statique `generation`.
        """
        self.elements: list[Product] = self.generation()

    @staticmethod
    def generation() -> list:
        """
        Méthode statique pour générer la liste initiale des produits en stock à partir d'un fichier Excel.
        :return : List[Product] : Liste des objets Product représentant les produits en stock.
        """

        stock: list = []

        products_dataframe = pd.read_excel("src/products.xlsx")
        Stock.populate_stock_from_dataframe(products_dataframe, stock)

        return stock

    @staticmethod
    def populate_stock_from_dataframe(
        products_dataframe: DataFrame, stock: list[Product]
    ) -> None:
        """
        Parcourt un DataFrame contenant des informations sur différents produits pour créer et ajouter des
        objets de produit à une liste de stock.

        Cette méthode itère sur chaque ligne du DataFrame fourni. Pour chaque ligne, elle détermine si le
        produit est un 'Légume' ou un 'Fruit' basé sur la première colonne. Ensuite, elle utilise le créateur
        de factory approprié pour créer un objet de produit correspondant et l'ajoute à la liste de stock
        fournie.

        :param products_dataframe: Un DataFrame contenant les informations des produits.
        Chaque ligne représente un produit avec le type de produit ('Légume' ou 'Fruit') dans la première
        colonne.
        :param stock:
        """
        for i in range(len(products_dataframe)):
            len(products_dataframe)
            produit: list = products_dataframe.iloc[i].tolist()

            if produit[0] == "Légume":
                stock.append(LegumeCreator().factory_method(produit))

            if produit[0] == "Fruit":
                stock.append(FruitCreator().factory_method(produit))
