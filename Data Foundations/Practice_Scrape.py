from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

#now let's scrape the web page
uClient=uReq(my_url) #sends GET request to URL 
page_html=uClient.read() #reads returned data and puts it in a variable
uClient.close() #close the connection

#let's create a file that we will want later to write parsed data to
filename="products.csv"
f=open(filename, 'w')
headers="brand, product_name, shipping\n"
f.write(headers)

#now for the good stuff..let's use BS to parse the webpage
page_soup=soup(page_html,'html.parser') #applying BS to the obtained html
#but this is useless in and of itself. It doesn't print or do anything
#it just reads and parses the HTML tree structure and "knows" what tages are where
print(page_soup.h1)
print(page_soup.p)
print(page_soup.body.span)
print(page_soup.body.div.div)

containers=page_soup.findAll('div',{'class','item-container'})
#print(containers[0])

for container in containers:
    brand=container.div.div.a.img['title'] #traverses down the html tree in BS object to the 'title' attribute in the image tag
    container_title=container.findAll('a',{'class','item-title'})
    product_name=container_title[0].text #.text gets the element text or element content
    container_shipping=container.findAll('li',{'class','price-ship'})
    shipping=container_shipping[0].text.strip()
    
    #to print to screen
    print('brand:'+brand)
    print('product_name:'+product_name)
    print('shipping:'+shipping)
    
    #to write to csv
    f.write(brand+','+product_name.replace(",",";")+','+shipping+'\n')
    
f.close()
