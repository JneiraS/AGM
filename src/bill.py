import client
class Bill
    dailyBill=[]
    def __init__(self,client: client.Client):
        amount= 0.0
        print(f"Facture de {client.prenom} {client.nom}")
        print("Produit  |Quantité    |Prix unitaire  |Prix total")
        print("-------------------------------------------------")
        for item in client.basket:
            # On calcule le prix et on déduit du stock
            total_price=item.quantity*item.unit_price
            print(f"{item.name}   |{item.quantity}  |{item.unit_price}  |total_price")
            amount += total_price
        print(f"Total : {amount}")