#!/usr/bin/python

import sys


def making_change(amount, denominations):
    total = 0
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    else:
        reverse_d = denominations.copy()
        reverse_d.reverse()
        for currency in denominations:
            reverse_d.remove(currency)
            if amount >= currency:
                max_c = amount // currency + 1
                for i in range(1, max_c):
                    total += making_change(amount - currency * i, reverse_d)
    return total


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
