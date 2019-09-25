# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:40:32 2019
@author: SAVANT.SPECTER
"""

from pathlib import Path
import re
from datetime import date
from selenium import webdriver
from time import sleep
import pandas as pd
path_to_driver = str(Path.home()) + "\\Desktop\\chromedriver.exe"              # in order to use selenium with chrome have to have the standalone chrome drive program

baseurl = "https://blog.ethereum.org/"

browser = webdriver.Chrome(path_to_driver)                                     #open new browser
browser.get(baseurl)                                                           #go to the etherem blog homepage

blog_posts = []
stop = False
while not stop:                                                                #loop until no more "older pages"
    post_list = browser.find_elements_by_class_name("post-preview")            #get a list of all posts. They all have the class "post-preview"
    for post in post_list:
        sub_ele = post.find_element_by_tag_name("a")                           #get the sub element for hte link
        
        title = sub_ele.find_element_by_tag_name("h2").text                    #pull the title from a second sub element
        link = sub_ele.get_attribute("href")                                   #get the link
        date_ele = re.search("(\\d{4})/(\\d{1,2})/(\\d{1,2})",link)            #from the link determine the date -- this uses a simple regular expression
        
        year = int(date_ele.group(1))
        month = int(date_ele.group(2))
        day = int(date_ele.group(3))    
        date1 = date(year,month,day)                                           #convert the date to a date obj for easier processing
        
        blog_posts.append((date1,title,link))                                  #add it to the link of all posts        
    try:                                                                       #selenium, when it can't find an element, throws an error - look for this error
        outer_posts_block = browser.find_element_by_class_name("next")         #try to find an "older posts" button
        older_posts_button = outer_posts_block.find_element_by_tag_name("a")   #get the sub element of that button
        older_posts_button.click()                                             #click on it
        sleep(1)                                                               #sleep for one second to wait for the page to load
    except:                                                                    #if the "older" button doesn't exist. Stop looping
        stop = True

browser.quit()                                                                 #close browser

df = pd.DataFrame(blog_posts,columns = ["date","title","link"])                #dataframe is unnecessary, but easier to work during analysis 

new_file = "blog_links.md.txt"                                                 #make a new file in the current directory, so no old files are changed programmatically
with open(new_file,"w+", encoding="utf-8") as fil:                             #encoding needed to handle the Eth symbol
    for i in range(df.shape[0]):                                               #format the line as markdown code
        text = "[%s - %s](%s)" % (
                df['date'][i].strftime("%Y.%m.%d"),
                df['title'][i].replace("]","").replace("[",""),
                df['link'][i]
                )
        print("%d - %s" % (i,text))                                            #print out in case there are any errors - easier to find and debug
        fil.write(text)                                                        #write line to file -- afterward the contents can be easily copy/pasted as desired
        fil.write("\n")
        