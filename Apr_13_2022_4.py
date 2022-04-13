#!/usr/bin/python3
from random import choice, sample

data = [x for x in range(1, 11)]

print(choice(data), sample(data, 5), sample(data, len(data)), sep='\t')