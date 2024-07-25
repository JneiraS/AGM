# -*- coding: utf-8 -*-
import os

from src.client import Client
from src.invoice import Invoice
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
        print("Bienvenue O'Primeur")
        stock = Stock().generation()

        customer_identity: tuple = (input('Votre Nom: '), input('Votre Prenom: '))
        customer: Client = Client(customer_identity[1], customer_identity[0])
        invoice_customer = Invoice(customer)
        response = ''

        while response != 'N':

            category: str = input('Envie de fruits (F) ou de légumes (L)? \nPayer (P): ').upper()
            clear_console()

            while True:

                if category == "F":
                    self.display_and_select_product(customer, stock, Fruit)
                    break

                if category == "L":
                    self.display_and_select_product(customer, stock, Legume)
                    break

                if category == "P":
                    clear_console()
                    invoice_customer.print()

                    response: str = input("\nNouveau Client (N) ou afficher le bilan de la journée (B)? : ")
                    if response == 'B':
                        clear_console()
                        print('Afficher le bilan de la journée')
                    if response == 'N':
                        break
                    break


    def display_and_select_product(self, client: Client, stock: list, product: any) -> None:
        """
        Affiche les produits filtrés du stock jusqu'à ce que l'utilisateur choisisse de retourner.

        Cette méthode affiche d'abord l'en-tête, puis les produits filtrés basés sur le stock et le produit
        spécifié. Elle demande ensuite à l'utilisateur si il souhaite acheter un produit (en entrant son ID et
        quantité) ou retourner au menu principal (en entrant 'R'). Le processus se répète jusqu'à ce que
        l'utilisateur choisisse de retourner.
        :param client:
        :param stock:
        :param product:
        Note:
        - Assurez-vous que les méthodes `header` et `display_filtered_products` sont correctement
        implémentées dans la même classe.
        - La fonction `clear_console()` doit être définie quelque part dans votre code pour nettoyer la
        console après chaque itération.
        """

        while True:
            self.header()
            self.display_filtered_products(stock, product)
            response: str = input('\nAcheter (Id/Qt) ou Retour (R): ').upper()
            if response != 'R':
                request: list = response.split(sep='/')
                stock[int(request[0])].subtract_to_stock(float(request[1]))
                client.basket.add(
                    product(stock[int(request[0])].name, float(request[1]), stock[int(request[0])].unit,
                            stock[int(
                                request[0])].price_unit))
                clear_console()
            else:
                break

    @staticmethod
    def header():

        print(f"Id:{"":<5}  {'Name':<20} {'Qt'}\t\t{'Price'}")
        print("-" * 50)

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
                print(f"Id:{i:<5}  {e.name:<20} {e.stock:.1f}\t\t{e.price_unit:}€/{e.unit:}")
