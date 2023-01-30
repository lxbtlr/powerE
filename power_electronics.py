# power_electronics.py
import matplotlib.pyplot as plt
from numpy import arange
import pandas as pd
import math
# parse log files and plot

def plotter(names, data, information ):
    # names - labels of every line to plot
    # data  - list of csv data path's
    # information  - labels for plot, broken by channel
    # i.e.      [(channels), (titles), (y-axis)]
    figs = []
    for i, d in enumerate(data):
        # get time information from data
        t_inc   = d.loc[0,'Increment']
        t_start = d.loc[0,'Start']
        d = d.drop(0,axis = 0)

        # remove extra col & row

        d = d.drop('Start', axis=1)
        d = d.drop('Increment', axis=1)
        d = d.drop(d.columns[-1], axis = 1)

        # making X axis time
        d['X'] = t_inc *d['X'].astype(float)
         
        # plot each channel 
        t_fig, axs = plt.subplots(len(information[0]))
        figs.append(t_fig)
        # figs[i].suptitle(names[i])
        for g,c in enumerate(information[0]):
       
            d[c] = d[c].astype(float)
            axs[g].set_title(information[1][g] + names[i]) 
            axs[g].set_ylabel(information[2][g])
            d.plot(ax=axs[g],x='X',y=c)
            plt.legend(loc='best')
            # plt.title(information[1][g] + names[i])
            plt.xlabel('Time, (s)')
            # plt.ylabel(information[0][g])

    plt.show()
    return True

#########################
# testing with lb3 data #
#########################

# setting information 

# plot name
p1 = "NMOS Drain Voltage as a function of time, input voltage = "
p2 = "Voltage across shunt resitor as a function of time, input voltage = "
info = [('CH1','CH2'),
        (p1, p2),
        ('NMOS Drain Voltage (V)', 'Voltage across shunt resistor (V)')]
# data path (s) 
raw =  [pd.read_csv('./data/NewFile1.csv'),
        pd.read_csv('./data/NewFile26.csv'),
        pd.read_csv('./data/NewFile28.csv'),
        pd.read_csv('./data/NewFile297.csv')]
# trial name
n_  =  ['4V', '6V', '8V', '9.69V']

# call function 
# plotter(n_, raw, info)


def ccm_duty_cycle(s_period,a_period):
    return a_period/s_period

def voltage_converation_factor(v_out, v_in):
    return v_out / v_in

def ccm_ripple(V, L, s_period, v_con_fac):
    
    # inductor ripple current in CCM operation

    i_out = .5 * (1-v_con_fac)*set_title*(V/L)

    return i_out


def ccm_peak_current(V, R, L, s_period, v_con_fac):
    
    # peak inductor current

    ipk_out = (V/R) +  .5 * (1-v_con_fac) * s_period * (V/L)

    return ipk_out

def solve_k(R, L, s_period):
    k = 2/s_period * L/R
    return k

def dcm_duty_cycle(K, v_con_fac):

    # also written as sqrt(alpha)*M = sqrt(aplha)*DC_ccm

    duty_cycle = math.sqrt(k) * math.sqrt(1/(1-v_con_fac)) * v_con_fac 

    return duty_cycle

def dcm_peak_current(K, v_con_fac):
    ipk_out = math.sqrt(K)*math.sqrt(1-v_con_fac) * v_con_fac
    return ipk_out

def k_crit(v_con_fac):

    return 1-v_con_fac

def L_crit(R, s_period, v_con_fac)
    # if L < L_crit, power converter will enter DCM

    lcrit_out = (1-v_con_fac) * R * s_period

    return lcrit_out

def alpha(L, L_crit):

    # also equal to K * (1 / 1-M)
    return L/L_crit
 

