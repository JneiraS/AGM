from datetime import datetime

from src.client import Client


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

        print(f"{'Name':<20} {'Qt'}\t{'Price'}")
        for article in self.client.basket.products:
            print(f"{article.name:<20} {article.stock}\t"
                  f"{article.stock * article.price_unit:.2f} €")
        print(f'\t-------------------------')
        print(f'{'TOTAL':>20}:   {sum([i.stock * i.price_unit for i in self.client.basket.products]):.2f}€')
