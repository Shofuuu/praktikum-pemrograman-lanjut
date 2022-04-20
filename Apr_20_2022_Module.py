#!/usr/bin/python3

def check_taxes(tax_type):
    try:
        if tax_type.lower() == 'pribadi':
            return 0.08
        elif tax_type.lower() == 'perusahaan':
            return 0.12
        elif tax_type.lower() == 'restoran':
            return 0.05
        else:
            return 0
    except AttributeError:
        print("[check_taxes] The tax type is not valid string")
        exit(1)