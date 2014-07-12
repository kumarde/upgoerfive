import nltk
from nltk.corpus import wordnet as wn
from collections import deque

WORDS = set()

def generate_words(filename):
  return set(line.strip() for line in open(filename))

def app_logic(sentence):
	sentence_split = sentence.split(" ")
	new_word_list = sentence_split
	for word in sentence_split:
			


def check_in_words(word):
  return bool(word in WORDS)

def explore_syn_tree(word, pos=None):
	if check_in_words(word):
	  return word

	synsets = None
	posSet = False
	if pos is None:
		synsets = wn.synsets(word)
	else:
		synsets = wn.synsets(word, pos=pos)
		posSet = True
	for synset in synsets:
		matching_hypernym = explore_hypernyms(synset)
		if matching_hypernym is not None:
			return matching_hypernym
		matching_hyponym = explore_hyponyms(synset)
		if matching_hyponym is not None:
			return matching_hyponym
	#Somed handling logic
	print "Abhishek"
	return "Abhishek"

def explore_hyponyms(syn):
    count = 0
    queue = deque()
    visited = set()
    queue.append(syn)
    visited.add(syn)
    
    while queue:
        current = queue.popleft()
	if check_in_words(str(current.lemmas[0].name)):
            return str(current.lemmas[0].name)
        for child in current.hyponyms():
            if child not in visited:
                visited.add(child)
                queue.append(child)
                count += 1
        if count == 10:
            break
    return "Debug12"


def explore_hypernyms(syn):
    count = 0
    queue = deque()
    visited = set()
    queue.append(syn)
    visited.add(syn)
    
    while queue:
        current = queue.popleft()
	if check_in_words(str(current.lemmas[0].name)):
            return str(current.lemmas[0].name)
        for child in current.hypernyms():
            if child not in visited:
                visited.add(child)
                queue.append(child)
                count += 1
        if count == 10:
            break
    return "Debug12"

if __name__ == '__main__':
	WORDS = generate_words('../words/1000base.txt')
	print explore_syn_tree("hi")
	print explore_syn_tree("complicated")
