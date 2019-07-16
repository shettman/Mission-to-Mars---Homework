#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imports & Dependencies

from splinter import Browser
from bs4 import BeautifulSoup
import time


# In[2]:


#Site Navigation
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Mars News
news_url = "https://mars.nasa.gov/news/"
browser.visit(news_url)
time.sleep(1)
html = browser.html
soup = BeautifulSoup(html, "html.parser")

article = soup.find("div", class_='list_text')
news_title = article.find("div", class_="content_title").text
news_p = article.find("div", class_ ="article_teaser_body").text
print(news_title)
print(news_p)


# In[4]:


# JPL Mars Space Images - Featured Image
image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")

image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://www.jpl.nasa.gov" + image
print(featured_image_url)


# In[9]:


# Mars Weather
mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(mars_weather_url)
time.sleep(1)
mars_weather_html = browser.html
mars_weather_soup = BeautifulSoup(mars_weather_html, 'html.parser')

tweets = mars_weather_soup.find('ol', class_='stream-items')
mars_weather = tweets.find('p', class_="tweet-text").text
print(mars_weather)


# In[10]:


import pandas as pd
facts_url = "https://space-facts.com/mars/"
browser.visit(facts_url)
mars_data = pd.read_html(facts_url)
mars_data = pd.DataFrame(mars_data[0])
mars_facts = mars_data.to_html(header = False, index = False)
print(mars_facts)


# In[11]:


import time 
hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemispheres_url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")
mars_hemisphere = []

products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup=BeautifulSoup(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title": title, "img_url": image_url})

