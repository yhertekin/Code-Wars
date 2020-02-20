"""
Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.
"""

import re

def is_digit(n):
    return bool(re.match("\d\Z", n))
    
#     or
    
#    return bool(re.match(r'^[0-9]$', n))
    
#     or
#     try:
#         a = int(n)
#         return True
#     except:
#         return False