"""
Your job is to find the gravitational force between two spherical objects (obj1 , obj2).

input
Two arrays are give :

arr_val (value array), consists of 3 elements
1st element : mass of obj 1
2nd element : mass of obj 2
3rd element : distance between their centers
arr_unit (unit array), consists of 3 elements
1st element : unit for mass of obj 1
2nd element : unit for mass of obj 2
3rd element : unit for distance between their centers
mass units are :

kilogram (kg)
gram (g)
milligram (mg)
microgram (μg)
pound (lb)
distance units are :

meter (m)
centimeter (cm)
millimeter (mm)
micrometer (μm)
feet (ft)
Note
value of G = 6.67 x 10-11N.kg–2.m2

1ft = 0.3048m

1lb = 0.453592kg

return value must be Newton for force (obviously)

μ copy this from here to use it in your solution
"""

def solution(arr_val, arr_unit) :
    mass = {'kg': 1, 'g': 10**(-3), 'mg': 10**(-6), 'μg': 10**(-9), 'lb': 0.453592}
    distance = {'m': 1, 'cm': 10**(-2), 'mm': 10**(-3), 'μm': 10**(-6), 'ft': 0.3048}
    G = 6.67 * 10**(-11)
    m1 = arr_val[0]*mass[arr_unit[0]]
    m2 = arr_val[1]*mass[arr_unit[1]]
    r = arr_val[2]*distance[arr_unit[2]]
    return G*m1*m2 / r**2    
