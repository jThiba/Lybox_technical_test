
from re import sub
from decimal import Decimal

def check_split_time(str):
    return ("yes")

def check_time(tab):
    return ("yes")

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
