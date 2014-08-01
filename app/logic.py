import nltk
import random
import inflect
from pattern.en import conjugate, tenses, singularize
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
from collections import deque
from textblob import TextBlob
from textblob.wordnet import *
from textblob import Word

class SimpleSentenceGenerator:
  def __init__(self, filename):
    self.words = set(line.strip() for line in open(filename))
    self.tagged_words = [TextBlob(word).tags for word in self.words]
    self.inflect_engine = inflect.engine()

  def test_logic(self, sentence):
    blob = TextBlob(sentence)
    new_word_list = [self.explore_syn_tree(wTuple, self.get_wordnet_pos(wTuple[1])) for wTuple in blob.tags]
    return ' '.join(new_word_list)

  def app_logic(self, sentence):
    new_word_list = [self.explore_syn_tree(word) for word in sentence.split(' ')]
    return ' '.join(new_word_list)

  def check_in_words(self, word):
    return bool(word in self.words)

  def explore_syn_tree(self, word_tuple, pos=None):
    if self.check_in_words(word_tuple[0]):
      return word_tuple[0]
    if word_tuple[0] == "difficult":
      return "hard"
    if word_tuple[0] == "saturn":
      return "up goer"
    if word_tuple[0] == "simple":
      return "easy"
    if word_tuple[0] == "shady":
      return "unusual"
    if word_tuple[0] == "questionable":
      return "shady"
    synsets = None
    posSet = False
    if pos is None:
      synsets = wn.synsets(word_tuple[0])
    else:
      synsets = wn.synsets(word_tuple[0], pos=pos)
      posSet = True
    for synset in synsets:
      matching_hypernym = self.explore_hypernyms(synset)
      if matching_hypernym != None:
        if(pos == wordnet.NOUN):
          if(self.is_plural(word_tuple[0])):
            #The word is a plural, yo.
            return self.inflect_engine.plural(matching_hypernym)
        if(pos == wordnet.VERB):
          pattern_tag = self.get_pattern_tense(word_tuple[1])
          person = 1
          if word_tuple[1] == "VBZ":
            person = 3
          matching_hypernym = conjugate(matching_hypernym, tense=pattern_tag, person=person, parse=True)
          return matching_hypernym
        return matching_hypernym
      matching_hyponym = self.explore_hyponyms(synset)
      if matching_hyponym != None:
        if(pos == wordnet.NOUN):
          if(self.is_plural(word_tuple[0])):
            #The word is a plural, yo.
            return self.inflect_engine.plural(matching_hyponym)
        if(pos == wordnet.VERB):
          pattern_tag = self.get_pattern_tense(word_tuple[1])
          person = 1
          if word_tuple[1] == "VBZ":
            person = 3
          matching_hypornym = conjugate(matching_hyponym, tense=pattern_tag, person = person, parse = True)
          return matching_hyponym
        return matching_hyponym
    #Some handling logic
    wn_pos = word_tuple[1]
    possible_solutions = set()
    for tagged_tuple in self.tagged_words:
      if wn_pos == tagged_tuple[0][1]:
        possible_solutions.add(tagged_tuple[0][0])
    return random.sample(possible_solutions, 1)[0]
     
  def explore_hyponyms(self, syn):
      count = 0
      queue = deque()
      visited = set()
      queue.append(syn)
      visited.add(syn)
      
      while queue:
          current = queue.popleft()
          print "hyponym"
          print current
          if self.check_in_words(str(current.lemmas[0].name)):
            return str(current.lemmas[0].name)
          for child in current.hyponyms():
            for similar in current.similar_tos():
              if child not in visited:
                  visited.add(child)
                  queue.append(child)
                  count += 1
              if similar not in visited:
                visited.add(similar)
                queue.append(similar)
                count += 1
      return None

  def explore_hypernyms(self, syn):
      count = 0
      queue = deque()
      visited = set()
      queue.append(syn)
      visited.add(syn)
      
      while queue:
          current = queue.popleft()
          print current
          if self.check_in_words(str(current.lemmas[0].name)):
              return str(current.lemmas[0].name)
          for child in current.hypernyms():
            if child not in visited:
              visited.add(child)
              queue.append(child)
              count += 1
      return None

  def get_wordnet_pos(self, treebank_tag):
    if treebank_tag.startswith('J'):
      return wordnet.ADJ
    elif treebank_tag.startswith('V'):
      return wordnet.VERB
    elif treebank_tag.startswith('N'):
      return wordnet.NOUN
    elif treebank_tag.startswith('R'):
      return wordnet.ADV
    else:
      return None

  def get_pattern_tense(self, treebank_tag):
    treebank_tag = treebank_tag.encode('ascii', 'ignore')
    if treebank_tag == "VB":
      return "present"
    elif treebank_tag == "VBD":
      return "past"
    elif treebank_tag == "VBG":
      return "presentparticiple"
    elif treebank_tag == "VBN":
      return "pastparticiple"
    elif treebank_tag == "VBP":
      return "present"
    elif treebank_tag == "VBZ":
      return "present"

  def is_plural(self, pluralForm):
    singularForm = singularize(pluralForm)
    plural = True if pluralForm is not singularForm else False
    return plural

# if __name__ == '__main__':
#   WORDS = generate_words('../words/1000base.txt')
#   print "we are the best hackers in the nation"
#   print app_logic("we are the best hackers in the nation")
#   print "will code for food"
#   print app_logic("will code for food")
#   print "trains are hilarious at night"
#   print app_logic("trains are hilarious at night")
#   print "the subway is the best place to find cold pizza"
#   print app_logic("the subway is the best place to find cold pizza")
#   print "dawn of the planet of the apes"
#   print app_logic("dawn of the planet of the apes")
#   print "breaking bad is the best television show to ever exist"
#   print app_logic("breaking bad is the best television show to ever exist")
#   print "et phone home"
#   print app_logic("et phone home")
#   print "this was a lot of fun"
#   print app_logic("this was a lot of fun")
#   print "comedy is the essence of humor"
#   print app_logic("comedy is the essence of humor")
