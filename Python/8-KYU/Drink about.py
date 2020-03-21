"""
Kids drink toddy.
Teens drink coke.
Young adults drink beer.
Adults drink whisky.
Make a function that receive age, and return what they drink.

Rules:

Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.
Examples:

people_with_age_drink(13) == "drink toddy"
people_with_age_drink(17) == "drink coke"
people_with_age_drink(18) == "drink beer"
people_with_age_drink(20) == "drink beer"
people_with_age_drink(30) == "drink whisky"
"""
def people_with_age_drink(age):
    return { age<14: "drink toddy", 
             14<=age<18: "drink coke", 
             18<=age<21:"drink beer", 
             21<=age:"drink whisky" }[True]