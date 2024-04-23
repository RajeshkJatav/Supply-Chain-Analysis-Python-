#!/usr/bin/env python
# coding: utf-8

# In[ ]:


FINANCIAL BUDGET ANALYSIS WITH (PYTHON)


# In[23]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[47]:


df = pd.read_csv(r'C:\Users\WB96\Desktop\Projects\FY-India-2021.csv', encoding= 'unicode_escape')


# In[48]:


df.shape


# In[49]:


df.head()


# In[68]:


print(df)


# In[140]:


df.dropna()


# In[54]:


#find for null values in the data 
df.isnull().sum() 


# In[55]:


df.columns


# In[65]:


df.rename(columns={'MINISTRY OF POWER': 'MINISTRY OF POWER & ELECTRICITY'}, inplace=True)


# In[71]:


df.describe()


# In[ ]:


EXPLORATORY DATA ANALYSIS (EDA)


# In[159]:


#Plot bar graph for the ministries w.r.t fund allocation.
# Create a DataFrame from your data
data = {
    'Department': [
        "MINISTRY OF AGRICULTURE", "DEPARTMENT OF ATOMIC ENERGY", "MINISTRY OF AYURVEDA, YOGA",
        "MINISTRY OF CHEMICALS AND FERTILISER", "MINISTRY OF CIVIL AVIATION", "MINISTRY OF COAL",
        "MINISTRY OF COMMERCE AND INDUSTRY", "MINISTRY OF COMMUNICATION", "MINISTRY OF CONSUMER AFFAIRS",
        "MINISTRY OF CORPORATE AFFAIRS", "MINISTRY OF CULTURE", "MINISTRY OF DEFENCE",
        "MINISTRY OF DEVELOPMENT OF NORTH EASTERN REGION", "MINISTRY OF EARTH SCIENCES", "MINISTRY OF EDUCATION",
        "MINISTRY OF ELECTRONICS AND INFORMATION TECHNOLOGY", "MINISTRY OF ENVIRONMENT, FOREST",
        "MINISTRY OF EXTERNAL AFFAIRS", "MINISTRY OF FINANCE", "MINISTRY OF FISHERIES, ANIMAL HUSBANDRY",
        "MINISTRY OF FOOD PROCESSING INDUSTRIES", "MINISTRY OF HEALTH AND FAMILY WELFARE", "MINISTRY OF HEAVY INDUSTRIES",
        "MINISTRY OF HOME AFFAIRS", "MINISTRY OF HOUSING AND URBAN AFFAIRS", "MINISTRY OF INFORMATION AND BROADCASTING",
        "MINISTRY OF JAL SHAKTI", "MINISTRY OF LABOUR AND EMPLOYMENT", "MINISTRY OF LAW AND JUSTICE",
        "MINISTRY OF MICRO, SMALL AND MEDIUM ENTERPRISES", "MINISTRY OF MINES", "MINISTRY OF MINORITY AFFAIR",
        "MINISTRY OF NEW AND RENEWABLE ENERGY", "MINISTRY OF PANCHAYATI RAJ", "MINISTRY OF PARLIAMENTARY AFFAIRS",
        "MINISTRY OF PERSONNEL, PUBLIC GRIEVANCES", "MINISTRY OF PETROLEUM AND NATURAL GAS", "MINISTRY OF PLANNING",
        "MINISTRY OF PORTS, SHIPPING", "MINISTRY OF POWER", "THE PRESIDENT, PARLIAMENT, UNION PUBLIC SERVICE COMMISSION",
        "MINISTRY OF RAILWAYS", "MINISTRY OF ROAD TRANSPORT AND HIGHWAY", "MINISTRY OF RURAL DEVELOPMENT",
        "MINISTRY OF SCIENCE AND TECHNOLOGY", "MINISTRY OF SKILL DEVELOPMENT", "MINISTRY OF SOCIAL JUSTICE AND EMPOWERMENT",
        "DEPARMENT OF SPACE", "MINISTRY OF STATISTICS", "MINISTRY OF STEEL", "MINISTRY OF TEXTILES", "MINISTRY OF TOURISM",
        "MINISTRY OF TRIBAL AFFAIRS", "MINISTRY OF WOMEN AND CHILD DEVELOPMENT", "MINISTRY OF YOUTH AFFAIRS AND SPORTS"
     
    ],
    'Fund allotted(in crores)': [
        131531.19, 18264.89, 2970.3, 80714.94, 3224.67, 534.88, 12768.25, 75265.22, 256948.4, 712.13, 2687.99,
        478195.62, 2658, 1897.13, 93224.31, 9720.66, 2869.93, 18154.73, 1386273.3, 4322.82, 1308.66, 73931.77,
        1017.08, 166546.94, 54581, 4071.23, 69053.02, 13306.5, 3229.94, 15699.65, 1466.82, 4810.77, 5753, 913.43,
        65.07, 2097.24, 15943.78, 1062.77, 1702.35, 15322, 1687.57, 110054.64, 118101, 133689.5, 14794.03, 2785.23,
        11689.39, 13949.09, 1409.13, 39.25, 3631.64, 2026.77, 7524.87, 24435, 2596.14,
    ]
}

