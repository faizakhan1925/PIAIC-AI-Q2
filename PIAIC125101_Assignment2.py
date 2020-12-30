# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:52:24 2020

@author: pc
"""

# Read Instructions carefully before attempting this assignment

# 1) don't rename any function name
# 2) don't rename any variable name
# 3) don't remove any #comment 
# 4) don't remove """ under triple quate values """
# 5) you have to write code where you found "write your code here"
# 6) after download rename this file with this format "PIAICCompletRollNumber_AssignmentNo.py"
#   Example piaic17896_Assignment1.py
# 7) After complete this assignment please push on your own GitHub repository.
# 8) you can submit this assignment through the google form
# 9) copy this file absolute URL then paste in the google form
#  The example above: https://github.com/EnggQasim/Batch04_to_35/blob/main/Sunday/1_30%20to%203_30/Assignments/assignment1.txt

# * Because all assignment we will be checked through software if you missed any above points 
# * then we can't assign your scores in our database.


import numpy as np
# Task no 1
def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =  np.arange(1,13).reshape((6,2))
    print("2-d array\n", x)
    return x
    """
    expected output:
    [[ 1  2]
    [ 3  4]
    [ 5  6]
    [ 7  8]
    [ 9 10]
    [11 12]]
    """
function1()
print("*************************************************************************")
# Task2
def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    
    x = np.arange(10,37,dtype=np.float64).reshape((3,3,3))     #wrtie your code here
    print("3-d array\n", x)
    return x
    """
    Expected: out put
array([[[10., 11., 12.],
        [13., 14., 15.],
        [16., 17., 18.]],
       [[19., 20., 21.],
        [22., 23., 24.],
        [25., 26., 27.]],
       [[28., 29., 30.],
        [31., 32., 33.],
        [34., 35., 36.]]])    
    """
function2()
print("*************************************************************************")
#task3
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    print("a:\n", a)
    x = a[(a%5==0) & (a%7==0)]
    #wrtie your code here
    print ("numbers from given array. those exist in 5,7 Table\n", x)
    return x
    """
    Expected Output:
     [35,  70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455,
       490, 525, 560, 595, 630, 665, 700, 735, 770, 805, 840, 875, 910,
       945, 980] 
    """
function3()
print("*************************************************************************")

#task4
def function4():
    #Swap columns 1 and 2 in the array arr.
    arr = np.arange(9).reshape(3,3)
    print("Original array:")
    print(arr)
    arr[:,[0, 1]] = arr[:,[1, 0]]
    print("\nAfter swapping arrays:")
    print(arr)
    return arr#wrtie your code here
    """
    Expected Output:
          array([[1, 0, 2],
                [4, 3, 5],
                [7, 6, 8]])
    """
function4()
print("*************************************************************************")

#task5
def function5():
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
   
    z = np.zeros(20).reshape(4,5) #wrtie your code here
    print("null Vector\n",z)
    return z
    """
    Expected Output:
          array([[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]])
    """ 
function5()
print("*************************************************************************")
#task6
def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
   
    arr = np.zeros(10) #wrtie your code here
    print("original null vector:",arr)
    arr[5]=10
    arr[8]=20
    print("5th value changed in a null vector:",arr)
    return arr
function6()
print("*************************************************************************")

#task7
def function7():
    #  Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.zeros(4, dtype=np.int64)
    print(x, "dtype",x.dtype)
    return x #write your code here

    """
    Expected Output:
          array([0, 0, 0, 0], dtype=int64)
    """ 
function7()
print("*************************************************************************")

#task8
def function8():
    # Create a new array of 2x5 uints, filled with 6.
    
   # x = np.zeros(10).reshape(2,5) #write your code here
    x = np.full((2, 5), 6)
    print(x)
    return x
"""
     Expected Output:
              array([[6, 6, 6, 6, 6],
                     [6, 6, 6, 6, 6]], dtype=uint32)
     """
function8()
print("*************************************************************************")

#task9
def function9():
    # Create an array of 2, 4, 6, 8, ..., 100.
    
    a = np.arange(2,101,2)
    print("Array of all the even integers from 2 to 100")
    print(a)# write your code here
    return a
"""
     Expected Output:
              array([  2,   4,   6,   8,  10,  12,  14,  16,  18,  20,  22,  24,  26,
                    28,  30,  32,  34,  36,  38,  40,  42,  44,  46,  48,  50,  52,
                    54,  56,  58,  60,  62,  64,  66,  68,  70,  72,  74,  76,  78,
                    80,  82,  84,  86,  88,  90,  92,  94,  96,  98, 100])
     """
function9()
print("*************************************************************************")

#task10
def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt = arr - brr[:,None]# write your code here 
    print(subt)
    return subt
"""
     Expected Output:
               array([[2 2 2]
                      [2 2 2]
                      [2 2 2]])
     """ 
function10()
print("*************************************************************************")

#task11
def function11():
    # Replace all odd numbers in arr with -1 without changing arr.
    
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ans = (arr%2 == 1)
    arr[ans] = -1 #write your code here 
    print(arr)
    return ans
"""
     Expected Output:
              array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
     """
function11()
print("*************************************************************************")

#task12
def function12():
    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking concept 
    arr = np.array([1,2,3])
    ans1=np.stack((arr, arr, arr),axis=1)
    print(ans1)
    ans = np.hstack((arr, arr, arr))
    print(ans)#write your code here 
    ans= np.concatenate((ans1, ans), axis=None)
    print(ans)
    return ans
"""
     Expected Output:
              array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
     """ 
function12()
print("*************************************************************************")

#task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    #ans = np.where((arr > 5) & (arr<10))
    ans = arr[(arr>5) & (arr<10)]#write your code here
    print(ans)
    return ans
"""
     Expected Output:
              array([6, 9])
     """ 
function13()
print("*************************************************************************")

#task14
def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method
    arr = np.arange(10, 34, 1).reshape(8,3) #write reshape code
    print(arr)
    ans = np.split(arr, 4)#write your code here 
    print(ans)
    return ans
"""
     Expected Output:
       [array([[10, 11, 12],[13, 14, 15]]), 
        array([[16, 17, 18],[19, 20, 21]]), 
        array([[22, 23, 24],[25, 26, 27]]), 
        array([[28, 29, 30],[31, 32, 33]])]
     """
function14()
print("*************************************************************************")

#task15
def function15():
    #Sort following NumPy array by the second column
    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
    ans = arr[np.argsort(arr[:, 1])]#write your code here 
    print(ans)
    return ans
"""
     Expected Output:
           array([[-4,  1,  7],
                   [ 8,  2, -2],
                   [ 6,  3,  9]])
     """ 
function15()
print("*************************************************************************")

#task16
def function16():
    #Write a NumPy program to join a sequence of arrays along depth.
    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    ans = np.concatenate((x, y), axis=1)#write your code here 
    print(ans)
    return ans
"""
     Expected Output:
                [[[1 2]]
                 [[2 3]]
                 [[3 4]]]
     """ 
function16()
print("*************************************************************************")

#Task17
def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    arr = np.arange(1,10*10+1).reshape((10,10))
    #print(arr)
    ans = np.where((arr%3==1) & (arr%5==1), arr, 'YES')
    #print(ans)
    ans1= np.where((ans=='YES'), ans, 'NO')
    #ans=np.where((arr%3==0) & (arr%5==0), arr, 'NO')
    #ans = np.where(arr%5==1, arr, 'YES')
    #ans= np.dtype('U3') 
    print(ans1)
    #arr[(ans)] = 'YES'
    return  ans       # Write Your Code HERE
#Excpected Out
"""
array([['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO']],
      dtype='<U3')
