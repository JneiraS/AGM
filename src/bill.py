from src.client import Client
class Facturette: # Une ligne de bill
    name: str
    quantity: float
    unit_price: float
    total_price: float
class Bill:
    dailyBill = []
    def __init__(self, my_client: Client):
        ligne: Facturette = Facturette()
        facture=[]
        self.amount = 0.0
        print(len(my_client.basket.products))
        for item in my_client.basket.products:
            # On calcule le prix
            total_price = item.stock * item.price_unit
            ligne.total_price = total_price
            ligne.name = item.name
            ligne.quantity = item.stock
            ligne.unit_price = item.price_unit
            self.amount += total_price
            facture += [ligne]
        Bill.dailyBill += [self]

    @classmethod
    def reset(cls):
        cls.dailyBill=[]

    def impression(self):
        print(f"Facture de {my_client.name} {my_client.surname}")
        print("Produit  |Quantité   |Prix unitaire  | Prix")
        print("-------------------------------------------")
        for facturette in ligne:
            print(f"{self.facturette.name}   |{self.facturette.quantity}  |{self.facturette.unit_price}  |{self.facturette.total}")
            print(f"Total : {amount}")