df = pd.DataFrame(data)

# Plotting the bar graph
plt.figure(figsize=(8, 17))
plt.barh(df['Department'], df['Fund allotted(in crores)'], color='skyblue')
plt.xlabel('Fund allotted(in crores)')
plt.ylabel('Department / Ministry')
plt.title('Fund Allotted to Different Departments / Ministries')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest value at the top
plt.show()


# In[ ]:


#We can see that not all the departments that are covered in this dataset are the main departments, 
as some departments can be covered in the others category. 
So let’s prepare the data by only selecting the main departments and putting all the other departments in the other category.


# In[157]:


# Data for the top 10 ministries and "OTHERS"
ministries = ["MINISTRY OF AGRICULTURE", "MINISTRY OF CONSUMER AFFAIRS", "MINISTRY OF DEFENCE", 
              "MINISTRY OF EDUCATION", "MINISTRY OF FINANCE", "MINISTRY OF HOME AFFAIRS", 
              "MINISTRY OF RAILWAYS", "MINISTRY OF ROAD TRANSPORT AND HIGHWAY", 
              "MINISTRY OF RURAL DEVELOPMENT", "OTHERS"]

funds = [131531.19, 256948.40, 478195.62, 93224.31, 1386273.30, 166546.94, 110054.64, 118101.00, 133689.50, 592971.08]

# Plotting the bar graph
plt.figure(figsize=(17, 7))
plt.bar(ministries, funds, color='skyblue')
plt.xlabel('Ministries')
plt.ylabel('Fund allotted (in ₹crores)')
plt.title('Top 10 Ministries Fund Allocation')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[ ]:


#As we cans see in above graph finance department is getting the most of the share from the total budget of the government.
Now let’s plot this data into a donut plot to have a clear view of the distribution of funds among all the departments:


# In[171]:


import matplotlib.pyplot as plt

# Data for the top 10 ministries and "OTHERS"
ministries = ["MINISTRY OF AGRICULTURE", "MINISTRY OF CONSUMER AFFAIRS", "MINISTRY OF DEFENCE", 
              "MINISTRY OF EDUCATION", "MINISTRY OF FINANCE", "MINISTRY OF HOME AFFAIRS", 
              "MINISTRY OF RAILWAYS", "MINISTRY OF ROAD TRANSPORT AND HIGHWAY", 
              "MINISTRY OF RURAL DEVELOPMENT", "OTHERS"]

funds = [131531.19, 256948.40, 478195.62, 93224.31, 1386273.30, 166546.94, 110054.64, 118101.00, 133689.50, 592971.08]

# Plotting the pie chart
plt.figure(figsize=(20, 9))
plt.pie(funds, labels=ministries, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
plt.title('Top 10 Ministries Fund Allocation')

# Draw a white circle at the center to make it a donut chart
centre_circle = plt.Circle((0,0),0.72,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

plt.tight_layout()
plt.show()


# In[ ]:


#We can see that the finance department is getting 40% of the funds. 
This is how we can analyze a dataset that contains data about the revenue and expenditure of the government for a financial year 2021.

