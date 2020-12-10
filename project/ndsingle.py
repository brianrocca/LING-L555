import sys
import eng_to_ipa as ipa
from Levenshtein import*
#open and read lines in file
filename = "minpairs.txt"
f = open(filename,"r")
input = f.readlines()
f.close()
#dictionaries/variables
IPAtoken = []
words = {}
pairs = {}
#Tokenize words in file
for c in input:
	lista = c.replace('.', ' ').replace(',', ' ').replace('?', ' ').replace('!', ' ')
	lista = lista.replace(';', ' ').replace(':', ' ').replace(')', ' ').replace('-', ' ')
	lista = lista.replace('(', ' ').replace('"', ' ').replace('/', ' ').replace('\n', ' ')
	lista = lista.replace('_', ' ').replace('<', ' ').replace('  ', ' ').replace('>', ' ')
	lista = lista.split(' ')
	lista_no_empty = [x for x in lista if x != '']
	#Transcribe words into IPA
	for token in lista_no_empty:
		IPAtoken = ipa.convert(token)
		#store each orthographic form
		if IPAtoken not in words:
			words[IPAtoken] = []
		words[IPAtoken].append(token)
#compute levenshtein_distance
for word1 in words:
	for word2 in words:
		if distance(word1, word2) <= 1:
			if word1 not in pairs:
				pairs[word1] = []
			pairs[word1].append(word2)
#Graph phonological neighborhood of word in terminal command
import networkx as nx
import matplotlib.pyplot as plt
#convert command line to IPA
k = ipa.convert(sys.argv[1])
#graph
G = nx.Graph()
f = plt.figure()
# For each related word
for vv in pairs[k]:
	# For each of the orthographic forms
	for ww in words[vv]:
		# For each of the orthographic forms
		for kk in words[k]:
			G.add_edge(kk,ww)
nx.draw(G,
	with_labels=True,
	node_color='blue',
	node_size=1600,
	font_color='white',
	font_size=12,
                )
f.savefig('ndgraph_' + sys.argv[1] + '.png')
