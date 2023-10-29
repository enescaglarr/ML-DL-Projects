#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

df = pd.read_csv("train.csv")
df.head()


# In[2]:


df = df.drop(['PdDistrict','Address','Resolution','Descript','DayOfWeek'], axis=1)


# In[3]:


df.tail(5)


# In[4]:


df.isnull().sum()


# In[5]:


f = lambda x: (x["Dates"].split())[0]
df["Dates"] = df.apply(f,axis=1)
df.head()


# In[6]:


f = lambda x: (x["Dates"].split("-"))[0]
df["Dates"] = df.apply(f,axis=1)
df.head()


# In[7]:


df_2014 = df[(df.Dates == '2014')]
df_2014.head()


# In[8]:


scaler = MinMaxScaler()

scaler.fit(df_2014[['X']])
df_2014['X_scaled'] = scaler.transform(df_2014[['X']])

scaler.fit(df_2014[['Y']])
df_2014['Y_scaled'] = scaler.transform(df_2014[['Y']])


# In[9]:


df_2014.head()


# In[10]:


k_range= range(1,15)


# In[11]:


list_dist = []

for k in k_range:
    model = KMeans(n_clusters = k)
    model.fit(df_2014[['X_scaled','Y_scaled']])
    list_dist.append(model.inertia_)


# In[12]:


from matplotlib import pyplot as plt

plt.xlabel('K')
plt.ylabel('Distortian value')
plt.plot(k_range,list_dist)
plt.show()


# In[13]:


#Using elbow method to decide k which is 5 in our case


# In[14]:


model = KMeans(n_clusters=5)
y_predicted = model.fit_predict(df_2014[['X_scaled','Y_scaled']])
y_predicted


# In[15]:


df_2014['cluster'] = y_predicted
df_2014


# In[17]:


import plotly.express as px


# In[19]:


figure = px.scatter_mapbox(df_2014, lat='Y', lon='X',center =dict(lat=37.8, lon = -122.4),
                           zoom = 9, opacity = .9,mapbox_style = 'open-street-map',color='cluster',
                           title= 'San Francisco Crime Map', width = 1100, height = 700,
                           hover_data=['cluster','Category','Y','X'])


# In[20]:


figure.show()


# In[21]:


import plotly
plotly.offline.plot(figure,filename="SanFranciscoCrimeMap.html", auto_open=True)


# In[ ]:




