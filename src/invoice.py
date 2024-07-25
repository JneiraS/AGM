from datetime import datetime

from src.client import Client


def day_review():
    for invoice in Invoice.review_of_the_day:
        print(f'{invoice.date}:\t\t{invoice.client.name} {invoice.client.name} :'
              f' {invoice.calculate_total_basket_value()}')
    return sum([i.calculate_total_basket_value() for i in Invoice.review_of_the_day])


class Invoice:
    review_of_the_day: list = []

    def __init__(self, client: Client):
        self.client: Client = client
        self.date: str = datetime.today().strftime("%d/%m/%Y à %H:%M")
        Invoice.review_of_the_day.append(self)

    def print(self):
        print(f"\tFacture de :{self.client.name} {self.client.surname}")
        print(f"\tDate d'acaht: {self.date}\n")
        print('\t\tRECAPITULATIF\n')
        print('\t-------------------------')

        print(f"{'Name':<20} {'Qt'}\t\t{'Price'}")
        for article in self.client.basket.products:
            print(f"{article.name:<20} {article.stock}\t"
                  f"{article.stock * article.price_unit:.2f} €")
        print(f'\t-------------------------')
        print(f'{'TOTAL HT':>20}:   {self.calculate_total_basket_value() * 0.8:.2f}  €')
        print(f'{'TOTAL TTC':>20}:   {self.calculate_total_basket_value():.2f}€')

    def calculate_total_basket_value(self) -> float:
        """
        Calcule le total des produits dans le panier d'un client.

        Cette méthode itère sur tous les produits présents dans le panier du client,
        multiplie le stock de chaque produit par son prix unitaire, et somme ces valeurs
        pour obtenir le total des produits.
        :return: float: Le total calculé des produits dans le panier du client.
        """
        return sum([i.stock * i.price_unit for i in self.client.basket.products])
