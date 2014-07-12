import nltk
from nltk.corpus import wordnet as wn

def app_logic():


def check_in_1000_words(word):
	pass

def explore_syn_tree(word, pos=None):
	synsets = None
	posSet = False
	if pos is None:
		synsets = wn.synsets(word)
	else:
		synsets = wn.synsets(word, pos=pos)
		posSet = True
	for synset in synsets:
		matching_hypernym = explore_hypernyms(synset)
		if(matching_hypernym != None):
			return matching_hypernym
		matching_hyponym = explore_hyponyms(synset)
		if(matching_hyponym != None):
			return matching_hyponym
	#Some handling logic
	return "Abhishek"

def explore_hyponyms(syn):
	pass

def explore_hypernyms(syn):
	



