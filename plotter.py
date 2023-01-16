import math
import matplotlib.pyplot as plt
from numpy import arange
import pandas as pd
# parse logfile

df_4 = pd.read_csv('./buck_data/NewFile1.csv')
df_6 = pd.read_csv('./buck_data/NewFile26.csv')
df_8 = pd.read_csv('./buck_data/NewFile28.csv')
df_9 = pd.read_csv('./buck_data/NewFile297.csv')

df_list = [df_4, df_6, df_8, df_9]
title_list = ['4V', '6V', '8V', '9.69V']

for i,df in enumerate(df_list):

    # grab timesteps, start time
    time_increment = df.loc[0, 'Increment']
    time_start = df.loc[0, 'Start']
    df = df.drop(0, axis = 0)
    # remove extraneous columns and rows
    df = df.drop('Start', axis = 1)
    df = df.drop('Increment', axis = 1)
    df = df.drop(df.columns[-1], axis = 1) # last col, unnamed

    df['X'] = time_increment * df['X'].astype(float) # x is now time
    df['CH1'] = df['CH1'].astype(float)
    df['CH2'] = df['CH2'].astype(float)


    # plot CH2
    df.plot(x='X',y='CH2')
    plt.legend(loc='best')
    plt.title('Voltage across shunt resistor as a function of time, input voltage = ' + title_list[i])
    plt.xlabel('Time, (seconds)')
    plt.ylabel('Voltage across shunt resistor, (volts)')

    # plot CH1
    df.plot(x='X',y='CH1')
    plt.legend(loc='best')
    plt.title('NMOS Drain Voltage as a function of time, input voltage = ' + title_list[i])
    plt.xlabel('Time, (seconds)')
    plt.ylabel('NMOS Drain Voltage (volts)')

plt.show()
