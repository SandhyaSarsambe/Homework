#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Q.1 Kilometers to Miles
Kilometers = float(input("Enter the value for Kilometers:"))
Miles = 0.62137 * Kilometers
print("The value for given kilometers in miles is", Miles)


# In[4]:


#Q.2 Degree Celsius to Fahrenheit
Celsius=float(input("Enter the temperature Value in celsius:"))
Fahrenheit= ((Celsius)*1.8)+32
print("Temp in Fahrenheit is", Fahrenheit)


# In[18]:


#Q.3 Displaying calendar 
import calendar 
Year = int(input("Enter the year:"))
Month = int(input("Enter the month:")) 
print(calendar.month(Year, Month))


# In[7]:


#Q.4 Solve Quadratic equation
import cmath
a=float(input("Enter a with (a!=0):"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
d= (b**2)-(4*a*c)
x1 = (-b+cmath.sqrt(d)/(2*a))
x2 = (-b-cmath.sqrt(d)/(2*a))
print("The solutions are {0} and {1}". format(x1, x2))


# In[12]:


#Q.5 Swap two variables without temp
a='sandhya'
b='sarsambe'
(a,b)=(b,a)
print(a,b)


# In[ ]:




