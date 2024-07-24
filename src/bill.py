import client


class Bill:
    dailyBill = []

    def __init__(self, my_client: client.Client):
        amount = 0.0
        self.ligne = 0
        for item in my_client.basket:
            # On calcule le prix
            total_price = item.quantity*item.unit_price
            self.total[self.ligne] = total_price
            self.name[self.ligne] = item.name
            self.quantity[self.ligne] = item.quantity
            self.item.unit_price[self.ligne] = item.unit_price
            self.amount += total_price
            self.ligne += 1

        super.dailyBill += [self]

    def impression(self):
        print("Produit  |Quantité   |Prix unitaire  | Prix")
        print("-------------------------------------------")
        for i in range(self.ligne):
            print(f"{self.name[i]}   |{self.quantity[i]}  |{self.unit_price[i]}  |{self.total[i]}")
            print(f"Total : {amount}")
