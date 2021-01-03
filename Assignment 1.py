# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 19:05:30 2020

@author: pc
"""

#Assignment For Numpy¶
#Difficulty Level Beginner

#1. Import the numpy package under the name np
import numpy as np

#2. Create a null vector of size 10
a= np.zeros(10)
print ("null vector of size 10 is a =", a)
print("_________________________________________________")

#3. Create a vector with values ranging from 10 to 49
values_ranging = np.arange(10,50)
print ("vector with values ranging from 10 to 49 are:", values_ranging)
print("_________________________________________________")

#Find the shape of previous array in question 3
print("shape of previous array in question 3 is:",values_ranging.shape)
print("_________________________________________________")

#Print the type of the previous array in question 3
print("type of the previous array in question 3 is:", values_ranging.dtype)
print("_________________________________________________")

#Print the numpy version and the configuration
print("Numpy Version")
print(np.__version__)
print("_________________________________________________")
print("Configuration")
print(np.show_config())
print("_________________________________________________")

#Print the dimension of the array in question 3
print("the dimension of the array in question 3 is:",values_ranging.ndim)
print("_________________________________________________")

#Create a boolean array with all the True values
# Array for random sampling
sample_arr = [True]
# Create a numpy array with random True or False of size 10
bool_arr = np.random.choice(sample_arr, size=10)
print('Numpy Array: ')
print(bool_arr)
print("_________________________________________________")

#Create a two dimensional array
Two_array = np.zeros((4,5))
# 4 rows, 5 columns
print("2-d array:", Two_array)
print("_________________________________________________")

#Create a three dimensional array
Three_array = np.zeros((3,3,4))
#3 Sets, 3 Rows per Set, 4 Columns
print("3-d array:", Three_array)
print("_________________________________________________")
print("**************************************************")

#Difficulty Level Easy

# 1.Reverse a vector (first element becomes last)
x = np.arange(1, 20)
print("Original array:", x)
x = x[::-1]
print("Reverse array:", x)
print("_________________________________________________")

# 2.Create a null vector of size 10 but the fifth value which is 1
a=np.zeros(10)
print("original null vector:",a)
a[5]=1
print("5th value changed in a null vector:",a)
print("_________________________________________________")

# 3.Create a 3x3 identity matrix
array_2D=np.identity(3)
print('3x3 matrix:', array_2D)
print("_________________________________________________")

# arr = np.array([1, 2, 3, 4, 5])
#Convert the data type of the given array from int to float
arr = np.array([1, 2, 3, 4, 5])
print("original array:",arr)
print("original array data type:",arr.dtype) 
# change the dtype to 'float64' 
arr = arr.astype('float64') 
# Print the array after changing 
# the data type 
print("converted array:",arr)
# Also print the data type 
print("converted array data type:", arr.dtype) 
print("_________________________________________________")

#arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])  
#arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
#Multiply arr1 with arr2
arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])
print("arr1 =",arr1)  
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print("arr2 =",arr2) 
out_arr = np.multiply(arr1, arr2)  
print ("Resultant output array: ", out_arr)  
print("_________________________________________________")

#arr1 = np.array([[1., 2., 3.],[4., 5., 6.]]) 
#arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
#Make an array by comparing both the arrays provided above
arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])
print("arr1 =",arr1)  
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print("arr2 =",arr2) 
comparison = arr1 == arr2 
equal_arrays = comparison.all() 
print("comparison result is:", equal_arrays) 
print("_________________________________________________")

#Extract all odd numbers from arr with values(0-9)
a = np.array([1,2,3,4,5,6,6,7,8,9])
odd=a[a % 2 == 1]
print("odd number from array are:",odd)
print("_________________________________________________")

#Replace all odd numbers to -1 from previous array
a = np.array([1,2,3,4,5,6,6,7,8,9])
odd = (a%2 == 1)
a[odd] = -1
print("odd number replaced with -1 array are:",a)
print("_________________________________________________")

#arr = np.arange(10)
#Replace the values of indexes 5,6,7 and 8 to 12
arr = np.arange(10)
print("original array",arr)
arr[5:8]=12
print("Changed array",arr)
print("_________________________________________________")

#Create a 2d array with 1 on the border and 0 inside
x = np.ones((5,5))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array:")
x[1:-1,1:-1] = 0
print(x)
print("_________________________________________________")

#Difficulty Level Medium
#arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#Replace the value 5 to 12
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("original array:", arr2d)
arr2d[1][1]=12
print("modified array:",arr2d)
print("_________________________________________________")

#arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#Convert all the values of 1st array to 64
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("original array:", arr3d)
arr3d[0] = 64
print("modified array:",arr3d)
print("_________________________________________________")

#Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it
arr = np.arange(9),
arr= np.reshape(arr,(3,3))
print("original array:", arr)
print("sliced 1st 1-D array:", arr[0, 0:])
print("_________________________________________________")

#Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it
arr = np.arange(9),
arr= np.reshape(arr,(3,3))
print("original array:", arr)
print("sliced 2nd value from 2nd 1-D array:", arr[1, 1:2])
print("_________________________________________________")

#Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows
arr = np.arange(9),
arr= np.reshape(arr,(3,3))
print("original array:", arr)
print("sliced the third column but only the first two rows of array:", arr[0:2,2])
print("_________________________________________________")

#Create a 10x10 array with random values and find the minimum and maximum values
x = np.random.random((10,10))
print("Original Array:")
print(x) 
xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax)
print("_________________________________________________")

#Find the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
print("a:",a) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
print("b:",b)
# Common values between two arrays 
print("Common values between a and b:",np.intersect1d(a, b)) 
print("_________________________________________________")

#Find the positions where elements of a and b match
a = np.array([1,2,3,2,3,4,3,4,5,6])
print("a:",a) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
print("b:",b)
print("the positions where elements of a and b match in array a:",np.searchsorted(a, np.intersect1d(a, b)))
print("_________________________________________________")

#Find all the values from array data where the values from array names are not equal to Will
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print("names:", names) 
data = np.random.randn(7, 4)
print("data:", data)
x = np.where(names != 'Will')
print(x)
n=(names != 'Will')
print(n)
print("_________________________________________________")

#Find all the values from array data where the values from array names are not equal to Will and Joe
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print("names:", names) 
data = np.random.randn(7, 4)
print("data:", data)
mask = (names == 'Bob')
# mask = (names != 'Will') | (names != 'Joe')
print(mask)
print("_________________________________________________")


#Difficulty Level Hard

#Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15
arr = np.arange(1,16).reshape(5,3)
print(arr)
print("_________________________________________________")

#Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.
arr = np.arange(16).reshape(2,2,4)
print(arr)
print("_________________________________________________")

#Swap axes of the array you created in Question 32
arr = np.arange(16).reshape(2,2,4)
print("array:",arr)
print("axes swaped of array:",arr.swapaxes(1, 2))
print("_________________________________________________")

#Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0
arr = np.arange(10)
print("arr:",arr)
x=np.sqrt(arr)
print("square root of every element in the array:", x)
print("Replace all elements of the said array with 0 which are less than 0.5")
x[x < 0.5] = 0
print(x)
print("_________________________________________________")

#Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays
a=np.random.randint(1,12,6)
print(a)
b=np.random.randint(1,12,6)
print(b)
m=np.maximum(a,b)
print("maximum values between each element of the two arrays:",m)
print("_________________________________________________")

#Find the unique names and sort them out!
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(names)
n=np.unique(names)
print(n)
print("_________________________________________________")

#From array a remove all items present in array b
a = np.array([1,2,3,4,5]) 
print(a)
b = np.array([5,6,7,8,9])
print(b)
result = np.setdiff1d(a, b)
print(result)
print("_________________________________________________")

#Following is the input NumPy array delete column two and insert following new column in its place
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print("original array:",sampleArray)
print("Array after deleting column 2 on axis 1")
sampleArray = np.delete(sampleArray , 1, axis = 1) 
print (sampleArray)
newColumn = np.array([[10,10,10]])
print("new Column:",newColumn)
print("Array after inserting column 2")
sampleArray = np.insert(sampleArray , 1, newColumn, axis = 1) 
print (sampleArray)
print("_________________________________________________")

#Find the dot product of the above two matrix
x = np.array([[1., 2., 3.], [4., 5., 6.]]) 
print("x=",x)
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print("y=",y)
d=np.dot(a, b)
print("dot product of x and y=",d)
print("_________________________________________________")

#Generate a matrix of 20 random values and find its cumulative sum
A = np.random.randint(20, size=(4,5))
print("matrix A:",A)
CS = np.cumsum(A)
print("cumulative sum of matrix A:",CS)
print("_________________________________________________")

print("______________________________THe END__________________")












