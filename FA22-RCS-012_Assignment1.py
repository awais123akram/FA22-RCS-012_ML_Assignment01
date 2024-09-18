#!/usr/bin/env python
# coding: utf-8

# In[55]:


"""Task 1: Lists, Dictionaries, Tuples
1.1. Creaye a list: nums = [3, 5, 7, 8, 12], make another list named ‘cubes’ and append the cubes of the given list ‘nums’
in this list and print it."""
nums = [3, 5, 7, 8, 12]
cubes = []
for num in nums:
    cubes.append(num**3)
print(cubes)


# In[56]:


"""1.2. Create an empty dictionary: dict = {}, add the following data to the dictionary: ‘parrot’: 2, ‘goat’: 4, ‘spider’: 8, ‘crab’:
10 as key value pairs."""
dict = {}
dict['parrot'] = 2
dict['goat'] = 4
dict['spider'] = 8
dict['crab'] = 10
print(dict)


# In[57]:


"""1.3. Use the ‘items’ method to loop over the dictionary (dict) and print the animals and their corresponding legs. Sum
the legs of each animal, and print the total at the end."""
dict = {'parrot': 2, 'goat': 4, 'spider': 8, 'crab': 10}
total_legs = 0
for animal, legs in dict.items():
    print(f"{animal}: {legs}")
    total_legs += legs
print(f"Total number of legs: {total_legs}")


# In[58]:


"""1.4. Create a tuple: A = (3, 9, 4, [5, 6]), change the value in the list from ‘5’ to ‘8’."""
A = (3, 9, 4, [5, 6])
A[3][0] = 8
print(A)


# In[59]:


"""1.5. Delete the tuple A."""
A = (3, 9, 4, [5, 6])
# After deletition of the tuple A there will be not exist any data in tuple A
del A


# In[60]:


"""1.6. Create another tuple: B = (‘a’, ‘p’, ‘p’, ‘l’, ‘e’), print the number of occurrences of ‘p’ in the tuple."""
B = ('a', 'p', 'p', 'l', 'e')
count_p = B.count('p')
print(f"The number of occurrences of 'p': {count_p}")


# In[61]:


"""1.7. Print the index of ‘l’ in the tuple."""
B = ('a', 'p', 'p', 'l', 'e')
index_l = B.index('l')
print(f"The index of 'l': {index_l}")


# In[62]:


"""Task 2: Numpy
Use built-in functions of numpy library to complete this task.
2.1 Convert matrix A into numpy array """
import numpy as np
A = [[1, 2, 3, 4], 
     [5, 6, 7, 8], 
     [9, 10, 11, 12]]
# Converting matrix  into an numpy array
A_array = np.array(A)
z = np.array([1, 0, 1])
print("Matrix A as numpy array:\n", A_array)


# In[63]:


""" 2.2 Use slicing to pull out the subarray consisting of the first 2 rows and columns 1 and 2. Store it in b which is a numpy
array of shape (2, 2)."""
import numpy as np
A = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8], 
              [9, 10, 11, 12]])
b = A[:2, 1:3]
print("Subarray b:\n", b)
print("Shape of b is :", b.shape)


# In[64]:


""" 2.3 Create an empty matrix ‘C’ with the same shape as ‘A’."""
import numpy as np
A = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8], 
              [9, 10, 11, 12]])
C = np.empty_like(A)
print("Shape of C:", C.shape)


# In[65]:


"""2.4 Add the vector z to each column of the matrix ‘A’ with an explicit loop and store it in ‘C’."""
import numpy as np
A = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8], 
              [9, 10, 11, 12]])
z = np.array([1, 0, 1])
C = np.empty_like(A)
for i in range(A.shape[1]):
    C[:, i] = A[:, i] + z
print("\nVector z:", z.shape)
print("Matrix C after adding vector z to each column of matrix A:\n", C)


# In[66]:


""" Create the following:
X = np.array([[1,2],[3,4]])
Y = np.array([[5,6],[7,8]])
v = np.array([9,10]) """
# Creating the arrays
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
print("Array X:\n", X)
print("Array Y:\n", Y)
print("Array v:\n", v)


# In[67]:


"""2.5 Add and print the matrices X and Y."""
SuM_XY = X + Y
print("Sum of X and Y:\n", SuM_XY)


