from pylab import *
from matplotlib import rc,rcParams
import matplotlib.pyplot as plt
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
import numpy as np
x = [20,30,40,50,60,70]

datal1=[19.0376,22.5148,25.0996,26.7576,28.6828,31.1158]
datal3=[25.4709,29.7743,33.2772,35.7501,39.031,41.3629]
datal9=[35.3015,41.5615,46.1395,49.108,51.7216,53.1989]
datal15=[42.598,48.7627,52.8551,56.6696,57.6845,60.318]


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




