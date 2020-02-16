"""
Write a function that rearranges an integer into its largest possible value.

super_size(123456) # 654321
super_size(105)    # 510
super_size(12)     # 21
If the argument passed through is single digit or is already the maximum possible integer, your function should simply return it.
"""

def super_size(n):
    l = [int(i) for i in str(n)]
    s = ""
    while l:
        s += str(max(l))
        l.remove(max(l))
        
    return int(s)

# or

def s_size(n):
    return int(''.join(sorted(str(n), reverse = True)))