# -*- coding: utf-8 -*-
import os

from src.client import Client
from src.invoice import Invoice, day_review
from src.products import Fruit, Legume


def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux
        os.system('clear')


class ShopTextRenderer:

    def display(self, stock):

        customer, invoice_customer, response = self.initialize_customer_interaction()
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

                    response: str = input(
                        "\nNouveau Client (N) ou afficher le bilan de la journée (B)? : ").upper()
                    if response == 'B':
                        self.display_daily_inventory_summary(stock)

                    if response == 'N':
                        break
                    break

    @staticmethod
    def display_daily_inventory_summary(stock):
        """
        Affiche un récapitulatif du stock disponible au jour.
        Cette méthode efface l'écran, affiche un titre "Bilan de la journée",
        suivi du montant total des ventes réalisées aujourd'hui (calculé par la fonction `day_review`),
        et ensuite liste tous les articles disponibles dans le stock, montrant leur nom, quantité et unité.

        :param stock:
        :return:
        """

        clear_console()
        print('Bilan de la journée')
        print(f"{day_review():.2f} €")
        print('-' * 30)
        print(f'{'STOCK':^30}')
        print('-' * 30)
        for i in stock:
            print(f'{i.name}  {i.stock} {i.unit}')

    @staticmethod
    def initialize_customer_interaction():

        """
        Initialise une interaction avec un nouveau client en créant un profil et une facture.

        Cette méthode efface la console, affiche un message de bienvenue, puis demande à l'utilisateur
        d'entrer son nom et prénom.
        Avec ces informations, elle crée un objet Client et génère une facture pour ce client.
        Elle retourne l'objet Client créé, la facture associée, et une chaîne vide représentant la réponse.

        :return: Un tuple contenant l'objet Client créé, l'objet Invoice associé, et une chaîne vide
        représentant la réponse.
        """

        response = ''
        clear_console()
        print("Bienvenue O'Primeur")
        customer_identity: tuple = (input('Votre Nom: '), input('Votre Prenom: '))
        customer: Client = Client(customer_identity[1], customer_identity[0])
        invoice_customer = Invoice(customer)
        return customer, invoice_customer, response

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