"""
function17()
print("*************************************************************************")

#Task18
def function18():
    # count values of "students" are exist in "piaic"
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    y=np.intersect1d(piaic, students)
    x = np.count_nonzero(y)# Write you code Here
    print(x)
    return x
    #Expected output: 3
function18()
print("*************************************************************************")

# Task19
def function19():
    #Create variable "X" from 1,25 (both are included) range values
    #Convert "X" variable dimension into 5 rows and 5 columns
    #Create one more variable "W" copy of "X" 
    #Swap "W" row and column axis (like transpose)
    # then create variable "b" with value equal to 5
    # Now return output as "(X*W)+b:

    X = np.arange(1,26).reshape(5,5)  # Write your code here
    W = np.copy(X)
    W = np.transpose(W)# Write your code here 
    b = 5  # Write your code here
    output = (X*W)+b 
    print(output)# Write your code here
    return output
    #expected output
    """
    array([[  6,  17,  38,  69, 110],
       [ 17,  54, 101, 158, 225],
       [ 38, 101, 174, 257, 350],
       [ 69, 158, 257, 366, 485],
       [110, 225, 350, 485, 630]])
    """
function19()
print("*************************************************************************")

#Task20
def fucntion20():
    #apply fuction "abc" on each value of Array "X"
    x = np.arange(1,11)
    def xyz(x):
        return x*2+3-2
    a=xyz(x)
    print(a)
    return a#Write your Code here
#Expected Output: array([ 3,  5,  7,  9, 11, 13, 15, 17, 19, 21])
fucntion20()
print("*************************************************************************")
#--------------------------X-----------------------------X-----------------------------X----------------------------X---------------------

















