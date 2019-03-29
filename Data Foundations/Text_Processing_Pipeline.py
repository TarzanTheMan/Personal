import nltk
from nltk.book import *
from nltk.corpus import gutenberg
from nltk import word_tokenize
 
#tokenizing
nltk.corpus.gutenberg.fileids()
macbeth_tok=gutenberg.words('shakespeare-macbeth.txt') #token=word level
len(macbeth_tok)
macbeth_sent=gutenberg.sents('shakespeare-macbeth.txt') #token=sentence level
len(macbeth_sent)
 
#more complex tokenization
from nltk.tokenize import sent_tokenize, word_tokenize
example_text="Hello Mr. Smith, How are you doing today? The weather is great and Python is awesome. They sky is pinkish blue. You should not eat cardboard."
print(sent_tokenize(example_text))
print(word_tokenize(example_text))
print(nltk.wordpunct_tokenize(example_text))
 
import os
import math
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from scipy import spatial
 
#open/read docs
os.chdir("C:/Users/adam_/Documents/MSDA/Data Foundations/")
frank=open('frank.txt').read()
 
#tokenize (word-level)
frank_tok=word_tokenize(frank) #tokenize Frank and store in list called frank_tok
tokens=len(frank_tok) #how many "words" are in this text? (note, words here includes punctuation)
unique=len(set(frank_tok)) #how many UNIQUE words?
print('Total tokens:',tokens)
print('Total unique tokens:',unique)
 
lexical_diversity=unique/tokens
print('Lexical diversity:',lexical_diversity)
print('Number of periods in Frank:',frank_tok.count('.')) #how many periods are in the text
print('Number of "The" in Frank:',frank_tok.count('The'))
print('Number of "the" in Frank:',frank_tok.count('the'))
 
#Case normalization
frank_tok_norm=[w.lower() for w in frank_tok if w.isalnum()] #convert all alpahnumerics to lowercase
print('Number of periods in Frank:',frank_tok_norm.count('.')) #how many periods are in the text
print('Number of "The" in Frank:',frank_tok_norm.count('The'))
print('Number of "the" in Frank:',frank_tok_norm.count('the'))
tokens=len(frank_tok_norm)
unique=len(set(frank_tok_norm))
print('Total tokens after case normalization:',tokens)
print('Total unique tokens after case normalization:',unique)
 
#apply stoplist (stopword removal)
stop=set(stopwords.words('english')) #create list of english of stopwords
frank_tok_norm_stop=[] #initialize a new list for stoplist'd token list
for w in frank_tok_norm: #add only word from previous frank list that aren't stopwords
    if w not in stop:
        frank_tok_norm_stop.append(w)
tokens=len(frank_tok_norm_stop)
unique=len(set(frank_tok_norm_stop))
print('Total tokens after case normalization and stoplist:',tokens)
print('Total UNIQUE tokens after case normalization and stoplist:',unique)
 
#apply stemming algorithm (or lemmatization) (common algorithms: Porter, Lancaster)
porter=nltk.PorterStemmer()
frank_tok_norm_stop_stem=[porter.stem(w) for w in frank_tok_norm_stop]
tokens=len(frank_tok_norm_stop_stem)
unique=len(set(frank_tok_norm_stop_stem))
print('Total tokens after case norm, stoplisting, stemming:',tokens)
print('Total UNIQUE tokens after case norm, stoplisting, stemming:',unique)
 
#Sidenote / example of feature vector similary measurement
vec1=[3,57]
vec2=[2,54]
vec3=[1,1]
cos_vec1_vec2=spatial.distance.cosine(vec1,vec2)
cos_vec2_vec3=spatial.distance.cosine(vec2,vec3)
cos_vec1_vec3=spatial.distance.cosine(vec1,vec3)
print('Dist1_2 ',cos_vec1_vec2)
print('Dist2_3 ',cos_vec2_vec3)
print('Dist1_3 ',cos_vec1_vec3)
 
#For your homework, you'll be creating matrices (binary matrix, TF matrix, TF-norm matrix, TF-IDF matrix)
#So you'll need to access vectors (rows) from respective matrices
 
#create binary feature space vector (really only one in this case)
#this is stupid to do when only have one doc, but sets you up for your homework
lexicon=set(frank_tok_norm_stop_stem) #set of unique terms in Frank
#in your homework, lexcion needs to be the superset of all unique terms in all docs
lexicon_dim=len(lexicon) #what is n in t_n (how many terms?)
termvect_binary_terms=[] #initializing term vector for lexicon (header row)
termvect_binary_frank=[] #initializing the binary vector for Frank
for c in lexicon:
    termvect_binary_terms.append(c) #this is going to create our header row
    if c in frank_tok_norm_stop_stem:
        termvect_binary_frank.append(1) #check if t_x is in Frank, if yes, value=1
    elif c not in frank_tok_norm_stop_stem:
        termvect_binary_frank.append(0) #else then value=0
print(termvect_binary_frank)
 
#create BINARY feature vector MATRIX (header plus the Frank feature vector)
count=0
matrix_binary=[[0 for c in range(lexicon_dim)] for r in range(2)] #range depends on number of rows (docs) dealing with; plus header
for c in lexicon:
    matrix_binary[0][count]=c
    if c in frank_tok_norm_stop_stem:
        matrix_binary[1][count]=1
    count=count+1
print(matrix_binary)
 
#create RAW TERM FREQUENCY matrix
count=0
matrix_TF=[[0 for c in range(lexicon_dim)] for r in range(2)]
for c in lexicon:
    matrix_TF[0][count]=c
    matrix_TF[1][count]=frank_tok_norm_stop_stem.count(c) #count number of times word 'c' is in list
    count=count+1
print(matrix_TF)
 
'''Now you create the rest of the matrices
Advice/hints: 
TF_norm ... value is count/total tokens (after norm, stoplist, stemming)
TF-IDF ... value is TF * IDF
'''
#for IDF you have to create an IDF vector
vector_idf=[] #initialize IDF vector
for i in range(lexicon_dim): #run through loop for each token in lexicon
    df=0 #df=doc frequency this is like n_t ... number of docs that term exists in
    if matrix_binary[1][i]==1: #[1] = doc1
        df=df+1
    #going to need to add more if loops to detect matrix_binary[2][i]==1
    # and matrix_binary[3][i]==1
    # and add them together
    idf=math.log(1/(df)) #1 is N (the number of docs, or number of rows in matrix minus header)
    #Do log(N/(1-n_t)) to avoid divide by zero error
    vector_idf.append(idf)
vector_idf
 
#again... modify code to handle multiple docs
 
#cos_text1_text2=spatial.distance.cosine(matrix_TFIDF[1],matrix_TFIDF[2])
























