#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
import re


# In[2]:


# im dead


# In[43]:


# Scrape Ryman events from URL and iterate through 5 following events pages.

# create empty tables to dump times and performer results into
all_days = []
all_times = []
all_perf = [] 
all_open = []

for u in range(1,6):
# convert range values to string to concat with url string
    page = str(u)
    
# apply string to end of url
    url = 'https://ryman.com/events/list/?tribe_event_display=list&tribe_paged=' + page
    
# print url while running loop to check page number iteration
    print(url)
    
# request html from url source
    r = requests.get(url)
    print(r.status_code)

# soup html from request as text
    soup = BS(r.text)
    
# find time tags
    showtimes = soup.findAll('time')
    
# select text from html time table 'showtimes'
    times_list = [x.text for x in showtimes]
    
# find event performer names from 'h2' using class identifier, to table 'performances'
    performances = soup.findAll('h2', attrs={'class':'tribe-events-list-event-title'})
    
# select text from html results table 'performances'
    perf_list = [x.find('a').get('title') for x in performances]
    
# extract date
    days = [i.split('day, ')[1].split('at ')[0] for i in times_list]

# extract times
    time = [i.split('t ')[1] for i in times_list]

# dump results into above created tables and add newly iterated results to the tables
    all_days += days
    all_times += time
    all_perf += perf_list
    
# find openers
    opener_data = soup.find_all('div', attrs = {'class':'tribe-beside-image'})
# if no openers exist in div/class, display message
    for x in opener_data:
        openers = x.find('span', class_='opener').text if x.find('span', class_='opener') else '<No Opening Act>'
# if opener text is less than 3 characters, display message        
        if len(openers) < 3:
            all_open.append('<No Opening Act')
        else:
            all_open.append(openers)
            
# create empty DF for times and performer results
everything = pd.DataFrame()

# create df column for artists and showtimes, populate from previous dump tables
everything['artist'] = all_perf
everything['day'] = all_days
everything['time'] = all_times
everything['opening_acts'] = all_open

# check final df results
everything.head(15)


# In[40]:





# In[41]:





# In[42]:





# In[ ]:




