import requests
from bs4 import BeautifulSoup
import csv
import re

#emojis are found in locations and titles frequently
#set a pattern for possible emojis that will that will help with removal
emoji_pattern=re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

#create a file that we will write parsed data to
filename="Burrows_HW4_ScrapedData.csv"
f=open(filename, 'w', newline="",encoding='utf-8')
csvwriter=csv.writer(f)
csvwriter.writerow(['Date', 'Location', 'Title', 'Price']) #create the header row

#Craigslist urls don't have a page number encoded, instead it uses the number of items on the page (typically 120)
i=0 #initialize a counter for the number of items on a page
while True:
    #url for xbox in Portland, Oregon
    page_link="https://portland.craigslist.org/search/sss?query=xbox&sort=date&s={}".format(i) #changes the url to different pages based on i
    res=requests.get(page_link)
    #use BS to parse the webpage
    soup=BeautifulSoup(res.text,'html.parser') #applying BS to the obtained html
    #find the chunks of information for all items
    data=soup.select('.result-info') #define the data early so an if condition can be constructed before the for loop
    #this is the condition that breaks out of the loop when there are no more results
    if not data:
        break
    #this is the same as in my required hw problem, but a simpler and more elegant approach 
    for container in data:
        date=container.select('.result-date')[0].text #finds all dates down to 'result-date' tag and selects text
        #first look for all local items denoted by 'result-hood'
        try:
            location=container.select('.result-hood')[0].text #finds all locations down to 'result-hood' tag and selects text
            location=emoji_pattern.sub(r'',location) #removes emoji patterns NOT NECESSARY
        #if 'result-hood' is not found, it's because it is part of the nearby items and must be searched for differently
        except:
            #second look for all nearby items denoted by 'nearby'
            try:
                location=container.select('.nearby')[0].text #finds all locations down to 'nearby' tag and selects text
                location=emoji_pattern.sub(r'',location) #removes emoji patterns NOT NECESSARY
            #finally if no location is found, return a '' because it was not on the page
            except:
                location=""
        title=container.select('.result-title')[0].text #finds all titles down to 'result-title' tag and selects text
        title=emoji_pattern.sub(r'',title) #removes emoji patterns NOT NECESSARY
        #first look for items with prices
        try:
            price=container.select('.result-price')[0].text #finds all prices down to 'result-price' tag and selects text
        #some items are not listed with a price, so return a ''
        except:
            price=""
        print(date,location,title,price) #print to screen to view scraped data
        #more efficicent way to write to the csv file without commas or delimiters causing problems
        csvwriter.writerow([date,location,title,price])
    i+=120 #increment the counter by 120, which allows the program to scrape the next page
f.close() #close the file
