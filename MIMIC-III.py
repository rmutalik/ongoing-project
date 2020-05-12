#!/usr/bin/env python
# coding: utf-8

# ## Import Libraries

# In[1]:


# Import libraries
import os, os.path
import shutil

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ## Load Data

# In[9]:


# Load Data
csv_folder = r'C:\Users\rmutalik\Desktop\mimic-iii-clinical-database-1.4'
df_dict = {}

# Loop through all files in folders
for file in os.listdir(csv_folder):
    
    if file.endswith(".csv"):
        name = os.path.splitext(file)[0]

        # If file size is greater than ~100MB, skip it
        MAX_FILE_SIZE = 100000000
        physical_file = os.path.join(csv_folder, file)
        statinfo = os.stat(physical_file)
#         print(statinfo)            
        if statinfo.st_size > MAX_FILE_SIZE:
            standardized_size = statinfo.st_size / (10**6)
            print(file, standardized_size, "MB")
            continue
        else:
            df_dict[name] = pd.read_csv(physical_file)


# In[10]:


df_dict.keys()


# In[11]:


from sys import getsizeof

print(getsizeof(df_dict), "bytes")


# ## Explore Data

# In[12]:


df_admissions = df_dict['ADMISSIONS']


# In[13]:


df_admissions.head()


# In[14]:


df_admissions.describe()


# In[23]:


df_admissions.isna().sum()

