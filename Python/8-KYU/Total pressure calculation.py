"""
Given the moleculer mass of two molecules ( M1 and M2 ), their masses present ( m1 and m2 ) in a vessel of volume ( V ) at a specific temperature ( T ). Find the total pressure exerted by the molecules ( Ptotal ) .

input
Six values :

m1
m2
M1
M2
V
T
output
One value :

Ptotal
notes
Units for each of the following are given as under :

m1 = gram
m2 = gram
M1 = gram.mole-1
M2 = gram.mole-1
V = dm3
T = Celsius
Ptotal = atmpspheric pressure (atm)
Remember : Temperature is given in Celsius while SI unit is Kelvin (K)

0 Celsius = 273.15Kelvin

The gas constant (R) has value of 0.082dm3.atm.K-1.mol-1
"""
def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    temp += 273.15
    p1 = (given_mass1/molar_mass1 * 0.082 * temp) / volume
    p2 = (given_mass2/molar_mass2 * 0.082 * temp) / volume
    return p1+p2