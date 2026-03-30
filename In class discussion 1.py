#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read the data from the CSV file
data = pd.read_csv("Data-Week2.csv")

# Convert the "State-County FIPS" column to strings
data['State-County FIPS'] = data['State-County FIPS'].astype(str)

# Extract the relevant columns and convert them to strings
counties = data['State-County FIPS'][:50]  # Select the first 50 counties
very_low_income = data['Very Low Income'][:50].astype(str)
low_income = data['Low Income'][:50].astype(str)

# Convert income columns to numeric for stacking
very_low_income = pd.to_numeric(very_low_income, errors='coerce')
low_income = pd.to_numeric(low_income, errors='coerce')

# Create a numpy array for the x-axis positions
x = np.arange(len(counties))

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(x, very_low_income, label='Very Low Income', width=0.4)
plt.bar(x, low_income, label='Low Income', width=0.4, bottom=very_low_income)
plt.xlabel('County')
plt.ylabel('Count')
plt.title('Very Low Income vs. Low Income by County (First 50 Counties)')

# Show the plot
plt.show()


# In[ ]:




