#for l=6
from pylab import *
from matplotlib import rc,rcParams
import matplotlib.pyplot as plt
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
import numpy as np
x = [20,30,40,50,60,70]

datal1=[27.291,29.7696,30.4245,30.8203,31.4594,30.7784]
datal2=[19.8425,20.7463,21.2935,22.0605,21.8369,22.1064]
datal3=[8.48886,8.80313,8.96997,8.83445,8.95471,8.65316]
datal4=[2.43109,2.93407,3.03326,3.16899,3.13087,3.24474]

plt.hold(True)
line1, = plt.plot(x,datal1, 'r^-', label="$f_DT_s: 0.005-0.05$", lw=3, ms=9.0)
line2, = plt.plot(x,datal2, 'mv-', label="$f_DT_s: 0.05-0.1$", lw=3, ms=9.0)
line3, = plt.plot(x,datal3, 'go-', label="$f_DT_s: 0.1-0.2$", lw=3, ms=9.0)
line4, = plt.plot(x,datal4, 'b*-', label="$f_DT_s: 0.5-0.6$", lw=3, ms=12.0)

first_legend = plt.legend(handles=[line1,line2,line3,line4], loc=7,bbox_to_anchor=(1.0,0.45))
#first_legend = plt.legend(handles=[line1,line2,line3,line4], loc=7)
plt.xlabel('Number of antennas')
plt.ylabel('Average Sum Rate [bps/Hz]')

plt.grid()
plt.show()






