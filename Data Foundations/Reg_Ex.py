import re #import regular expression package
 
pattern=re.compile('[a-z]+') #creates a compiled regex object
print(pattern.match("")) #returns nothing because there are no alphas in ""
print(pattern.match("tempo")) #returns 'hit' on 'tempo' (see greediness - gets longest string match possible)
m=pattern.match('tempo')
m.group()
m.start()
m.end()
m.span()
 
print(pattern.match('::: message'))
m=pattern.search('::: message')
print(m)
m.group()
m.span()
 
#common uses in program
pattern=re.compile('pattern goes here')
m=pattern.search('string to search')
if m:
    print('Match found: ',m.group())
else:
    print('No match found.')
 
pattern=re.compile('to')
m=pattern.search('string to search')
if m:
    print('Match found: ',m.group())
else:
    print('No match found.')
 
#findall example
pattern=re.compile('\d+') #want to find one or more digits
pattern.findall('12 drummers drumming, 11 pipers piping, 100 lords-a-leaping')
 
iterator=pattern.finditer('12 drummers drumming, 11 pipers piping, 100 lords-a-leaping')
for match in iterator:
    print(match.span())
 
#can call top-level functions directly calling the re module
print(re.match('From\s','Fromage amk')) #prints None because looking for 'From' followed by whitespace
print(re.fullmatch('string','longstring')) #retuns None because pattern is in string, but pattern isn't the full string
 
#can also substitute
print(re.sub('\.0+','.','192.168.08.011')) #want to get rid of leading zeroes
 
#can also split
print(re.split('[\s,:]',"Eggs,bacon toast:OJ")) #splits on multple things
