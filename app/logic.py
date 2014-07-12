import nltk
from nltk.corpus import wordnet as wn

def app_logic():
	pass
WORDS = set()

def generate_words(filename):
  return set(line.strip() for line in open(filename))

def app_logic():
  pass

def check_in_words(word):
  return word in WORDS 

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
	print "Abhishek"
	return "Abhishek"

def explore_hyponyms(syn):
	return None

def explore_hypernyms(syn):
	return None

#if __name__ == '__main__':
