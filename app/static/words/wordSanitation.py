import nltk

with open("1000base.txt") as f:
	content = f.readlines()

for word in content:
	token = nltk.word_tokenize(word)
	tag = nltk.pos_tag(token) #This will generate a part of speech for each token
	print tag

