#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the CSV file
df_cocoa = pd.read_csv('D:/flavors_of_cocoa.csv')


# In[2]:


df_cocoa.describe()


# In[3]:


columns = df_cocoa.columns
print("Columns in the DataFrame:")
print(columns)


# # Which of the following variable have null values?

# In[4]:


# Check for null values in each column
null_values = df_cocoa.isnull().sum()


# In[5]:


columns_with_nulls = null_values[null_values > 0]

print("Columns with null values:")
print(columns_with_nulls)


# # Which of the following countries have maximum locations of cocoa manufacturing companies?

# In[6]:


# Group by the 'Country' column and count the number of occurrences for each country
country_counts = df_cocoa['Company Location'].value_counts()

# Get the country with the maximum locations
max_country = country_counts.idxmax()
max_count = country_counts.max()

print(f"The country with the maximum locations of cocoa manufacturing companies is {max_country} with {max_count} locations.")


# # After checking the data summary, which feature requires a data conversion considering the data values held?

# In[7]:


# Display a summary of the data types and non-null counts
data_summary = df_cocoa.info()


# In[8]:


# Optionally, display a statistical summary of the data
stat_summary = df_cocoa.describe(include='all')


# In[9]:


# Display unique values of each column to check for inconsistencies
unique_values = {col: df_cocoa[col].unique() for col in df_cocoa.columns}


# In[10]:


# Print the results
print("Data Types and Non-Null Counts:")
print(data_summary)


# In[11]:



print("\nStatistical Summary:")
print(stat_summary)


# In[12]:


print("\nUnique Values in Each Column (useful for detecting inconsistent data types):")
for col, values in unique_values.items():
    print(f"{col}: {values[:5]}...")  # Displaying only the first 5 unique values for brevity


# # What is the maximum rating of chocolates?

# In[13]:


# Find the maximum rating
max_rating = df_cocoa['Rating'].max()


# In[14]:


print("The maximum rating of chocolates is:", max_rating)

