#!/usr/bin/env python
# coding: utf-8

# In[1]:


#u.item and u.data will be used from Kaggle Movielens - 100k dataset 
#u.item movie id, name of the movie (1th and 2th columns)
#u.data user id, movie id, user rating (1th, 2th and 3th columns)


# In[2]:


import pandas as pd


# In[3]:


column_names = ['user_id', 'item_id','rating','timestamp']
df = pd.read_csv("u.data", sep = '\t', names = column_names)


# In[4]:


df.head() #Here we can see data frames


# In[5]:


len(df) # here is lenght of data frame


# In[9]:


column_names_sec = ['item_id','title']
movie_titles = pd.read_csv("u.item", sep = '|', names = column_names_sec, usecols=range(2),encoding='latin-1')


# In[10]:


movie_titles.head()


# In[11]:


len(movie_titles)


# In[12]:


df = pd.merge(df, movie_titles, on="item_id")
df.head()


# In[13]:


moviepivot = df.pivot_table(index='user_id',columns = 'title', values = 'rating')
moviepivot.head()


# In[14]:


type(moviepivot)


# In[34]:


starwars_user_ratings = moviepivot['Star Wars (1977)']
starwars_user_ratings.head()


# In[35]:


similar_to_starwars = moviepivot.corrwith(starwars_user_ratings)


# In[36]:


similar_to_starwars


# In[37]:


corr_starwars = pd.DataFrame(similar_to_starwars,columns = ["Correlation"])
corr_starwars.dropna(inplace = True)
corr_starwars.head()


# In[38]:


corr_starwars.sort_values('Correlation',ascending=False).head(10)


# In[39]:


df.head()


# In[40]:


df.drop(['timestamp'],axis=1)


# In[41]:


ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.sort_values('rating',ascending=False).head()


# In[42]:


ratings['rating_count'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()


# In[43]:


ratings.sort_values('rating_count',ascending=False).head()


# In[44]:


corr_starwars.sort_values('Correlation',ascending=False).head()


# In[45]:


corr_starwars = corr_starwars.join(ratings['rating_count'])
corr_starwars.head()


# In[46]:


corr_starwars[corr_starwars['rating_count']>100].sort_values('Correlation',ascending=False).head()


# In[ ]:





# In[ ]:




