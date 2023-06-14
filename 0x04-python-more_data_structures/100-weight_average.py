#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    tpl_mul_sum = 0
    sum_mul = 0
    for tpl in my_list:
        tpl_mul_sum += tpl[0] * tpl[1]
        sum_mul += tpl[1]
    return (tpl_mul_sum / sum_mul)
