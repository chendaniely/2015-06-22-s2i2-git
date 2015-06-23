#! /usr/bin/env python

"""This is a python module that converts temperatures
"""

def f_to_k(temp):
    converted = ((temp - 32) * (5 / 9.0)) + 273.15
    return converted

def k_to_c(temp):
    return temp - 273.15

def f_to_c(temp):
    temp_k = f_to_k(temp)
    result = k_to_c(temp_k)
    return result


print(f_to_k(32))
print(f_to_k(212))
print(k_to_c(273.15))
print(f_to_c(32))
