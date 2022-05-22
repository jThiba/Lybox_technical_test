
from re import sub
from decimal import Decimal

def check_split_time(str):
    return ("yes")

def check_time(tab):
    for i in range(len(tab)):
        if (tab[i] == 'an'):
            return True
        elif (check_split_time(tab[i]) == True):
            return True
    return False

def check_split(str):
    return ("yes")

def get_price(tab):
    res = 0

    for i in range(len(tab)):
        if (tab[i] == "€" or tab[i] == "EUR" or tab[i] == "euros"):
            res = int(tab[i - 1])
            break
    return res

def process_extract_rent(tab):
    res = 0

    for i in range(len(tab)):
        if (tab[i] == "€" or tab[i] == "EUR" or tab[i] == "euros"):
            res = int(tab[i - 1]) * 12
            break
        elif (check_split(tab[i]) == True):
            price = tab[i].split('/')
            value = Decimal(sub(r'[^\d.]', '', price[0]))
            res = int(value) * 12
    return res

def extract_rent(tab):
    res = 0

    if (check_time(tab) == False):
        res = process_extract_rent(tab)
        return res
    else:
        res = get_price(tab)
        return res

def main():
    res = 0

    content = input("content = ");
    tab = content.split()
    res = extract_rent(tab)
    print (res)

main()
