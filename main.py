#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.render import ShopTextRenderer


def main():

    shop = ShopTextRenderer()

    while True:
        shop.display()



if __name__ == '__main__':
    main()
