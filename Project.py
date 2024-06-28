#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
a= pd.read_excel("Downloads/HR-Employee-Data.xlsx")
df=pd.DataFrame(a)
df


# In[27]:


lowest_salary_employees = df[df['salary'] == 'low']
lowest_salary_employees[['Emp_Id']]


# In[21]:


salary_counts = df['salary'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(salary_counts, labels=salary_counts.index, autopct='%1.1f%%', startangle=140, colors=['blue','red','green'])
plt.title('Employee Distribution by Salary')
plt.axis('equal')  
plt.show()


# In[28]:


high_satisfaction_employees = df[df['satisfaction_level'] > 0.75]
high_satisfaction_employees


# In[26]:


high_hours_employees = df[df['average_montly_hours'] > 200]
high_hours_employees


# In[30]:


it_employees = df[df['Department'] == 'IT'][['Emp_Id', 'number_project']]
it_employees.head()


# In[32]:


df_cleaned = df.drop(columns=['Work_accident', 'left'])
df_cleaned.head()

