#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#We use sklearn library in many machine learning calculations and we use pandas which is well-known ml library.
from sklearn import linear_model

#then we import dataset
df = pd.read_csv("housepricesdataset.csv",sep=";")


# In[2]:


#to check our dataset 
df


# In[6]:


#Time to define linear regression model
reg = linear_model.LinearRegression()
reg.fit(df[['area','roomcount','buildingage']], df['price'])

#reg.fit(df[input values], [output values])


# In[7]:


#Our model is ready, we can make predictions with using this model

reg.predict([[230,4,10]])


# In[8]:


reg.predict([[230,6,0]])


# In[10]:


reg.predict([[355,3,20]])


# In[11]:


#Let's see some details about our Linear Regression formula

#to see coefficients
reg.coef_


# In[12]:


#to see intercept
reg.intercept_


# In[13]:


# y = a + bX1 + cX2 + dX3 + ...
# This is formula of linear regression

# y = 262365.1503032055 + 1018.99865454*x1 + 14893.82374984*x2 - 2606.68429997*x3
# price = intercept + area + room count - building age


# In[14]:


a = reg.intercept_
b = reg.coef_[0]
c = reg.coef_[1]
d = reg.coef_[2]

x1= 355
x2= 3
x3= 20

y = a + b*x1 + c*x2 + d*x3
y


# In[ ]:




