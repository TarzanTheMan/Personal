import nltk
#nltk.download_gui()

from nltk.book import *
text1

#contextual based functions
text1.concordance('whale') #show me where 'whale' exists in text1
text1.similar('whale') #show 'similar' terms (based entirely on collocation/adjacency)

#graphical lexical analysis
text4.dispersion_plot(['citizens','democracy','freedom','duties','America'])

#counting and sorting tokens
len(text3) #count all the tokens ('word' is the default token in an NLTK text object)
sample_text="data data data data"
len(sample_text) #character is the default token in a string object
sample_text=['data','data','data','data']
len(sample_text) #list uses 'word' as default token
len(set(sample_text)) #set() gives unique tokens;
set(text3) #all unique words for text3
len(set(text3)) #number of unique words out of total number of words in text3
len(set(text3))/len(text3) #ratio of unique words to total words; measure of lexical richness/diversity

#more lexical characteristics
len(text1)
len(set(text1))
fdist1=FreqDist(text1) #calculate frequency distribution of terms
print(fdist1)
fdist1.most_common(50) #print tuple of the 50 most comomonly used words and their count
fdist1.plot(100, cumulative=True) #plot cumulatively the most frequent 100 tokens
fdist1.plot(100 )#plot NOT cumulatively the most frequent 100 tokens
fdist1.hapaxes() #words that only show up once
len(fdist1.hapaxes()) #number of words that only appear once

#list comprehension
long_words=[w for w in text1 if len(w)>15] #return word for words in text1 if length of word is greater than 15
print(long_words)
sorted(long_words) #alphabetically sorted
sorted(set(long_words)) #alphabetically sorted words not repeated
sorted(w for w in set(text1) if len(w)>7 and fdist1[w]>50) #return unique word for unique words in text1 if conditions hold

from nltk.corpus import gutenberg
from nltk.corpus import shakespeare

nltk.corpus.gutenberg.fileids() #show files in the collection
nltk.corpus.shakespeare.fileids()

hamlet=nltk.corpus.gutenberg.words('shakespeare-hamlet.txt') #list of words
macbeth=nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')
hamlet_sentences=nltk.corpus.gutenberg.sents('shakespeare-macbeth.txt') #each sentence is a list of words
hamlet_all=nltk.corpus.gutenberg.raw("shakespeare-macbeth.txt") #entire text
print(hamlet)
print(hamlet_sentences)
print(hamlet_all)

#bringing in your own text in as an NLTK text object
from nltk.corpus import PlaintextCorpusReader
dir='C:/Users/adam_/Documents/MSDA/Data Foundations/'
file='IS6713_syllabus.txt'
syllabus=PlaintextCorpusReader(dir,file)
syllabus.words() #ERROR

#conditional frequency distributions provide handy tables and plot
from nltk import ConditionalFreqDist as CFD
cfd=CFD((fileid, len(word)) for fileid in shakespeare.fileids() \
        for word in shakespeare.words(fileid)[:20000] if len(word)>3)
#loop through each file in the Shakespeare collection and return the frequency distribution for words greater than
#3 characters long for each file truncating each file after the first 20,000 words
cfd.tabulate()
cfd.plot()
cfd[u'a_and_c.xml'] #'u' indicates unicode parsing of the source file

from nltk.corpus import stopwords #Brown stopword list
stopwords.words('english') #note all stopwords are lowercase

from nltk.tokenize import word_tokenize
sentence="This is an example showing off stop word filtration"
stopwords=set(stopwords.words('english'))
words=word_tokenize(sentence)
print(words)
filtered_sentences=[] #intialize an empty list into which we'll put our stoplist filter
for w in words:
    if w not in stopwords:
        filtered_sentences.append(w)
print(filtered_sentences)

#stemming
from nltk.stem import PorterStemmer
ps=PorterStemmer()
example_words=['deliver','delivering','delivered']
for w in example_words:
    print(ps.stem(w))