# In[68]:


"""2.6 Multiply and print the matrices X and Y."""
Prod_XY = X * Y
print("Element-wise multiplication of X and Y:\n", Prod_XY)


# In[69]:


"""2.7 Compute and print the element wise square root of matrix Y."""
Sqroot_Y = np.sqrt(Y)
print("Element-wise square root of Y:\n", Sqroot_Y)


# In[70]:


"""2.8 Compute and print the dot product of the matrix X and vector v."""
DoT_Prod_Xv = np.dot(X, v[:X.shape[1]])
print("Dot product of X and v:\n", DoT_Prod_Xv)


# In[71]:


"""2.9 Compute and print the sum of each column of X."""
Sum_Of_Column_X = np.sum(X, axis=0)
print("Sum of each column of X:\n", Sum_Of_Column_X)


# In[72]:


"""Task 3: Functions and Loops
3.1 Create a function ‘Compute’ that takes two arguments, distance and time, and use it to calculate velocity."""
def Compute(Dis, T):
    if T == 0:
        raise ValueError("Time cannot be zero for velocity !!!")
    velocity = Dis / T
    return velocity
Dis = 100 
T = 20 
velocity = Compute(Dis, T)
print(f"Velocity: {velocity} m/s")


# In[73]:


"""3.2 Make a list named ‘even_num’ that contains all even numbers up till 12. Create a function ‘mult’ that takes the list
‘even_num’ as an argument and calculates the products of all entries using a for loop."""
def mult(numbers):
    Prod = 1
    for num in numbers:
        Prod *= num
    return Prod
even_num = [i for i in range(2, 13, 2)]
product_of_even_num = mult(even_num)
print(f"List of even numbers: {even_num}")
print(f"Product of all even entries in above list: {product_of_even_num}")


# In[74]:


"""Task 4: Pandas
Create a Pandas dataframe named ‘pd’ that contains 5 rows and 4 columns,"""
import pandas as pd
data = {
    'C1': [1, 2, 3, 5, 5],
    'C2': [6, 7, 5, 4, 8],
    'C3': [7, 9, 8, 6, 5],
    'C4': [7, 5, 2, 8, 8]
}
# Creating the dataframe
df = pd.DataFrame(data)


# In[75]:


"""4.1 Print only the first two rows of the dataframe."""
print("First two rows:\n", df.head(2))


# In[76]:


"""4.2 Print the second column."""
print("Second column (C2):\n", df['C2'])


# In[77]:


"""4.3 Change the name of the third column from ‘C3’ to ‘B3’."""
df = df.rename(columns={'C3': 'B3'})
print("\nDataFrame after renaming C3 to B3:\n", df)


# In[78]:


"""4.4 Add a new column to the dataframe and name it ‘Sum’."""
df['Sum'] = df.sum(axis=1)


# In[79]:


"""4.5 Sum the entries of each row and add the result in the column ‘Sum’."""
print("\nDataFrame with 'Sum' column:\n", df)


# In[80]:


"""4.6 Read CSV file named ‘hello_sample.csv’into a Pandasdataframe.
4.7 Print complete dataframe."""
import pandas as pd
df = pd.read_csv('hello_sample.csv')


# In[81]:


""" 4.7 Print complete dataframe."""
print("Complete DataFrame:\n", df)


# In[82]:


""" 4.8 Print only bottom 2 records of the dataframe."""
print(df.tail(2))


# In[83]:


""" 4.9 Print information about the dataframe."""
print(df.info())


# In[84]:


"""4.10 Print shape (rows x columns) of the dataframe."""
print(df.shape)


# In[85]:


""" 4.11 Sort the data of the dataFrame using column ‘Weight’."""
df_sorted = df.sort_values(by='Weight')
print(df_sorted)


# In[86]:


"""4.12 Use isnull() and dropna() methods of the Pandas dataframe and see if they produce any changes."""
missing_values = df.isnull()
print("Missing values in the DataFrame:")
print(missing_values)
df_dropped = df.dropna()
print("\nDataFrame after dropping missing values:")
print(df_dropped)
if df.shape != df_dropped.shape:
    print("\nChanges were made: Rows with missing values were removed.")
else:
    print("\nNo changes were made: No missing values were found.")

