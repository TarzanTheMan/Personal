#WordNet
#WordNet is a semantically-oriented dictionary of English, similar to a traditional thesaurus but with a richer structure. (source: NLTK book)
from nltk.corpus import wordnet as wn
wn.synsets('motorcar') #what are the synonyms of 'motorcar'? returns '[Synset('car.n.01')]' -- meaning motorcar is the 1st synonym of the car synset (set of synonyms)
wn.synset('car.n.01').lemma_names() #return the synonyms of 'car' ('lemma' = pairing of a synset with a name
wn.synset('car.n.01').definition() #return the definition for the 'car' synset
wn.synset('car.n.01').examples() #return example uses of the 'car' lemma
 
wn.synset('car.n.01').lemmas() #return all the lemmas associated with the 'car' synset
wn.lemma('car.n.01.automobile') #look up the 'automobile' synset
wn.lemma('car.n.01.automobile').synset() #return the synset associated with the 'automobile' lemma
wn.lemma('car.n.01.automobile').name() #return just the name of the lemma
wn.lemmas('car') #return a list of all the lemmas for a word
wn.lemmas('dish')
 
for synset in wn.synsets('car'):
    print(synset.lemma_names()) #prints just the lemma names (i.e. synonym words)
wn.lemmas('car') #prints the lemma sets in synset format
 
#understanding a concept by drilling down on the concept more (going down the wordnet hierarchy)
motorcar=wn.synset('car.n.01') #selecting a synset
motorcar_types=motorcar.hyponyms() #getting lower level concepts for that synset
motorcar_types[0] #printing out the first element in the lower level concept set (hyponym set)
sorted(lemma.name() for synset in motorcar_types for lemma in synset.lemmas()) #for each element in the motorcar hyponym set, and for each lema in that, print the lemma name -- so returns the synonyms for each lower-level neighbor of 'motorcar' -- provides fuller understanding of the 'motorcar' concept
 
#understanding a concept by going up the hierarchy
motorcar.hypernyms()
paths=motorcar.hypernym_paths()
len(paths)
[synset.name() for synset in paths[0]] #this hypernym path identifies a car as a CONTAINER OBJECT (instrumentality is_a container)
[synset.name() for synset in paths[1]] #this hypernym path identifies a car as a CONVENYANCE METHOD (instrumentality is_a conveyance
 
#concept similarity measures
#reference: http://www.nltk.org/howto/wordnet.html (similarity section)
wn.synsets('car')
wn.synsets('ambulance')
wn.synsets('elevator')
wn.synsets('frog')
wn.synsets('automobile')
car=wn.synset('car.n.01')
ambulance=wn.synset('ambulance.n.01')
elevator=wn.synset('elevator.n.01')
frog_noun=wn.synset('frog.n.01')
frog_verb=wn.synset('frog.v.01')
auto_noun=wn.synset('automobile.n.01')
auto_verb=wn.synset('automobile.v.01')
print(car.path_similarity(ambulance))
print(car.path_similarity(elevator))
print(car.path_similarity(frog_noun))
print(car.path_similarity(frog_verb))
print(car.path_similarity(auto_noun))
print(car.path_similarity(auto_verb))
print(car.wup_similarity(ambulance)) #just a different similarity measure, but still concept hierarchy based metric
 
#concept similarity measures in NLTK
#metrics based similarity measures -- those that only use concept hierarchy path-based measures
    #path_similarity, Leacock-Chodorow Similarity, Wu-Palmer (WUP) Similarity
#metrics that also incorporate corpus based probability distribution measures
    #Resnik Similarity, Jiang-Conrath Similarity, Lin Similarity
 
wn.synset('ambulance.n.01').min_depth() #min_depth() shows how general (smaller number, closer to root node) or specific (larger number, X nodes away from root node) a concept is
wn.synset('car.n.01').min_depth()
wn.synset('vehicle.n.01').min_depth()
wn.synset('entity.n.01').min_depth()
 
#Lemmatization
#Conceptually similar to stemming, but result is a real world (not a truncated, non-word); lemmatized word may be a synonym, not necessarily the root word; result is more sensical dimensions
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize('deliver')) #notice the 'root' is more sensical ('deliver' vs. 'deliv')
print(lemmatizer.lemmatize('delivering')) #same here
 
print(lemmatizer.lemmatize('cats')) #this is a better example of what we think of as stemming, but with sensical root
print(lemmatizer.lemmatize('cacti')) #same here