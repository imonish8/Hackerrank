# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

# Create an OrderedDict to store item names and their net prices
ordered_dictionary = OrderedDict()

# Read the number of items
n = int(input())

# Process each item
for _ in range(n):
    item, space, price = input().rpartition(' ')
    price = int(price)
    if item in ordered_dictionary:
        ordered_dictionary[item] += price
    else:
        ordered_dictionary[item] = price

# Print the items and their net prices in order of their first occurrence
for item, net_price in ordered_dictionary.items():
    print(item, net_price)


# TRAP HERE IS TO UPDATE THE ORDERED DICTIONARY WITH NET PRICE.

