# Matrix Algebra


# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd


# In[4]:

# declare Matrices and Vectors
A = np.array([[1,2,3], [2,7,4]])
B = np.array([[1,-1], [0,1]])
C = np.array([[5,-1], [9,1],[6,0]])
D = np.array([[3,-2,-1], [1,2,3]])


# In[15]:

u = np.array([[6,2,-3,5]])
v = np.array([[3,5,-1,4]])
w = np.array([[1],[8],[0],[5]])


# In[17]:

print ('Dimensions of matix A: {}'.format(A.shape))
print ('Dimensions of matix B: {}'.format(B.shape))
print ('Dimensions of matix C: {}'.format(C.shape))
print ('Dimensions of matix D: {}'.format(D.shape))
print ('Dimensions of matix u: {}'.format(u.shape))
print ('Dimensions of matix v: {}'.format(v.shape))
print ('Dimensions of matix w: {}'.format(w.shape))
 
"""Answers
Dimensions of matix A: (2, 3)
Dimensions of matix B: (2, 2)
Dimensions of matix C: (3, 2)
Dimensions of matix D: (2, 3)
Dimensions of matix u: (1, 4)
Dimensions of matix v: (1, 4)
Dimensions of matix w: (4, 1)

"""
# 
# Vector Operations

# In[18]:

print(u+v)

# Answer: [[ 9  7 -4  9]]
# In[19]:

print(u-v)

# Answer [[ 3 -3 -2  1]]
# In[22]:

c = 6
print(c*u)

# Answer: [[ 36  12 -18  30]]
# In[23]:

print(u*v)
# Answer: [[18 10  3 20]]

# Magnitude of Vector

# In[34]:

print (np.sqrt((u*u).sum()))

# Answer: 8.60232526704
# Matrix Operations

# In[36]:

print ('A + C not defined')


# In[40]:

print (A - C.T)

# Answer: [[-4 -7 -3]
#          [ 3  6  4]]
# In[41]:

print(C.T  + 3*D)
# Answer: [[14  3  3]
#          [ 2  7  9]]

# In[46]:

print (B.dot(A))

# Answer: [[-1 -5 -1]
#          [ 2  7  4]]
# In[48]:

print ('B.dot(A.T) not defined')
