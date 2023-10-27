#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from kmodes.kprototypes import KPrototypes


# In[6]:


df = pd.read_csv("segmentation-data.csv")
df.head()


# In[7]:


df.isnull().sum()


# In[ ]:


# Our data has no nulls. Good!


# In[8]:


df_temp = df[['ID','Age','Income']]
df_temp


# In[ ]:


# Time to scaling


# In[9]:


scaler = MinMaxScaler()
scaler.fit(df[['Age']])
df['Age'] = scaler.transform(df[['Age']])

scaler.fit(df[['Income']])
df['Income'] = scaler.transform(df[['Income']])


# In[10]:


df = df.drop(['ID'],axis=1)
#Since we do not use ID in analysis


# In[11]:


mark_array = df.values
mark_array[:,2] = mark_array[:,2].astype(float)
mark_array[:,4] = mark_array[:,4].astype(float)
#convert age and income to float


# In[12]:


df.head()


# In[27]:


kproto = KPrototypes(n_clusters=25, verbose=2,max_iter=20)
clusters= kproto.fit_predict(mark_array, categorical = [0,1,3,5,6])

print(kproto.cluster_centroids_)
len(kproto.cluster_centroids_)


# In[28]:


clusters_col=[]
for c in clusters:
    clusters_col.append(c)
    
df['cluster']=clusters_col

#put original columns from temp to df
df[['ID','Age','Income']] = df_temp


# In[25]:


df[df['cluster']==0].head(10)


# In[26]:


colors = ['green','red','gray','orange','yellow','cyan','magenta','brown','purple','blue']

plt.figure(figsize=(15,15))
plt.xlabel('Age')
plt.ylabel('Income')

for i, col in zip(range(10),colors):
    dftemp = df[df.cluster==i]
    plt.scatter(dftemp.Age,dftemp['Income'],color=col, alpha=0.5)

plt.legend()
plt.show()


# In[ ]:




