import unittest

from src.client import *
from src.products import *


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client('John', 'Doe')
        self.shopping_cart = ShoppingCart(self.client, [])
        self.orange = Product('orange', 3.0, 'pièce', 0.5)

    def test_client_class(self):
        self.assertIsInstance(self.client, Client)

    def test_shoppingcart_class(self):
        self.assertIsInstance(self.shopping_cart, ShoppingCart)

    def test_add_method(self):
        self.shopping_cart.add(self.orange)

        test_product_name = self.shopping_cart.products[0].name
        test_product_stock = self.shopping_cart.products[0].stock

        self.assertEqual(test_product_name, 'orange')
        self.assertEqual(test_product_stock, 3.0)

    def test_remove_method(self):
        self.shopping_cart.add(self.orange)
        self.shopping_cart.remove(self.orange)

        self.assertEqual(self.shopping_cart.products, [])


if __name__ == '__main__':
    unittest.main()
