# power_electronics.py
import matplotlib.pyplot as plt
from numpy import arange
import pandas as pd


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
plotter(n_, raw, info)

