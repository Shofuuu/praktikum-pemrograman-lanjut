#!/usr/bin/python3
import Apr_13_2022_Module as m
from random import randint as ri

data = [ri(x-1, x) for x in range(1, 11)]

print(data)
print(m.mean(data), m.median(data), m.mode(data), sep='\t')