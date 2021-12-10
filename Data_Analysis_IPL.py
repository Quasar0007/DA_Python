#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().system(' pip install seaborn')
import seaborn as sns


# In[24]:


data = pd.read_csv("./IPL Matches 2008-2020.csv") #Loading the data


# In[25]:


data #Shows the data's rows, first five and last five


# In[26]:


data.head() #Shows first 5 records of the dataset


# In[27]:


data.head(-5) # shows both the first 5 and last five records of the dataset


# In[28]:


data.info() #Complete info about the columns


# In[29]:


data = data.drop(['method'], axis=1) #Removes the column with the name 'method'


# In[30]:


data


# ### Most Wins in IPL

# In[46]:


#The heading above is given using markdown from the drop down menu present at the top pane with 'code' value initially
temp = pd.DataFrame({"Winner": data['winner']})
count_wins = temp.value_counts()
#print(count_wins)

labels = [X[0] for X in count_wins.keys()]
bar, ax = plt.subplots(figsize=(20,12))
ax = plt.pie(x = count_wins, autopct = "%.1f%%", labels = labels)
plt.title("Most Wins in IPL from 2008-2020", fontsize = 18)
plt.show()


# ### Most Wins in Eliminator

# In[49]:


sns.countplot(data['winner'][data['eliminator'] == 'Y'], data = data) 
plt.title("Most Wins in an Eliminator", fontsize = 18)
plt.xticks(rotation=90) #Rotating the merged values in X-axis by 90-degree so that they appear vetical
plt.show()


# ### Toss Decision

# In[52]:


teams = data['toss_winner'].unique()

decision_making = pd.DataFrame([], columns = ['Toss Winner', 'Decision', 'Times'])

for id, element in enumerate(teams):
    temp_bat = data[(data['toss_winner']==element) & (data['toss_decision']=='bat')]
    temp_field = data[(data['toss_winner']==element) & (data['toss_decision']=='field')]
    
    decision_making = decision_making.append({'Toss Winner' : element, 'Decision': 'bat', 'Times': temp_bat['toss_winner'].count()}, ignore_index=True)
    decision_making = decision_making.append({'Toss Winner' : element, 'Decision': 'field', 'Times': temp_field['toss_winner'].count()}, ignore_index=True)


# In[53]:


decision_making


# In[55]:


sns.catplot(x = "Toss Winner", y="Times", hue="Decision", data=decision_making, kind='bar', height=5, aspect = 2)
plt.xticks(rotation=90)
plt.title("Toss Decision of IPL Teams")
plt.xlabel("IPL Teams")
plt.ylabel("Toss Decision")
plt.show()


# ### Famous Venues

# In[58]:


sns.barplot(x=data['venue'].value_counts().head(8).values, y=data['venue'].value_counts().head(8).index, data=data)
plt.title("Top Venues")
plt.xlabel("No. of Games Played")
plt.ylabel("Venues")
plt.show()


# ### Top Umpires_1

# In[59]:


sns.barplot(x = data['umpire1'].value_counts().head(5).index, y=data['umpire1'].value_counts().head(5).values, data=data)
plt.xticks(rotation=90)
plt.xlabel('Umpire 1')
plt.ylabel('No. of matches umpired')
plt.title("Top Umpires_1")
plt.show()


# ### Top Umpires_2

# In[62]:


sns.barplot(x = data['umpire2'].value_counts().head(5).values, y=data['umpire2'].value_counts().head(5).index, data=data)

plt.xlabel('Umpire 2')
plt.ylabel('No. of matches umpired')
plt.title("Top Umpires_2")
plt.show()


# In[ ]:




