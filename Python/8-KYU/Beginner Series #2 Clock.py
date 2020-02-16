"""
Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to milliseconds.

Example:
past(0, 1, 1) == 61000
Input constraints: 0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59
"""
def past(h, m, s):
    return (h * 36 * 10**5) + (m * 60 * 10**3) + (s * 10**3)
 

# 1 s -> 1000 ms == 10**3
# 1 h -> 60 m -> 3600 s -> 3600*1000 ms -> 36*10**5
