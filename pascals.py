# -*- coding: utf-8 -*-
#! /usr/bin/env python3

from math import factorial

# functions to generate pascals trinangle numbers


def get_value_at(row=1, col=1, acc = 1):
    '''
    a nCr b = a!/(b!*(a-b)!)
    a nCr b = get_value_at(b+1, a-b+1)
    get_value_at(a < b)  = (b+a-2) nCr (a-1)

    >>> get_value_at(5, 5)
    70
    '''
    
    row = row - 1
    for i in range(row):
        acc *= (col + i)

    return acc // factorial(row)


def grid_printer(width=1, length=1):
    '''
    >>> for x in grid_printer(5,5):
    ...     x

    [1, 1, 1, 1, 1]
    [1, 2, 3, 4, 5]
    [1, 3, 6, 10, 15]
    [1, 4, 10, 20, 35]
    [1, 5, 15, 35, 70]
    '''

    for delta_r in range(1, width+1):
        row = []
        for delta_c in range(1, length+1):
            row.append(get_value_at(delta_r, delta_c))
        yield row


def pascal_bits(number=2):
    '''
    >>> pascal_bits(5)
    [1, 5, 10]
    '''
    for i in range(number // 2):
        if not i:
            bits = [1, number]
        else:
            bits.append(get_value_at(number-i, i+2))
    return bits


def pascals_row(number=0):
    '''
    >>> pascal_row(5)
    [1, 5, 10, 10, 5, 1]
    '''
    try:
        out = pascal_bits(number)
    except UnboundLocalError:
        out = [1] * (number + 1)
    else:
        if number % 2:
            out += out[::-1]
        else:
            out += out[len(out)-2::-1]
    return out


def pascals_triangle(end=0):
    '''
    >>> for x in pascals_triangle(5):
    ...     x

    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]

    '''
    for row in range(end+1):
        yield pascals_row(row)

