'''
Text Mining Softdes2015 Mini Project #3
Author: Zarin Bhuiyan

-----------
This program trains a kNN classifier to recognize adjectives taken from Twitter. 
Adjectives are classified and identified as #win or #fail.
The adjective vectors are put in a corpus to train the classifier.
"damn" and "sucks" are classified as #fail & "awesome" and "cool" are classified as "win"
Results vary according to real-time tweets.

'''



from pattern.web import Twitter
from pattern.en import Sentence, parse
from pattern.search import search
from pattern.vector import Document, Corpus, KNN



corpus = Corpus()   #collection of texts

for i in range (1,15):
	for tweet in Twitter().search('#win' or '#fail', start=i, count =100): #searches 15*100=1500 tweets for these classes of hashtags
		p = '#win' in tweet.description.lower() and 'WIN' or 'FAIL'
		m = '#fail' in tweet.description.lower() and 'WIN' or 'FAIL'
		s = tweet.description.lower()
		s = Sentence(parse(s))  #parse anlayzes & gives strings that are annotated with specified tags
		s = search('JJ',s) #searches for adjectives in tweets (JJ = adjectiive)
		s = [match[0].string for match in s]
		s=' '.join(s)
		if len(s)>0:
			corpus.append(Document(s,type=p))
			corpus.append(Document(s,type=m))


classifier = KNN() #k-nearest neighbor classifier = K-NN
objects = []

for document in corpus: #documents are an unordered bag of given sentences.

	classifier.train(document) #adjective vectors in corpus trains the classifier 
	objects.append(classifier.classify('awesome')) #predicts awesome as win
	objects.append(classifier.classify('cool')) #predicts cool as win
	objects.append(classifier.classify('damn')) #predicts damn as fail
	objects.append(classifier.classify('sucks')) #predicts sucks as fail

print objects
wincounter = 0
failcounter = 0
for thing in objects:
		if thing == 'WIN':
			wincounter += 1
		elif thing == 'FAIL':
			failcounter += 1
		else:
			pass


print "wins =", wincounter
print "fails =",failcounter


ratio = float(wincounter)/float(failcounter)
print "ratio of wins to fails = ",ratio

	
	

