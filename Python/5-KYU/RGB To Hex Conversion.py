"""
The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

"""
def rgb(r, g, b):
    valid = lambda x: min(255, max(x, 0))
    return ('%02x%02x%02x' % (valid(r), valid(g), valid(b))).upper()


"""
OR

def valid(num):
    if num < 0:
        return 0
    elif num > 255:
        return 255
    else: return num

def rgb(r, g, b):
    r = valid(r)
    g = valid(g)
    b = valid(b)
    return ('%02x%02x%02x' % (r, g, b)).upper()
"""