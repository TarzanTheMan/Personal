import urllib.request #functions and classes that help open URLs
import urllib.parse #break URL strings up in components, combine components back to URL string, convert URLs
from bs4 import BeautifulSoup #library for pulling data out of HTML files (navigating, searching, and modifying the parse tree)
import re #provides regular expression matching operations

from bs4.element import Comment #special type of NavigableString; add something extra to the string (comment has special formatting in an HTML document)
from string import ascii_lowercase #all lowercase letters (a-z), value is not locale-dependent and won't change
import random #implements pseudo-random number generators for various distributions

# This is a function that takes in a URL and returns it if evaluates true, in the sense that the URL
# is qualified=it is a complete URL with network location=has enough information to be reachable; else the
# function returns a URL joined with a base (start) if evaluates false
def ensure_absolute(url):
    if bool(urllib.parse.urlparse(url).netloc): #needs to evaluate true
        return url #returns the inputted URL if it meets the requirements described above
    else:
        return urllib.parse.urljoin(start,url)

# This is a function that accepts one or more urls as a parameter and returns a list of good urls. Good
# urls are considered qualified by the following: have been evaluted by the ensure_absolute function,
# have the same network location as the base url, match a wikipedia path, and have an empty query, fragment,
# and param. It breaks the url into its 6 components via the urlparse function. This allows for a more
# robust use of the url. If the url components meet certain requirements, then it is added to the list of
# urls. 
def ensure_urls_good(urls):
    result = [] #empty list initialized for possible 'good' urls
    basenetloc = urllib.parse.urlparse(start).netloc #store network location of the base url
    for url in urls: #loop trhough each url from urls and break them down into their 6 components
        url = ensure_absolute(url)
        path = urllib.parse.urlparse(url).path
        netloc = urllib.parse.urlparse(url).netloc
        query = urllib.parse.urlparse(url).query
        fragment = urllib.parse.urlparse(url).fragment
        param = urllib.parse.urlparse(url).params
        #assure these conditions are met and add qualifying urls to the result list
        if (netloc == basenetloc and re.match(r'^/wiki/', path) and query == '' and fragment == '' and param == ''):
            result += [url]
    return result #return the list of urls

# This is a function that makes a URL request and returns the page source as a string
# Note that we are setting a commonly used header called user-agent to a commonly set value
# This is because many popular webservers check the user-agent as a basic way to filter out crawlers or spambots
def getsource(url):
    req=urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}) #sends GET request to URL
    uClient=urllib.request.urlopen(req) #make urlopen calls
    page_html=uClient.read() #reads returned data and puts it in a variable
    uClient.close() #close the connection
    page_soup=BeautifulSoup(page_html,"html.parser") #applying BS to the obtained HTML
    return [page_soup, page_html]

# This is a function that accepts pagesoup as input, which is the HTML parsed text using Beautiful Soup.
# An empty list is initialized. The function loops through each anchor in pagesoup by finding tags, then
# adds 'href' to the result list. The list is updated to the result list after being evaluated by the 
# ensure_urls_good function, and then the list is returned.
def getanchors(pagesoup):
    result = [] #initialize list
    #loop through all 'a' anchors and update the result list to include 'href' info
    for anchor in pagesoup.find('div', {"id":'bodyContent'}).findAll('a'):
        result += [anchor.get('href')]
    result = ensure_urls_good(result) #perform function described above and then return the result
    return result

# This is a function that takes an element as a parameter and determines if the element is part of a
# specific parent class or Comment. If it's not then the element has a visible tag, which will need to be
# removed when parsing the text.
def tag_visible(element):
    #checks if the parent name of element is one in the list, returns false if it matches
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    #checks if the element is a Comment and if true, the if statement will return false
    if isinstance(element, Comment):
        return False
    return True

# This is a function that accepts the read data and parses using Beautiful Soup. The unfiltered text data
# is stored in a variable called texts, and then text is stored in another variable minus the visible tags.
# The function returns the text joined after stripping the extra whitespace from the front and back.
def text_from_html(page_html):
    soup = BeautifulSoup(page_html, 'html.parser') #parse the page using BS
    texts = soup.findAll(text=True) #find all text from that page
    visible_texts = filter(tag_visible, texts)  #filter out the visible tags from the parsed text
    return u" ".join(t.strip() for t in visible_texts) #return the text

# This is a function that counts the number of times each letter shows up in texts. The letters and their
# corresponding counts are stored in a dictionary, which is returned after it traverses the alphabet.
def count_letters(texts):
    alphabet = {} #intialize empty dictionary
    #loop through every lowercase letter a-z
    for letter in ascii_lowercase:
        alphabet[letter] = texts.count(letter) #count the number of times each letter appears and add to the dictionary
    return alphabet #return dictionary

# This is a function that accepts texts and the desired number of ngrams as parameters. After looping through
# all pattern matches in text, the conditional statements create a list of ngram word pairs that is updated
# to a dictionary and then returned. *Think bigrams in this example, however we could change n to be any
# other value*
def count_ngrams(texts, n):
    ngrams = {} #initialize empty dictionary
    grams = [] #initialize empty list
    pattern = re.compile(r'\[\w+\]|([a-zA-Z]+\'{0,1}[a-zA-Z]+)') #store regex pattern to match
    #iterates through all instances where pattern is found in texts
    for m in re.finditer(pattern, texts):
        #makes sure the last group is not equal to 'None' aka something was found
        if (str(m.group(1)) != 'None'):
            # If the length of the list grams is less than the desired_ngram_level (n=2), then add the last
            # match of string m to the list grams
            if (len(grams) < n):
                grams += [m.group(1)]
            # When the length of the list grams exceeds the desired_ngram_level, join the list grams to a 
            # string called ngram (separated by a space). Then if an ngram is found in the dictionary ngrams,
            # update the count by one for this ngram. In the case where an ngram is not found in ngrams,
            # initialize it with a count of one. Slice off index 0 in grams and then add the next match.
            else: 
                ngram = ' '.join(grams); #assign the two matches to a string variable separated by a space
                # If the dictionary ngrams already contains the string ngram, then update the key ngram
                # value by 1. If this is the first time seeing the string ngram, assign the key ngram a
                # value of 1. After the conditional statements, slice the first entry off grams list and
                # add the next match to the grams list.
                if (ngram in ngrams):
                    ngrams[ngram] = ngrams[ngram]+1
                else:
                    ngrams[ngram] = 1
                grams = grams[1:] #remove the first match from grams (match at index 1 is now at index 0)
                grams += [m.group(1)] #add the next match to grams (index 1)
    return ngrams #returns a dictonary with the ngram:count as the key:value pairs

# This is a function that combines key:value pairs for dictionary 1 and dictionary 2. The function loops
# through all keys in either dict1 or dict2 and .get function grabs the value associated with each key,
# adds them together (0 is default if key is not in dictionary, since dictionaries might not contain the
# same items), and stores them to a new result dictionary for each key.
def combinedicts(dict1,dict2):
    result = { k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2) }
    return result

# This is a function that writes the dictionary to a csv file. The function accepts a dictionary, header,
# and data. After opening the file, it writes the headers followed by a newline. Then it loops through
# each item in reverse sorted order and writes the item and data associated with the item to csv, followed
# by a newline. The file then closes.
def write_dict_to_csv(fname,header,data):
    f=open(fname,'w') #open the file, and begin writing
    f.write(header) #write the headers
    f.write('\n') #write a newline
    #loop through every item in reverse sorted order
    for item in sorted(data, key=lambda i: int(data[i]), reverse=True):
        f.write(str(item)+','+str(data[item])) #write the name of the item and the data for that item
        f.write('\n') #writes a newline
    f.close() #close the file
    return

# This is a function that accepts a parameter for a url link and the number of pages to crawl. This function
# implements most of the functions defined in this example. It loops through the number of times specified,
# by the limit parameter, and performs conditional statements in order to create two dictionaries. These
# dictionaries contain the letter frequencies and ngram frequencies, which will be returned as a list at
# the end of the loop.
def crawl(url, limit):
    result1 = {}
    result2 = {}
    pagedata = getsource(url) #returns the page source as a string for url and assigns to a variable called pagedata
    anchors = getanchors(pagedata[0]) #assigns all the 'a href' anchors to a variable called anchors 
    #loops through all pages 
    for i in range(0,limit):
        secure_random = random.SystemRandom() #generates random numbers from sources provided by the operating system
        random_url = secure_random.choice(anchors) #return a random element from anchors and assigns to a variable called random_url
        pagedata = getsource(random_url) #returns the page source as a string for the random_url chosen and assigns to a variable called pagedata 
        texts = text_from_html(pagedata[1]).lower() #stores the filtered pagedata (from text_from_html function defined above) and case normalizes all the text
        letterfreqs = count_letters(texts) #stores the letter frequencies of the texts parameter
        ngramfreqs = count_ngrams(texts, desired_ngram_level) #stores the ngrams frequencies
        anchors = getanchors(pagedata[0]) #assigns all the 'a href' anchors to a variable called anchors
        # First time through evalautes the else statement, which assigns the letterfreqs and ngramfreqs
        # to the empty result1 and result2 dictionaries, respectively. After that, the if statement is
        # evaluated and the combinedicts function is called upon to essentially update the previously
        # stored data (freqs of letters and ngrams) to contain the new data also.
        if len(result1) > 1: #once dict has at least one entry
            result1 = combinedicts(result1,letterfreqs)
        else: #first instance
            result1 = letterfreqs
        if len(result2) > 1: #once dict has at least one entry
            result2 = combinedicts(result2,ngramfreqs)
        else: #first instance
            result2 = ngramfreqs
    return [result1, result2] #return a list containing both dictionaries

# The base URL for the web scraping
start="https://en.wikipedia.org/wiki/Special:Random"

# Assign the number of pages to crawl, will be used as the limit in the crawl function
pagestocrawl = 20

# Assign the number of ngram levels, will be used as the n in count_ngrams function
desired_ngram_level = 2

# Assigns a list of dictionaries to freq variable
freqs = crawl(start,pagestocrawl) #contains the letterfreqs and ngramfreqs
write_dict_to_csv('letter_freqs.csv','letter,frequency',freqs[0]) #writes the letter frequencies to csv file
write_dict_to_csv('ngram_freqs.csv','ngram,frequency',freqs[1]) #writes the ngram frequencies to csv file
