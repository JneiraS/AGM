import client


class Bill:
    dailyBill = []

    def __init__(self, my_client: client.Client):
        amount = 0.0
        print(f"Facture de {my_client.surname} {my_client.name}")
        print("Produit  |Quantité    |Prix unitaire  |Prix total")
        print("-------------------------------------------------")
        for item in my_client.basket:
            # On calcule le prix et on déduit du stock
            total_price = item.quantity*item.unit_price
            print(f"{item.name}   |{item.quantity}  |{item.unit_price}  |total_price")
            amount += total_price
        print(f"Total : {amount}")
        super.dailyBill += [self]
