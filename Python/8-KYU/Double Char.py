"""
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "
Good Luck!
"""
def double_char(s):
    a = ''
    for item in s:
        a += item*2
    return a