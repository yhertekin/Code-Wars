"""
Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56

Function: ####javascript

getNumberFromString(s)
####ruby

get_number_from_string(s)
####CSharp

GetNumberFromString(string s)
"""
import re
def get_number_from_string(string):
    return int("".join([n for n in string if n.isdigit()]))
    #or
    # return int(re.sub(r'\D', '', s))