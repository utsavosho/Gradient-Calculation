#!/usr/bin/env python
# coding: utf-8

# In[6]:


from sympy import *
x = Symbol('x')
y = Symbol('y')
f = x**2*y - x*y**2
dfdx=diff(f, x)
dfdy=diff(f, y)

def grad():
    print("This is a program to find the Gradient of x**2*y - x*y**2")
    
    x0 = input("Enter the value for x co-ordinate: ")
    y0 = input("Enter the value for y co-ordinate: ")
    try:
            x0=float(x0)
            y0=float(y0)
            a = dfdx.evalf(2,subs={x: x0, y:y0})
            b = dfdy.evalf(2,subs={x: x0, y:y0}) 
            sol = [a,b]
            print("The gradient is:", sol)
    except ValueError:

            print("Invalid Parameters")


# In[7]:


grad()


# In[8]:


grad()


# In[ ]:




