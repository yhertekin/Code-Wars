"""
Complete the function which converts a binary number (given as a string) to a decimal number.
"""
def bin_to_decimal(inp):
    return sum(int(inp[::-1][i])*2**i for i in range(len(inp)))
    #or 
    #return int(inp, 2)