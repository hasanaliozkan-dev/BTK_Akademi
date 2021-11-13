import numpy as np
import time as tm
#Python list
py_list = [1,2,3,4,5,6,7,8,9]
#print(type(py_list))
#numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])
#print(type(np_array))
py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)#(row,column)
#print(py_multi)
#print(np_multi)
#print(np_array.ndim)
#print(np_multi.ndim)
#print(np_array.shape)
#print(np_multi.shape)
#print(np_array.dtype)
#print(np_multi.dtype)
np_arange_array = np.arange(1,10)
np_arange_array = np.arange(10,100,3)
np_zeros = np.zeros(10)
np_ones = np.ones(10)
np_linspace = np.linspace(0,100,5)
np_linspace = np.linspace(0,100) #default value is 50.
np_linspace = np.linspace(0,100,25,endpoint=False) # endpoint is exclusive
np_random = np.random.randint(0,9)
np_random_intarr= np.random.randint(0,10,4)
np_random_0to1 = np.random.rand(5)
np_random_n = np.random.randn(5)
np_arr = np.arange(50)
np_matrix = np_arr.reshape(5,10)

#playing with random numbers array
rndNumbers = np.random.randint(0,100,10)
max = rndNumbers.max()
min = rndNumbers.min()
mean = rndNumbers.mean()
median = np.median(rndNumbers)
standart = rndNumbers.std()
indOfMax = rndNumbers.argmax()
indOfMin = rndNumbers.argmin()
#print("Random Array = {0}".format(rndNumbers))
#print("Max Value = {0}\nMin Value {1}\nMean {2}\nIndex Max {3}\nIndex Min {4}".format(max,min,mean,indOfMax,indOfMin))


#numpy operatiions
numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)
#print(numbers1)
#print(numbers2)

sum = numbers1 + numbers2
difference = abs(numbers1-numbers2)
plusTen = numbers1 + 10
minusTwenty = numbers2-20
product = numbers1*numbers2
divided = numbers1 / numbers2
sin = np.sin(numbers1)
cos = np.cos(numbers1)
square = np.sqrt(numbers1)
logarithm = np.log(numbers1)
#print("Sum {0}\nDifference {1}\nPlusTen {2}\nMinusTwenty {3}\nProduct {4}\nDivided {5}\nSinus {6}\nCosinus {7}\nSquare {8}\nLogarithm {9}".
      #format(sum,difference,plusTen,minusTwenty,product,divided,sin,cos,square,logarithm))
