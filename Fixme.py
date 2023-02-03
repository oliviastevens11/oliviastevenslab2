#!/usr/bin/python3


def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    evens = []
    for i in range(0, n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
