import numpy as np
import matplotlib.pyplot as plt
"""
npArr1 = np.linspace(0,10,20)
npArr2 = npArr1**2
(myFigure,myAxes) = plt.subplots()
myAxes.plot(npArr1,npArr2,color="#008B8B")
myAxes.plot(npArr2,npArr1,color="#FF00FF")
"""
npArr1 = np.linspace(0,10,20)
npArr2 = npArr1**2
(newFig,newAxe) = plt.subplots()
newAxe.plot(npArr1,npArr1+2,"red",linewidth=5.0,linestyle='-.')
newAxe.plot(npArr1,npArr1+3,"blue",linewidth=5.0,linestyle=':')
newAxe.plot(npArr1,npArr1+4,"green",linewidth=5.0,linestyle='--')#(linestyle=':','-.')
newAxe.plot(npArr1,npArr1-3,"black",linewidth=5.0,linestyle='-',marker='o',markersize=8.0,markerfacecolor="yellow")

plt.show()
