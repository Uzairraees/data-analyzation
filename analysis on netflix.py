#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


df = pd.read_csv("D:/netflix data/netflix_titles.csv")
df.head()


# In[4]:


nan_df = df[df.isna().any(axis=1)]
display(nan_df.head())


# In[6]:


df.isna().sum()


# In[7]:


df = df.dropna(axis=0)


# In[8]:


df.isna().sum()


# In[9]:


df.shape


# In[10]:


df.columns


# In[11]:


df["type"].value_counts()


# In[12]:


df.groupby('type').size().plot(kind='bar')


# In[14]:


df.loc[:,'release_year']


# In[16]:


df.loc[:,['release_year','duration']]


# In[17]:


df['release_year'].plot.hist()


# In[18]:


df['country'].value_counts()


# In[19]:


df["rating"].value_counts()


# In[20]:


plt.figure(figsize=(12,6))
df.groupby('rating').size().plot(kind='bar')


# In[23]:



sns.countplot(x='rating' ,hue='type' ,data=df)

fig=plt.gcf()
fig.set_size_inches(12,6)
plt.title('Relation between type and rating')
plt.show()


# In[24]:


df.director.value_counts().head()


# In[25]:


df.listed_in.value_counts()


# In[26]:


df.listed_in.value_counts().head(10).plot(kind='bar')
plt.title('top 10 famous genere')
plt.show()


# In[ ]:




