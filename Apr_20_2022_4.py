#!/usr/bin/python3

def check_usr_login(usr_in, pwd_in):
    # read user.txt file
    # user.txt contains username on first line and password on second line
    try:
        f = open("user.txt", "r")
        usr = f.readline().strip()
        pwd = f.readline().strip()
        f.close()
    except FileNotFoundError:
        print("[check_usr_login] File not found")
        exit(1)

    if usr_in == usr:
        if pwd_in == pwd: return True
        else: return False
    else: return False

def summary_price(data_list):
    total = 0
    for x in data_list:
        total += x
    return total

def any_discount(day):
    if day in [28, 29, 30, 31]:
        return 0.25
    elif day in [14, 15, 16, 17]:
        return 0.15
    else:
        return 0

def member_discount(is_member):
    if is_member:
        return 0.15
    else:
        return 0

def check_taxes(tax_type):
    try:
        if tax_type.lower() == 'pribadi':
            return 0.1
        elif tax_type.lower() == 'perusahaan':
            return 0.5
        elif tax_type.lower() == 'restoran':
            return 0.05
        else:
            return 0
    except AttributeError:
        print("[check_taxes] The tax type is not valid string")
        exit(1)

def main_program():
    list_total_price = []
    list_index = 0

    while True:
        try:
            list_total_price.append(int(input("[main_program] Price : ")))
            
            if list_total_price[list_index] < 0:
                print("[main_program] Price cannot be negative")
                list_total_price.pop()
                continue
            elif list_total_price[list_index] == 0:
                break

            list_index += 1
        except ValueError:
            print("[main_program] The price is not valid integer")
            exit(1)
    
    total_price = summary_price(list_total_price) * 1.0
    try:
        day = int(input("\n[main_program] Day : "))
    except ValueError:
        print("[main_program] The day is not valid integer")
        exit(1)
    
    old_price = total_price
    total_price = total_price * (1 - any_discount(day))
    print("[main_program] Total price : Rp.{:,}".format(total_price), end="")
    print(" (discount Rp.{:,})".format(any_discount(day) * old_price) if any_discount(day) != 0 else "")

    member = str(input("\n[main_program] Member? (Y/N) : ")).upper()
    old_price = total_price
    total_price = total_price * (1 - member_discount(True if member == 'Y' else False))
    print("[main_program] Total price : Rp.{:,}".format(total_price), end="")
    print(" (discount Rp.{:,})".format(member_discount(True if member == 'Y' else False) * old_price) if member_discount(True if member == 'Y' else False) != 0 else "")

    tax_type = str(input("\n[main_program] Tax type Pribadi(P) or Perusahaan(U): ")).upper()
    tax_type = ('pribadi' if tax_type == 'P' else ('perusahaan' if tax_type == 'U' else 'any'))

    old_price = total_price
    total_price = (total_price * check_taxes(tax_type)) + total_price
    print("[main_program] Total price : Rp.{:,}".format(total_price), end="")
    print(" (Taxes Rp.{:,})".format(check_taxes(tax_type) * old_price) if check_taxes(tax_type) != 0 else "")

    tax_type = 'restoran'
    old_price = total_price
    total_price = (total_price * check_taxes(tax_type if total_price >= 500000 else 'any')) + total_price
    print("[main_program] Final price : Rp.{:,}".format(total_price), end="")
    print(" (Taxes Rp.{:,})".format(check_taxes(tax_type) * old_price) if old_price >= 500000 else "")

    # write the total price to transaksi.txt
    f = open("transaksi.txt", "w")
    f.write("Total price : Rp.{:,}".format(total_price))
    f.close()
    print("\n[main_program] Total price written to transaksi.txt")

    another_payment = str(input("\n[main_program] Another payment? (Y/N) : ")).upper()
    if another_payment == 'N':
        exit(0)

if __name__ == "__main__":
    login_retry = 3

    while True:
        # read user login input
        usr_in = input("[main] Username: ")
        pwd_in = input("[main] Password: ")

        # check user login
        if check_usr_login(usr_in, pwd_in):
            print("[main] Login success", end="\n\n")
            main_program()
            login_retry = 3
            print("")
        else:
            if login_retry > 1:
                print("[main] Login failed", end="\n\n")
                login_retry -= 1
            else:
                break
    
    print("[main] Retry limit reached. End")
