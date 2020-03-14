"""
Define a function that removes duplicates from an array of numbers and returns it as a result.

The order of the sequence has to stay the same.
"""
from collections import OrderedDict
def distinct(seq):
    return list(OrderedDict.fromkeys(seq))