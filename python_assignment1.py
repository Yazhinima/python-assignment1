#!/usr/bin/env python
# coding: utf-8

# # python assignment 1
Write a program which will find all such numbers which are 
divisible by 7 but are not a multiple of 5, between 2000 and 3200 
(both included). The numbers obtained should be printed
in a comma-separated sequence on a single line.


Write a Python program to accept the user's first and last name and then 
getting them printed in the the reverse order with a space between first name and last name.


Write a Python program to find the volume of a sphere with diameter 12 cm
Formula: V=4/3 * π * r 3

# In[59]:



new_list = []
for i in range(2000,3201):
    if i%7 == 0 != i%5:
        new_list.append(i)
print(new_list)

        


# In[3]:


first_name = input(str("First Name : " ))
last_name = input(str("Last_name : " ))

print(last_name, first_name)


# In[1]:


r = 12/2
v = (4/3) * 3.14 * (r **3)


print("volume of the sphere is : ", v)

