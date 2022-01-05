#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


df=pd.read_csv(r'C:\Users\DELL\Downloads\archive\Iris.csv')
df


# In[6]:


df.describe()


# In[7]:


# random test observation created 
test=[6.05,3.8,4.7,1.96]


# In[8]:


import numpy as np
y=df.drop(["Species","Id"],axis=1)


# In[9]:


#Distance function for n number of features
def euclidean_distance(a, b):
    dim = len(a)       # Store the number of dimensions
    distance = 0
    for d in range(dim):
        distance += abs(a[d] - b[d])**2
    distance = distance**(1/2)
    return distance


# In[10]:


#finding distance of each datapoint from test point
distance=[]
for i in y.index:
    d=euclidean_distance(test, y.iloc[i])
    distance.append(d)
df['distance']=distance
df


# In[11]:


#sort and get k closest datapoints
df1=df.sort_values("distance")[:5]
df1


# In[12]:


#Select class based on class of maximum out of k observations
from collections import Counter

# Create counter object to track the labels

counter = Counter(df1["Species"])
#Select class based on class of maximum out of k observations
counter.most_common()[0][0]


# In[ ]:




