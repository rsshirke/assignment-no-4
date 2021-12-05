#!/usr/bin/env python
# coding: utf-8

# # Q1.Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

# In[3]:


y = lambda a : a+25
y(10)


# In[ ]:





# In[ ]:





# # Q2. Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# 
# 
# 

# In[1]:


my_list=[1,2,3,4,5,6,7]
def fun(b):
    return b*3


# In[4]:


list(map(fun,my_list))


# In[ ]:





# In[ ]:





# # Q3. Write a Python program to square the elements of a list using map() function.
# 
# 
# 
# Sample List: [4, 5, 2, 9]

# In[2]:


list(map(lambda  x : x**2,[4,5,2,9,]))


# In[ ]:




