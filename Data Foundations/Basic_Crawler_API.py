# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 @way too late in th evening O'clock 2017

@author: Eric
"""
# Import the necessary resources
# In this case, urllib.request is the aspect of urllib we need to allow for headers to be set and to make urlopen calls
# urllib.parse is a utility featureset in urllib that makes parsing a url into major parts simpler than writing our own split and check function
# bs4 from beautifulsoup is there because regex is that know-it-all no one likes and beatifulsoup is the cool kid
# json is brought in to make working with json easy (though we could just think of it)
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as soup
import json

# This function takes in a URL and returns true if the URL is qualified and false if it is not
# qualified in this sense means it is a complete URL with network location
# as in it is a URL that has enough information to be reachable
def is_absolute(url):
    return bool(urllib.parse.urlparse(url).netloc)

# This function takes a reddit URL and returns the subreddit
# technically it would return the user name if you pass it a reddit username URL
def getsubreddit(url):
    subreddit = (urllib.parse.urlparse(url).path).split("/")[2]
    return subreddit

# This function interacts with the reddit API to retrieve JSON full of information about a passed in subreddit
# It then returns the subscriber and currently active user counts
def getapi(subreddit):
    r = str(getsource("https://www.reddit.com/r/" + subreddit + "/about/.json"))
    data = json.loads(r)
    subscribers = data.get("data").get("subscribers")
    active = data.get("data").get("accounts_active")
    return [str(subscribers), str(active)]

# This is a function that makes a URL request and returns the page source as a string
# Note that we are setting a commonly used header called user-agent to a commonly set value
# This is because many popular webservers check the user-agent as a basic way to filter out crawlers or spambots
def getsource(incoming):
    req=urllib.request.Request(incoming, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}) #sends GET request to URL
    uClient=urllib.request.urlopen(req)
    page_html=uClient.read() #reads returned data and puts it in a variable
    uClient.close() #close the connection
    page_soup=soup(page_html,"html.parser")
    return page_soup

# This is a function that pulls a set of initial links from the subreddit main page (passed in as trailhead)
# Number of trails is how many main page links we will chase
# If the number of links specified exceeds number of links found then limit to number found
# Returns an array containing the links representing the start points of the crawl
def starthike(trailhead, numtrails):
    result = []
    anchors=trailhead.findAll("a",{"class","title may-blank outbound"})
    if numtrails > len(anchors):
        numtrails = len(anchors)
        print("Only", numtrails, "trails found...adjusting depth.")
    for i in range(0, numtrails):
        if is_absolute(anchors[i].get('href')):
            result += [anchors[i].get('href')]
    return result

# This is the function that takes the passed in URL and finds the switcheroo link (attempts to, very basic)
# Returns the link it finds
def keephiking(onthetrail):
    divcontainers=onthetrail.findAll("div",{"class","sitetable nestedlisting"})
    for divcontainer in divcontainers:
        subdivs=divcontainer.findAll("div",{"class","md"})
        for subdiv in subdivs:
            anchors=subdiv.findAll("a")
            for anchor in anchors:
                if is_absolute(anchor.get('href')):
                    result = anchor.get('href')
    return result

# Subreddit start point
url="https://www.reddit.com/r/switcharoo/"

# How deep we want to crawl
depth = 5

# How many branching crawls we want from our start point
trailstochase = 1

# Function call to get the starting links for the crawl
trails = starthike(getsource(url),trailstochase)

# Creates a file to hold the csv output
# Opens it and writes the header to it
filename="switcharoo_api.csv"
f=open(filename,'w')
headers="link,depth,subreddit,subscribers,active\n"
f.write(headers)

# Cycles through the starting links and crawls through to the specified depth for each start point
# Writes the relevant data at each depth point (start point is technically depth 0)
for trail in trails:
    miles = 0
    subreddit = getsubreddit(trail)
    apidata = getapi(subreddit)
    row = trail + "," + str(miles) + "," + subreddit + "," + apidata[0] + "," + apidata[1] + "\n"
    f.write(row)
    while (depth > miles):
        subreddit = getsubreddit(trail)
        apidata = getapi(subreddit)
        trail = keephiking(getsource(trail))
        miles += 1
        row = trail + "," + str(miles) + "," + subreddit + "," + apidata[0] + "," + apidata[1] + "\n"
        f.write(row)

# close the file so that it writes and saves before the program ends
f.close()