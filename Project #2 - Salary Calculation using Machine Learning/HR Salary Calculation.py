#!/usr/bin/env python
# coding: utf-8

# In[3]:


# We are going to use polynomial linear regression because generally salaries can be expressed with this formula
# y = a+bx+cx^2+dx^3+... by the years of experience to salary. We can see with matplotlib.pyplot

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("salaries_dataset.csv",sep=";")


# In[4]:


df


# In[5]:


plt.scatter(df['experience_level'],df['salary'])
plt.xlabel('Experience Level')
plt.ylabel('Salary')
plt.show()


# In[13]:


# Polynamial functions degree of 2 is y = a + bx + cx^2

polynomial_regression = PolynomialFeatures(degree=4)

x_polynomial = polynomial_regression.fit_transform(df[['experience_level']])


# In[14]:


reg = LinearRegression()
reg.fit(x_polynomial,df['salary'])


# In[15]:


y_head = reg.predict(x_polynomial)
plt.plot(df['experience_level'],y_head, color="red",label="Polynomial Regression")
plt.legend()

plt.scatter(df['experience_level'],df['salary'])
plt.show()

#we can change degree of polynomial_regression to get better results.


# In[16]:


x_polynomial1 = polynomial_regression.fit_transform([[4.5]])
reg.predict(x_polynomial1)


# In[ ]:




