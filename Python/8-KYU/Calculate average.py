"""
Write function avg which calculates average of numbers in given list.

Python:

Due to rounding issues please do not use statistics.mean or such.
If the array is empty, return 0.
"""
def find_average(l):    
    return sum(l) / len(l) if l else 0