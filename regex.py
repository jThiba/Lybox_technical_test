
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
    return ("yes")

def process_extract_rent(tab):
    return ("yes")

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
