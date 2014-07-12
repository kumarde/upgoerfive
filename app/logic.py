import nltk
from nltk.corpus import wordnet as wn
from collections import deque

WORDS = set()

def set_words(filename):
  WORDS = set(line.strip() for line in open(filename))

def app_logic(sentence):
  new_word_list = [explore_syn_tree(word) for word in sentence.split(' ')]
  return ' '.join(new_word_list)

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
	#Some handling logic
	return "thing"

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
        if count == 10000:
            break
    return None


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
        if count == 10000:
            break
    return None

# if __name__ == '__main__':
#  	WORDS = generate_words('../words/1000base.txt')
#  	print "we are the best hackers in the nation"
#  	print app_logic("we are the best hackers in the nation")
#  	print "will code for food"
#  	print app_logic("will code for food")
#  	print "trains are hilarious at night"
#  	print app_logic("trains are hilarious at night")
#  	print "the subway is the best place to find cold pizza"
#  	print app_logic("the subway is the best place to find cold pizza")
#  	print "dawn of the planet of the apes"
#  	print app_logic("dawn of the planet of the apes")
#  	print "breaking bad is the best television show to ever exist"
#  	print app_logic("breaking bad is the best television show to ever exist")
#  	print "et phone home"
#  	print app_logic("et phone home")
#  	print "this was a lot of fun"
#  	print app_logic("this was a lot of fun")
#  	print "comedy is the essence of humor"
#  	print app_logic("comedy is the essence of humor")
