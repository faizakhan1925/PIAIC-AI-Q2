# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:17:50 2020

@author: pc
"""

import numpy as np

#Numpy_Assignment_2::

#Question:1
#Convert a 1D array to a 2D array with 2 rows?
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print('1D Numpy array:')
print(arr)
# Convert 1D array to a 2D numpy array of 2 rows and 3 columns
arr_2d = np.reshape(arr, (2, 5))
print(arr_2d)
print("_________________________________________________")

#Question:2
#How to stack two arrays vertically?
x=np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
print(x)
y=np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
print(y)
array=np.vstack((x,y))
print("array:",array)
print("_________________________________________________")

#Question:3¶
#How to stack two arrays horizontally?
x=np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
print(x)
y=np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
print(y)
array=np.hstack((x,y))
print("array:",array)
print("_________________________________________________")

#Question:4
#How to convert an array of arrays into a flat 1d array?
arr = np.array([[0,1, 2], [3,4, 5],[6,7,8],[9,10,11], [12,13,14]])
print("arr=",arr)
newarr = arr.reshape(-1)
print("newarr=", newarr)
print("_________________________________________________")

#Question:5
#How to Convert higher dimension into one dimension?
arr = np.arange(15).reshape(3,5)
print(arr)
newarr = arr.reshape(-1)
print("newarr=", newarr)
print("_________________________________________________")

#Question:6
#Convert one dimension to higher dimension?
arr = np.arange(15)
print(arr)
newarr = arr.reshape(5, 3)
print("newarr=", newarr)
print("_________________________________________________")

#Question:7
#Create 5x5 an array and find the square of an array?
x = np.arange(25).reshape(5,5)
print(x)
s=np.square(x)
print("square of an array:",s)
print("_________________________________________________")

#Question:8
#Create 5x6 an array and find the mean?
x = np.arange(30).reshape(5,6)
print(x)
m=np.mean(x)
print("mean of an array:",m)
print("_________________________________________________")

#Question:9
#Find the standard deviation of the previous array in Q8?
x = np.arange(30).reshape(5,6)
print(x)
std=np.std(x, dtype=np.float64)
print("standard deviation of an array:",std)
print("_________________________________________________")

#Question:10
#Find the median of the previous array in Q8?
x = np.arange(30).reshape(5,6)
print(x)
median=np.median(x)
print("median of an array:",median)
print("_________________________________________________")

#Question:11¶
#Find the transpose of the previous array in Q8?
x = np.arange(30).reshape(5,6)
print(x)
t=x.transpose()
print("transpose of an array:",t)
print("_________________________________________________")

#Question:12
#Create a 4x4 an array and find the sum of diagonal elements?
x = np.arange(16).reshape(4,4)
print(x)
# calculating the Trace of a matrix 
trace = np.trace(x) 
print("\nTrace of given matrix:",trace)
print("_________________________________________________")

#Question:13
#Find the determinant of the previous array in Q12?
x = np.arange(16).reshape(4,4)
print(x)
print ("determinant of the array:",np.linalg.det(x))
print("_________________________________________________")

#Question:14
#Find the 5th and 95th percentile of an array?
# 2D array 
arr = [[14, 17, 12, 33, 44],  
       [15, 6, 27, 8, 19], 
       [23, 2, 54, 1, 4,]] 
print("arr:", arr) 
#axis = 0 means along the column and axis = 1 means working along the row.    
# Percentile of the flattened array 
print("\n5th Percentile of arr, axis = None : ", 
      np.percentile(arr, 5)) 
print("95th Percentile of arr, axis = None : ", 
      np.percentile(arr, 95))   
# Percentile along the axis = 0 
print("\n5th Percentile of arr, axis = 0 : ", 
      np.percentile(arr, 5, axis =0)) 
print("95th Percentile of arr, axis = 0 : ", 
      np.percentile(arr, 95, axis =0)) 
print("_________________________________________________")

#Question:15
#How to find if a given array has any null values?
print("Original array:")
nums = np.random.randint(0,3,(4,10))
print(nums)
print("\nIs NaN: \n", np.isnan(nums)) 
print("\nTest whether the said array has null values or not:")
n=np.all(np.isnan(nums))
print(n)
print("_________________________________________________")























