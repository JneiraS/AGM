# -*- coding: utf-8 -*-
import pandas as pd

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
    def generation():
        """
        Méthode statique pour générer la liste initiale des produits en stock à partir d'un fichier Excel.
        :return: List[Product]: Liste des objets Product représentant les produits en stock.
        """

        stock: list = []

        products_dataframe = pd.read_excel('src/products.xlsx')

        for i in range(len(products_dataframe)):
            len(products_dataframe)
            produit: list = products_dataframe.iloc[i].tolist()

            if produit[0] == 'Légume':
                stock.append(LegumeCreator().factory_method(produit))

            if produit[0] == 'Fruit':
                stock.append(FruitCreator().factory_method(produit))

        return stock


