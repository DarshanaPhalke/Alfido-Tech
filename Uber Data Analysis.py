#!/usr/bin/env python
# coding: utf-8

# # Uber Data Analysis

# #### Import required Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# #### Read dataset

# In[2]:


df=pd.read_csv('C:/Users/hp/Desktop/UberDataset.csv')


# #### First 5 rows of dataset

# In[3]:


df.head()


# #### Last 5 rows of dataset

# In[4]:


df.tail()


# #### Dimensions of dataset

# In[5]:


df.shape


# #### Check data types

# In[6]:


df.dtypes


# #### Check null values

# In[7]:


df.isna().sum()


# #### So, Observing the result of last 5 rows and checking null values:         the last row of the dataset contains Nan values and 503 values in 'PURPOSE' column are Null

# #### Drop last row

# In[8]:


df=df.drop(df.index[-1])
df.tail()


# #### We will replace null values by mode 
# 

# In[9]:


df['PURPOSE']=df['PURPOSE'].fillna(df['PURPOSE'].mode()[0])


# #### Re-check for null values

# In[10]:


df.isnull().sum()


# #### Statistical information of Numerical column

# In[11]:


df.describe()


# #### Statistical information of Categorical columns

# In[12]:


df.describe(include='object')


# In[13]:


df.info()


# #### Correct spelling mistake

# In[14]:


df['START']=df['START'].replace('Kar?chi','Karachi')
df['STOP']=df['STOP'].replace('Kar?chi','Karachi')

df['START']=df['START'].replace('R?walpindi','Rawalpindi')
df['STOP']=df['STOP'].replace('R?walpindi','Rawalpindi')


# In[15]:


df['START'].nunique()


# In[16]:


df['STOP'].nunique()


# #### Change data type of 'START_DATE' AND 'END_DATE' to datetime

# In[17]:


df['START_DATE']=pd.to_datetime(df['START_DATE'])


# In[18]:


df['END_DATE']=pd.to_datetime(df['END_DATE'])


# In[19]:


df.dtypes


# #### Seperate time from 'START_DATE' column

# #### Extract START_DAY & END_DAY from DATE

# In[20]:


df['START_DAY'] = df['START_DATE'].dt.day_name()
df['END_DAY'] = df['END_DATE'].dt.day_name()
df.head()


# #### Countplot of Number of rides by day

# In[21]:


plt.figure(figsize=(10, 6))
sns.countplot(x='START_DAY', data=df)
plt.xlabel('Day')
plt.ylabel('No. of Rides')
plt.title('No. of rides by day')
plt.show()


# #### Average of miles by purpose of ride:

# In[22]:


avg_miles_by_purpose =df.groupby('PURPOSE')['MILES'].mean()
avg_miles_by_purpose


# #### Visualization:

# In[23]:


plt.figure(figsize=(10,8))
plt.bar(avg_miles_by_purpose.index, avg_miles_by_purpose.values)
plt.xlabel('Purpose')
plt.ylabel('Average Miles')
plt.title('Average Miles for Personal and Business Purposes')
plt.xticks(rotation=45)
plt.show()


# #### Result: Most of the rides are booked to travel from work place to home i.e commute

# #### Average of miles by category of rides:

# In[24]:


avg_miles_by_category =df.groupby('CATEGORY')['MILES'].mean()
avg_miles_by_category


# #### Visualization:

# In[25]:


plt.figure(figsize=(10, 6))
sns.countplot(x='CATEGORY', data=df, order=df['CATEGORY'].value_counts().index)
plt.title('Distribution of Ride Categories')
plt.xlabel('Ride Category')
plt.ylabel('Number of Rides')
plt.show()


# #### Result: Most of the miles are travelled by business class people

# #### Count of rides booked by Top 10 start_points :

# In[26]:


top_10_start_points = df['START'].value_counts().nlargest(10)
print("Top 10 Start Points:")
print(top_10_start_points)


# #### Visualization:

# In[27]:


plt.figure(figsize=(10, 6))
plt.bar(top_10_start_points.index, top_10_start_points.values)
plt.xlabel('Start Points')
plt.ylabel('Count')
plt.title('Top 10 Start Points')
plt.xticks(rotation=90)
plt.show()


# #### Count of rides booked by Top 10 Stop_points :

# In[28]:


top_10_stop_points = df['STOP'].value_counts().nlargest(10)
print("\nTop 10 Stop Points:")
print(top_10_stop_points)


# #### Visualization:

# In[29]:


plt.figure(figsize=(10, 6))
plt.bar(top_10_stop_points.index, top_10_stop_points.values)
plt.xlabel('Stop Points')
plt.ylabel('Count')
plt.title('Top 10 Stop Points')
plt.xticks(rotation=90)
plt.show()


# #### Count of rides booked by least 10 Start_points :

# In[30]:


least_10_start_points = df['START'].value_counts().nsmallest(10)
print("\least 10 Start Points:")
print(least_10_start_points)


# In[32]:


least_10_stop_points = df['STOP'].value_counts().nsmallest(10)
print("\least 10 Stop Points:")
print(least_10_stop_points)


# #### Calculate duration:

# In[34]:


df['DURATION_MIN'] = (df['END_DATE'] - df['START_DATE']).dt.total_seconds() / 60
df.head()


# In[35]:


min_duration=df['DURATION_MIN'].min()
min_duration


# In[36]:


max_duration=df['DURATION_MIN'].max()
max_duration


# In[37]:


avg_duration=df['DURATION_MIN'].mean()
avg_duration


# In[39]:


plt.figure(figsize=(10, 6))
sns.histplot(df['DURATION_MIN'], bins=30, kde=True)
plt.title('Distribution of Ride Durations')
plt.xlabel('Ride Duration (minutes)')
plt.ylabel('Frequency')
plt.xlim(0, df['DURATION_MIN'].max())
plt.show()


# In[ ]:




