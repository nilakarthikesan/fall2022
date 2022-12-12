#!/usr/bin/env python
# coding: utf-8

#   **CMSC320 FINAL PROJECT** 
# 
# 
#  **Introduction:** 
#  
# In this data science tutorial, I will be using data from the Women's Tennis Association, which is the principal organizing body of women's professional tennis in order to analyze how this information can be used to display data. 
#  
# This data shows us the rankings and matches of Women's tennis players from 2022 which can be used to display many indiciative stats in Women's tennis. A person might want to analyze this data if they were interested in understanding the attriubtes that went into Women's tennis. 
# 

#  **About the Data:** 
# 
# I have chosen to use a dataset that can be found at https://github.com/JeffSackmann/tennis_wta. Here I took the data set that shows us the WTA tennis matches from 2022. 
# 

# **Setup the Packages** 
# 
# These are the packages that we will be using.

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from collections import Counter
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# This is one of the datasets that I had mentioned earlier that displays the womens tennis matches from 2022.

# In[4]:


matches2022 = pd.read_csv('wta_matches_2022.csv')
matches2022.head()


# This is another dataset that I will be using which displays the womens tennis players from 2022. 

# In[5]:


players = pd.read_csv('wta_players.csv')
players.head()


# I will also be using a dataset to display the 2022 WTA rankings. 

# In[6]:


ranks = pd.read_csv('wta_rankings_20s.csv')
ranks.head()


# **Exploratory Data Analysis** 

# Players with the most Wins:
# 
# Here I am seeing who the most dominant players in womens tennis and it can be seen that Smith has been the dominant player. 

# In[8]:


colours = list()
for i in range(0,10):
    colours.append((random.random(), random.random(), random.random(),random.uniform(0.8,1)))
players['name_last'].value_counts().head(20).plot.bar(color=colours,figsize=(10,6),title="Players with most wins")
plt.show()


# **Hypothesis testing**
# 
# 
# Hand of Players: 
# 
# I want to test if there is a preferred hand for the majority of tennis players. We can clearly see that most of the players are right handed and there are many that are undetermined. 

# In[9]:


players['hand'].value_counts().plot.bar(color={'#8470ff','#3cb371','#ff4500'},figsize=(10,6),title="Handedness of players")
plt.show()


# Countries with most players in WTA: 
# 
# I want to test which countries have the most talented tennis players so see if the economic state of a country can influence the number of players from a country. After displaying th data in a bar graph I am able to denote that the countries with the most dominant tennis players come from the United States and Great Britian. In addition it can clearly be seen that the United States is ahead of other countries by a large margin.

# In[11]:


colours = list()

for i in range(0,10):
    colours.append((random.random(), random.random(), random.random(),random.uniform(0.8,1)))
players['ioc'].value_counts().head(20).plot.bar(color=colours,figsize=(10,6),title="Countries with most players in WTA")
plt.show()


# **Conclusion 
# 
# 
#  The conclusions I can draw from my analysis range understanding who the dominant tennis players are in Womens Tennis Association and I am able to see the dominant hand that the women use to play with. Other analysis that we can see are the countries that produce the most talented tennis players. We cans see that the United States produces the best players, this is probably because of the economic wealth in the United States. Playeres are given the best resources to succeed. 
# 
# 
# 
# 
