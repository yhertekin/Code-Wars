"""
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.
"""

def well(x):
    counter = 0 
    for idea in x:
        if idea == 'good':
            counter+=1
    if 1 <= counter <= 2:
        return 'Publish!'
    elif counter > 2:
        return 'I smell a series!'
    return 'Fail!'
#or 

def well2(x):
    num_of_good = x.count('good')
    if 1 <= num_of_good <= 2:
        return 'Publish!'
    elif num_of_good > 2:
        return 'I smell a series!'
    return 'Fail!'