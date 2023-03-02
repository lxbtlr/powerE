# Inductor calculations

import math
import numpy as np
import pandas as pd
import matplotlib as plt

# peak current
Ipk = 10
# theoretical inductance
t_inductance = 20*10**(-6)
# free space permeance
mew_0 = 1.257*10**(-6)
data = { 'L':[],
        'lg':[],
        'N1':[], 
        'N2':[], 
        'Pe':[],
        'Ae':[]}
# sweeping through airgap lengths in mm
for lg in np.linspace(.00508,.0009*25.4,10):
    # solving for side piece
    wing_effective_area = (2*(7+lg)*(10.25+lg))-((7-lg)*math.sqrt(((9-lg)**2)-((7-lg)**2))) - ((9-lg)**2) * np.arcsin((7+lg)/(9-lg))
    
    # solving for circle
    r = math.sqrt(62.6/math.pi)+lg
    circle_effective_area = (r**2)*math.pi 
    
    # two side pieces and circle make the total effective length, convert units to m^2
    effective_area = (circle_effective_area + 2*wing_effective_area)*(10**(-6)) #mm^2 -> m^2
    
    # Pe = (u_0 * Ae )/ lg
    permeance = mew_0 * (effective_area / lg)
    
    # solving for number of turns (this will need to be an int)
    ## solving using L = N^2 * Pe
    turns = math.sqrt(t_inductance/permeance)
    ## solving using N = flux_max / (Pe * i_rms), where flux max is Bmax*Amin
    turns2 = (.200*59.1*10**(-6)) / (Ipk*permeance)
    
    # making dict
    data['L'].append(math.floor(turns)**2 * permeance)
    data['lg'].append(lg)
    data['N1'].append(turns)
    data['N2'].append(turns2)
    data['Pe'].append(permeance)
    data['Ae'].append(effective_area)

df = pd.DataFrame(data)
print(df)    




