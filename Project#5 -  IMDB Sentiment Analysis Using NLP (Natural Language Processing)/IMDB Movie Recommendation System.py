#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from bs4 import BeautifulSoup
import re
import nltk
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords


# In[4]:


df = pd.read_csv('labeledTrainData.tsv', delimiter = "\t", quoting=3)


# In[5]:


df.head()


# In[6]:


len(df)


# In[7]:


len(df["review"])


# In[8]:


nltk.download('stopwords')
#we cannot use stopwords such as the,it,as,by,with in NLP (natural language process)


# In[9]:


# There are HTML tags in dataset we should delete them.
# We are going to use BeautfiulSoup Module to clean them.
sample = df.review[0]
sample


# In[10]:


sample = BeautifulSoup(sample).get_text()
sample
#to clear HTML tags


# In[11]:


sample = re.sub("[^a-zA-Z]",' ',sample)
sample
#to clear punctation and numbers


# In[13]:


sample = sample.lower()
sample
#make all letters lower


# In[14]:


sample = sample.split()
# we are going to get rid of stopwords by split all words and put them all in a list


# In[15]:


sample


# In[16]:


len(sample)


# In[17]:


swords = set(stopwords.words("english"))
sample = [w for w in sample if w not in swords]
sample


# In[18]:


len(sample)


# In[57]:


# it was sample we are going to do it for 25000 review, so let's create a function
def process(review):
    review = BeautifulSoup(review).get_text()
    review = re.sub("[^a-zA-Z]",' ',review)
    review = review.lower()
    review = review.split()
    swords = set(stopwords.words("english"))
    review = [w for w in review if w not in swords]
    return(" ".join(review))


# In[58]:


train_x_tum= []
for r in range(len(df["review"])):
    if(r+1)%1000 == 0:
        print("No of reviews processed =", r+1)
    train_x_tum.append(process(df["review"][r]))
    


# In[59]:


x = train_x_tum
y = np.array(df["sentiment"])

train_x, test_x, y_train, y_test = train_test_split(x,y, test_size=0.1)


# In[60]:


vectorizer = CountVectorizer(max_features = 5000)
train_x = vectorizer.fit_transform(train_x)


# In[61]:


train_x


# In[62]:


train_x = train_x.toarray()
train_y = y_train


# In[63]:


train_x.shape, train_y.shape


# In[64]:


train_y


# In[65]:


model = RandomForestClassifier(n_estimators = 100, random_state=42)
model.fit(train_x,train_y)


# In[67]:


test_xx = vectorizer.transform(test_x)


# In[69]:


test_xx


# In[70]:


test_xx = test_xx.toarray()


# In[71]:


test_xx.shape


# In[72]:


test_predict = model.predict(test_xx)
acc = roc_auc_score(y_test,test_predict)


# In[73]:


print("Accuracy % ", acc * 100)


# In[ ]:




