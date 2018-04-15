import matplotlib.pyplot as plt
import matplotlib.patches as  mpatches
x = [20,30,40,50,60,70]

datarate_11 = [45.7511,49.3951,51.8119,54.0416,55.4539,56.7973]
datarate_12 = [28.396,30.2474,31.664,32.4024,33.0093,33.2947 ]
#datarate_13 = [ 22.7833,24.6208,26.717,26.8829,27.1649,27.5991]
datarate_13 = [22.7833,24.6208,25.621,26.249,26.543,27.5991 ] 

datarate_21 = [52.6282,56.627,59.53,61.2555,62.69,64.2975] 
datarate_22 = [28.8175,30.4493,31.7506,33.081,34.2482,34.5522]
#datarate_23 = [23.2323,24.6727,25.739,26.3349,26.7843,27.6355]
datarate_23 = [23.2323,24.6727,25.739,26.3349,26.7843,27.6355]

datarate_31 = [56.3715,60.2531,62.7415,65.126,66.4467,67.3696]
datarate_32 = [31.2901,34.3059,35.7296,36.8561,37.8746,38.67]
#datarate_33 = [23.4164,24.6758,25.9111,26.7256,26.948,27.865]
datarate_33 = [23.4164,24.6758,25.9111,26.7256,26.948,27.865]


plt.hold(True)
colour1, = plt.plot(x,datarate_11, 'b', label="$f_DT_s: 0.05-0.05$")
plt.plot(x,datarate_11, 'b^-', x, datarate_21, 'bo-',x, datarate_31, 'b.-')

colour2, = plt.plot(x,datarate_12, 'g', label="dfdsf")
plt.plot(x,datarate_12, 'g^-', x, datarate_22, 'go-',x, datarate_32, 'g.-')

colour3, = plt.plot(x,datarate_13, 'r', label="dfdsf")
line1, = plt.plot(x,datarate_13, 'r^-', label="L = 3")
line2, = plt.plot(x,datarate_23, 'ro-', label="L = 9")
line3, = plt.plot(x,datarate_33, 'r.-', label="L = 15")


first_legend = plt.legend(handles=[line1,line2,line3], loc=7)
second_legend = plt.legend(handles=[colour1,colour2], loc=10)
plt.gca().add_artist(first_legend)




plt.xlabel('Number of antennas ->')
plt.ylabel('Average Sum Rate [bps / Hz] ->')


blue_patch = mpatches.Patch(color= 'blue',label='fDTs= 0.005-0.05')
#plt.legend(handles=[blue_patch])

green_patch = mpatches.Patch(color= 'green',label='fDTs= 0.1-0.3')
#plt.legend(handles=[green_patch])

red_patch = mpatches.Patch(color= 'red',label='fDTs= 0.6-0.9')
#plt.legend(handles=[blue_patch,green_patch,red_patch])
plt.grid()
plt.show()
