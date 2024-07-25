#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.render import ShopTextRenderer
from src.stock import Stock


def main():

    shop = ShopTextRenderer()
    stock = Stock().generation()

    while True:
        shop.manage_customer_transaction(stock)


if __name__ == '__main__':
    main()
