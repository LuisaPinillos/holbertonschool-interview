#!/usr/bin/python3
'''
Method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
Returns an integer. If n is impossible to achieve, return 0.
'''


def minOperations(n):

    if type(n) is not int or n < 2:
        return 0

    num_op = 0

    for i in range(2, n):
        while n % i == 0 and n / i != 0:
            num_op += i
            n /= i
    return num_op
