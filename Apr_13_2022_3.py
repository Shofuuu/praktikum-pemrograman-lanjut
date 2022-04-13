#!/usr/bin/python3
from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2*log(2)))
print(pow(e, e) == exp(0))