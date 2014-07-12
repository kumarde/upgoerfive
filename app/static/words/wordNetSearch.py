from nltk.corpus import wordnet as wn

#Example of all sets for a specific word
bearSynSet = wn.synsets('bear')
print "This is an example of bear synsets:"
print bearSynSet

#Example of words that include the word bear as a "POS"
nounBearSynSet = wn.synsets('bear', pos=wn.NOUN)
print "This is an example of bear noun synsets"
print nounBearSynSet

#Dive into a specific synset
bear = wn.synset('bear.n.01')
print "These are the hypernyms (above) of bear"
bearHypernyms = bear.hypernyms()
print bearHypernyms
print "These are the hyponyms (below) of bear"
bearHyponyms = bear.hyponyms()
print bearHyponyms

#Print all the synsets
for synset in list(wn.synsets('bear')):
	print type(synset)
	#bear = wn.synset(synset)
	#bearHypernyms = bear.hypernyms()
	#bearHyponyms = bear.hyponyms()
	#print bearHypernyms
	#print bearHyponyms
