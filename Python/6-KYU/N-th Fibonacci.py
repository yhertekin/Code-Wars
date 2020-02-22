"""
I love Fibonacci numbers in general, but I must admit I love some more than others.

I would like for you to write me a function that when given a number (n) returns the n-th number in the Fibonacci Sequence.

For example:

   nth_fib(4) == 2
Because 2 is the 4th number in the Fibonacci Sequence.

For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.
"""

def nth_fib(n):
    if n == 1: return 0
    
    fibo = [0, 1] 
    for i in range(n-2):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo[-1]
    
for i in range(1, 26):
    print(nth_fib(i))