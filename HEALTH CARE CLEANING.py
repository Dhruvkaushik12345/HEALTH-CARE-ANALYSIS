# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 18:01:20 2025

@author:DHRUV KAUSHIK
"""
import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\Users\DELL\Desktop\data sets\HEALTHCARE\healthcare_dataset.csv")

print('original data:')

print(df.columns)

x = df[df[['Room Number','Age','Billing Amount']].isnull().all(axis=1)]

# Fill NaN values with the mean for specific columns

# Removing Duplicates

df.duplicated()
df = df.drop_duplicates()
print(df)

df.to_csv(r"C:\Users\DELL\Desktop\data sets\HEALTHCARE\Healthcare Cleaned_Data.csv")

print("\ncleaned data has been exported as 'Healthcare Cleaned_Data.csv'")












