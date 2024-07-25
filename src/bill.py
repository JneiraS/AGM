import client
class Facturette: # Une ligne de bill
    name: str
    quantity: float
    unit_price: float
    total_price: float
class Bill:
    dailyBill = []
    def __init__(self, my_client: client.Client):
        ligne: Facturette
        facture=[]
        amount = 0.0
        for item in my_client.basket:
            # On calcule le prix
            total_price = item.quantity * item.unit_price
            ligne.total_price = total_price
            ligne.name = item.name
            ligne.quantity = item.quantity
            ligne.unit_price = item.unit_price
            self.amount += total_price
            facture += [ligne]
        Bill.dailyBill += [self]

    @classmethod
    def reset(cls):
        cls.dailyBill=[]
        :

    def impression(self):
        print(f"Facture de {my_client.name} {my_client.surname}")
        print("Produit  |Quantité   |Prix unitaire  | Prix")
        print("-------------------------------------------")
        for facturette in ligne:
            print(f"{self.facturette.name}   |{self.facturette.quantity}  |{self.facturette.unit_price}  |{self.facturette.total}")
            print(f"Total : {amount}")
