"""
Create a function called shortcut to remove all the lowercase vowels in a given string.

Examples
shortcut("codewars") # --> cdwrs
shortcut("goodbye")  # --> gdby
Don't worry about uppercase vowels.
"""

vowels = ['a', 'e', 'i', 'u', 'o']

def shortcut( s ):
    return ''.join(i for i in s if i not in vowels)