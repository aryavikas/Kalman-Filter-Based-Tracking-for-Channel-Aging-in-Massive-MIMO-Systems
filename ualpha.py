#for l=6
from pylab import *
from matplotlib import rc,rcParams
import matplotlib.pyplot as plt
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
import numpy as np
x = [20,30,40,50,60,70]

datal1=[31.3937,36.5254,40.7867,44.2287,46.1697,48.3449]
datal2=[22.6504,27.5985,30.6328,33.6881,35.5862,37.8286]
datal3=[10.8439,13.0612,13.5919,15.206,16.2283,17.304]
datal4=[3.98832,4.80775,5.63223,6.48232,6.7459,7.21031]


plt.hold(True)
line1, = plt.plot(x,datal1, 'r^-', label="$f_DT_s: 0.005-0.05$", lw=3, ms=9.0)
line2, = plt.plot(x,datal2, 'mo-', label="$f_DT_s: 0.05-0.1$", lw=3, ms=9.0)
line3, = plt.plot(x,datal3, 'b*-', label="$f_DT_s: 0.1-0.2$", lw=3, ms=12.0)
line4, = plt.plot(x,datal4, 'gv-', label="$f_DT_s: 0.5-0.6$", lw=3, ms=9.0)

first_legend = plt.legend(handles=[line1,line2,line3,line4], loc='best')

plt.xlabel('Number of antennas')
plt.ylabel('Average Sum Rate [bps/Hz]')

plt.grid()
plt.show()






