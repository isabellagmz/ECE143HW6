# Isabella Gomez A15305555
# ECE143 HW6

import random
from random import randint
def multinomial_sample(n,p,k=1):
    '''
    This function

    :param n: number of trials
    :param p: list of probabilities
    :param k: number of desired samples
    :return: samples from a multinomial distribution
    '''

    # check that k and n are ints
    assert type(n) == int
    assert type(k) == int

    # check p is list
    assert type(p) == list

    # check that the addition of numbers in p is 1
    probs=0
    for num in range(len(p)):
        probs = probs + p[num]
    assert probs == 1

    # check that K >= len(p) or it won't be able to be divided
    assert n >= len(p)

    multinomial = []
    number_of_divisions = len(p)

    # run experiments for n number of trials
    for trial in range(k):
        entry = []
        # if n = len(p) populate multinomial with 1
        if n == len(p):
            for i in range(len(p)):
                entry.append(1)
        # if probability is 1
        elif len(p) == 1:
            entry.append(n)
        else:
            # generate a random number between 1 and k - len(p)
            rand_int = randint(1, n - len(p) + 1)
            entry.append(rand_int)
            # find the remaining difference
            difference = n - rand_int -1

            for i in range(len(p)-1):
                # check that the numbers in list are equal to k
                if i == len(p)-2:
                    sum = 0
                    for j in range(len(entry)):
                        sum = sum + entry[j]
                    last_num = n - sum
                    entry.append(last_num)
                    break
                # check that value of k has not been reached
                if difference <= 0:
                    entry.append(1)
                    break
                # append next random number
                rand_int = randint(1, difference)
                entry.append(rand_int)
                difference = difference - rand_int
        # append entry to multinomial list
        multinomial.append(entry)

    return multinomial
