#1.Create a 1D array of numbers from 0 to 9
#2. Create a 3×3 NumPy array of all Boolean value Trues
#3. Extract all odd numbers from array of 1 10
#4. Replace all odd numbers in an array of 1 10 with the value 1
#5.Convert a 1D array to a 2D array with 2 rows
#6. Create two arrays a and b, stack these two arrays vertically use the np.dot and np.sum to calculate totals

import numpy as np

OneD_array = np.arange(0,10,1)
ThreeD_array = np.ones((3, 3), dtype=bool)

OneD_arrayb = np.arange(0,11,1)
No_odd = OneD_arrayb[OneD_arrayb % 2 == 1]

OneD_arrayb2 = np.arange(0,11,1)
OneD_arrayb2[OneD_arrayb2 % 2 == 1] = -1

TwoD_array = OneD_array.reshape(2,5)

a =  np.arange(0,9,1).reshape (3,3)
b =  np.arange(0,9,1).reshape (3,3)
c = np.dot(a,b)
total_each_column = np.sum(c,0)
total_sum = np.sum (c)

                         #Extension
#1. Create the following pattern without hardcoding. Use only NumPy functions

x= np.ones(9).reshape((3, 3))
x[0] = 1
x[1] = 2
x[2] = 3
x = x.reshape(1,9)

y= np.ones(9).reshape((3, 3))
y[:,0] = 1
y[:,1] = 2
y[:,2] = 3
y= y.reshape(1,9)

z = np.append(x,y)

# 2.In two arrays a ( 1,2,3,4,5) and b ( 4,5,6,7,8,9) remove all repeating items present in array b

a1 = np.arange(1,6,1)
b1 = np.arange(4,10,1)

b2 = np.unique(b1)

#3.Get all items between 3 and 7 from a and b and sum them together
a2 = a1[(a1 > 3) & (a1 < 7)]
b2 = b1[(b1 > 3) & (b1 < 7)]

sum_a2b2 = np.sum(np.append(a2,b2))