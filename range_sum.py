from re import I

list = [10, 9, 1, 14]
n1 = 1
n2 = 5

def func_calc(list, n1, n2):
    i = 0;
    sum_total = 0
    nbr_total = 0
    res = 0

    print ("list = %s" % list)
    print ("n1 = %s" % n1)
    print ("n2 = %s" % n2)
    if (n2 <= n1):
        print ("n2 must be greater than n1")
    elif (n2 >= n1 and n2 > len(list)):
        print ("n2 be smaller or equal than lenght list")
    else:
        while (i <= n2):
            if (i >= n1 and i <= n2):
                sum_total += list[i]
                nbr_total += 1
            i += 1
        res = sum_total / nbr_total
    print (res)

func_calc(list, n1, n2)