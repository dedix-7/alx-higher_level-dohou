#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    A function that returns the weighted average
    of all integers tuple (<score>, <weight>)

    Args:
        my_list (list, optional): A list. Defaults to [].
    """
    if not my_list:
        return 0
    else:
        product = 0
        total_sum = 0
        for i in my_list:
            product += i[0] * i[1]
            total_sum += i[1]
        weighted_mean = product / total_sum
    return (weighted_mean)
