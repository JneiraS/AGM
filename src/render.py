# -*- coding: utf-8 -*-
import os

from src.client import Client
from src.products import Fruit, Legume
from src.stock import Stock


def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux
        os.system('clear')


class ShopTextRenderer:

    def display(self):

        clear_console()
        print("Bienvennue O'Primeur")
        stock = Stock().generation()

        customer_identity: tuple = (input('Votre Nom: '), input('Votre Prenom: '))
        customer: Client = Client(customer_identity[1], customer_identity[0])

        category: str = input('Envie de fruits (F) ou de légumes (L)? : ').upper()
        clear_console()

        if category == "F":
            self.display_filtered_products(stock, Fruit)

        if category == "L":
            self.display_filtered_products(stock, Legume)

        input('\nID article et quantité (ex: 7/1): ')

    @staticmethod
    def display_filtered_products(stock: list, product_type: any) -> None:
        """
        Affiche les détails des produits dans le stock qui correspondent au type spécifié.

        Cette méthode parcourt le stock fourni et affiche les informations de chaque produit
        dont le type correspond au paramètre `product_type`. Les informations affichées incluent
        l'identifiant du produit dans le stock, le nom du produit, la quantité en stock, et le prix unitaire.

        :param stock: Une liste d'objets représentant les produits dans le stock.
        :param product_type: Le type de produit à filtrer. Cette méthode utilise `isinstance` pour
                           comparer chaque produit dans le stock avec le type spécifié.

        """
        for i, e in enumerate(stock):
            if isinstance(e, product_type):
                print(f"id:{i:<5}  {e.name:<20} {e.stock:}\t{e.price_unit:}/{e.unit:}")
