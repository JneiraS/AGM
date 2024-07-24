#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.client import Client
from src.stock import Stock
from src.render import ShopTextRenderer


def main():

    shop = ShopTextRenderer()
    shop.display()


if __name__ == '__main__':
    main()
