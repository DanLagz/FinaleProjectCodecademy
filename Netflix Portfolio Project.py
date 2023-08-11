#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
# 

# ## Goals
# This notebook contains an analysis on some Global earth temperature.  The goal for this project was to do the following:
# * Get acquainted with the data
# * Clean the data so it is ready for analysis
# * Develop some questions for analysis
# * Analyze variables within the data to gain patterns and insights on these questions

# ## Data
# The data for the project is taken from Kaggle:
# https://www.kaggle.com/datasets/joebeachcapital/global-earth-temperatures?resource=download
# 

# ### Loading the data 
# 

# First, the necessary libraries are loaded into the notebook. The pandas library is used to import data from Global Temperature.csv and preview the first five rows of the DataFrame.

# In[74]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import re


# In[75]:


df = pd.read_csv('Netflix Userbase.csv')


# ### Data Information
# Some immediate insights are:
# * There are 10 columns and 2,500 rows.
# * The name and datatype of each column -- most values are objects in this dataset.
# * There are no missing values 

# In[76]:


#to see all the columns
df.columns


# In[77]:


df.info()


# In[78]:


print(df.describe())


# In[79]:


#see if there is any missing data 
df.isnull().sum()


# ## Reading the Data 

# In[157]:


df.head(10)


# #### Data manipulation

# In[81]:


#print(df['Join Date'].dtype)   # Join Date is a object, we need to convert it into DateTime Type
df['Join Date'] = pd.to_datetime(df['Join Date'])
#print(df['Join Date'].dtype)
df['Join Year'] = df['Join Date'].dt.year


# ## The number of Males and Females

# In[82]:


gender = df['Gender'].value_counts()
print(gender)


# In[90]:


colors = ['#336BFF','#FFAC33']
plt.figure(figsize=(8,4))
plt.pie(gender.values, labels = gender.index, autopct='%1.1f%%',colors = colors, shadow = True)


# ## What devices are used the most by the users?

# In[50]:


deviceUsed = df.Device.value_counts()
print(deviceUsed)


# In[51]:


plt.figure(figsize=(8,4))
plt.title("Devices used by users")
plt.bar_label(plt.bar(deviceUsed.index, deviceUsed.values, width = 0.7, color = ['#336BFF',"#C94845","#49D845","#FFAC33"]))
plt.xlabel("Devices Used")
plt.ylabel("Number of device")


# ## Which are the most comman plans subscribed by users?
# 

# In[52]:


Plans = df['Subscription Type'].value_counts()
print(Plans)


# In[53]:


plt.figure(figsize=(8,4))
plt.title("Most Comman Plan")
plt.bar_label(plt.bar(Plans.index, Plans.values, width = 0.7, color = ['#336BFF',"#C94845","#49D845"]))
plt.xlabel("Plan")
plt.ylabel("Number of subscribed users")


# ## Which plan is giving the most income?

# In[145]:


#as we know the revenue of each plan is, basic = 10, standard = 12, premium = 15
plans = df['Subscription Type'].value_counts()
basic = 999 * 10
standard = 768 * 12
premium = 733 * 15
lst = [basic,standard,premium]
print(plans)
print(lst)


# In[158]:


plt.figure(figsize=(8,4))
plt.title("Most Profitble plan")
plt.bar_label(plt.bar(plans.index, lst, width = 0.7, color = ['#336BFF',"#C94845","#49D845"]))
plt.xlabel("Plan")
plt.ylabel("Money")


# ## Number of User on Devices and their Age
# 

# In[135]:


plt.figure(figsize=(8,4))
device_data = df.groupby(['Device','Age']).count()['User ID'].reset_index()
device_data.rename(columns = {'Device':'Device' , 'Age':'Age', 'User ID':'Num_of_User'}, inplace = True)
sns.scatterplot(data = device_data , x= 'Device' , y = 'Num_of_User', hue = 'Age', palette = 'mako')
plt.legend(loc= 'best' ,bbox_to_anchor=(1, 1))
plt.title('Number of User on Devices and their Age')


# ## Age distribution

# In[165]:


plt.figure(figsize=(8,4))
sns.histplot(data=df,x="Age",stat="count",color = '#336BFF',bins = 15)
plt.title("Age Distribution")
plt.show()


# ## Devices used by countries

# In[121]:


countryGroup = df.groupby(['Country'])
lst = []
for countries in df.Country.unique():
    smartphoneCount = countryGroup.get_group(countries).Device.value_counts()['Smartphone']
    laptopCount = countryGroup.get_group(countries).Device.value_counts()['Laptop']
    smartTVCount = countryGroup.get_group(countries).Device.value_counts()['Smart TV']
    tabletCount = countryGroup.get_group(countries).Device.value_counts()['Tablet']
     
    dic = {'Country': countries, 'Smartphone': smartphoneCount, 'Laptop': laptopCount, 'SmartTV': smartTVCount, 'Tablet': tabletCount}
    lst.append(dic)
newDF = pd.DataFrame.from_dict(lst)
print(newDF)
newDF.plot.bar(x = "Country", y = ["Smartphone",  "Laptop",  "SmartTV",  "Tablet"], title="Devices used by countries",figsize=(10,6), rot=20)


# ### Conclusion
# 
# #### Findings Overview
# Although the least common plan is `premium` still that plan is making the most money, interesting insights about `Devices` and `Country`, how different countries prefer to watch Netflix. This is also interesting how almost every 5 years of age the amount of people using Netflix is dropped.
# 
# 
# 
# 
