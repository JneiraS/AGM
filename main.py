#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.client import Client


def main():
    # Création d'un clent
    client_one = Client('Dupont', 'Patrick')
    print(client_one)


if __name__ == '__main__':
    main()
