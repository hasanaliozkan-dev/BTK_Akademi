import numpy as np
import matplotlib.pyplot as plt
"""
ageList = [10,20,30,40,50,60,70,80,90,75]
weightList = [20,99,80,56,99,78,70,90,80,65]
numpyAgeList = np.array(ageList)
numpyWeightList = np.array(weightList)

plt.plot(numpyAgeList,numpyWeightList,"g") #(x-axis,y-axis)
plt.title("Age vs Weight")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.show()

array = np.linspace(0,10,20)
array1 = array**3
plt.plot(array,array1,"r") #("r*-","r--")
plt.subplot(1,2,1) # bir sıra olacak,iki kolon olacak,birinciyi çiziyorum.
plt.plot(array,array1,"b")
plt.subplot(1,2,2) # bir sıra olacak,iki kolon olacak,ikinciyi çiziyorum.
plt.plot(array1,array,"y")
plt.show()

array = np.linspace(0,10,20)
array1 = array**3

myFigure = plt.figure()
figureAxes1 = myFigure.add_axes([0.1,0.1,0.7,0.7])#[startpointforx,startpointfory,width,height]
figureAxes1.plot(array,array1,"black")
figureAxes1.set_title("My Figure")
figureAxes1.set_xlabel("My figure Xlabel")
figureAxes1.set_ylabel("My figure Ylabel")
figureAxes2 = myFigure.add_axes([0.2,0.4,0.3,0.3])#[startpointforx,startpointfory,width,height]
figureAxes2.plot(array,array1,"red")
figureAxes2.set_title("My Figure")
figureAxes2.set_xlabel("My figure Xlabel")
figureAxes2.set_ylabel("My figure Ylabel")
plt.show()

(myFigure,myAxes) = plt.subplots(nrows=1,ncols=2)
np1 = np.linspace(0,100,20)
np2 = np.linspace(0,100,20)**2
for axes in myAxes:
    axes.plot(np1,np2,"red")
    axes.set_xlabel("X label")
    axes.set_ylabel("Y label")
    axes.set_title("TITLE")
plt.tight_layout()
plt.show()
"""
array = np.linspace(0,10,20)
array1 = array**3
newFigure = plt.figure(dpi=1000) #figsize=(6,6)
newAxes = newFigure.add_axes([0.2,0.2,0.7,0.7])
newAxes.plot(array,array1,label="X^3")
newAxes.plot(array,array**2,label="X^2",color="r")
newAxes.legend(loc=2)

plt.show()
#newFigure.savefig("MyFigure.pdf",dpi=1000)

d = np.arange(0.0,5.0,0.2)
plt.plot(d,d,"r--",d,d**2,"bs",d,d**3,"g^")