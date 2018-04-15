from pylab import *
from matplotlib import rc,rcParams
import matplotlib.pyplot as plt
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
import numpy as np
x = [20,30,40,50,60,70]

datal1=[5.48152,5.65596,6.03219,6.03884,5.6669,5.81501]
datal3=[6.38748,6.98016,6.98371,7.02234,6.7842,6.70984]
datal9=[7.34637,8.30115,8.87877,9.15395,9.22455,9.08797]
datal15=[9.20899,11.81415,13.08415,14.226,14.2052,14.3056]



plt.hold(True)
line1, = plt.plot(x,datal1, 'r^-', label="$m = 1$", lw=3, ms=9.0)
line2, = plt.plot(x,datal3, 'mo-', label="$m = 3$", lw=3, ms=9.0)
line3, = plt.plot(x,datal9, 'g*-', label="$m = 9$", lw=3, ms=12.0)
line4, = plt.plot(x,datal15, 'bv-', label="$m = 15$", lw=3, ms=9.0)
first_legend = plt.legend(handles=[line1,line2,line3,line4], loc='best')

plt.xlabel('Number of antennas')
plt.ylabel('Average Sum Rate [bps/Hz]')

plt.grid()
plt.show()




