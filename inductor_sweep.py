import math
import numpy as np
import pandas as pd
from pint import UnitRegistry

ur = UnitRegistry()
''' CONSTRAINTS
Inductance: 20 uH +0%/-20%
Peak current: 10 A, DCM at Dmax = 50%
Maximal peak flux density in ferrite core: 200 mT
Maximal RMS current density in copper wire: 10 Arms/mm^2 (note: "rms" not "peak")
'''
target_L    = ur(".000020 Wb/A")
low_target_L=target_L - target_L*.2
b_max       = ur(".200 T")
Ipk         = ur("10 A")
max_Irms_density = ur("10 A/(mm)^2")

# other constants
## Free space permeance
mew_0 = 1.257 *10**(-6)*ur("Wb/A / m")
Ae_min = 59.1*ur("mm^2")
flux_max = (b_max*Ae_min).to("Wb")
work  =  ((1/2)*target_L*(Ipk**2)).to("J")
upper = ((flux_max**2)/(2*work)).to("Wb/A")
winding_area = 1*6*ur("mm^2")
k_factor = .6

ca = (62.6 / math.pi)*ur("mm^2")
radius = ca**.5
circle = radius**2 * math.pi


print(f"Desired L: {target_L}")
print(f"L -20%: {low_target_L}")
print(f"Peak Flux Density: {b_max}"       )
print(f"Peak Current: {Ipk}"        )
print(f"Free Space Permeability: {mew_0}")
print(f"Min Area: {Ae_min}")
print(f"Max Flux:{flux_max}")
print(f"Energy in Inductor: {work}")
print(f"Pe Upper-limit: {upper}")

data = { 'L':[],
        'lg':[],
        'N':[], 
        'Pe':[],
        'Work':[],
        'upperlimit':[],
        'Ae':[]}

def total_effective_area(length):
    w_ea = (2*(7+length)*(10.25+length))-((7-length)*(((9-length)**2)- \
            ((7-length)**2))**.5) - ((9-length)**2) * np.arcsin((7+length)/(9-length))
    total = w_ea*2*ur("mm^2") + circle
    return total


def perm(length, area,):
    out = area*mew_0.to("Wb/ A /mm") / (length)
    return out

# sweeping through windings    #
for n in range(5,20): 
    #sweeping through airgaps
    for l in np.linspace(.002*25.4,.012*25.4,100)*ur("mm"):
        
        Ae = total_effective_area(l.magnitude).to("mm^2") 
        Pe = perm((l),Ae)
        L = ((n**2)*Pe).to("Wb/A")
        if L > low_target_L and L < target_L and Pe < upper:
            print(f"Perm: {Pe}, L {L}, N {n} ")




