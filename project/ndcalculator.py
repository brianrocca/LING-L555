import sys
import eng_to_ipa as ipa
from Levenshtein import*
#open and read lines in file
filename = sys.argv[1]
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
	lista = lista.lower()
	lista = lista.split(' ')
	lista_no_empty = [x for x in lista if x != '']

	for token in lista_no_empty:
		#Transcribe words into IPA
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

#Graph phonological neighborhoods as one large network
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
#For each pair of IPA words
for k,v in pairs.items():
	#For each related word
	for vv in v:
		#For each of the orthographic forms
		for ww in words[vv]:
			#For each of the orthographic forms
			for kk in words[k]:
				G.add_edge(kk,ww)		
f = plt.figure()
nx.draw_kamada_kawai(G,
		with_labels=True,
		node_color='blue',
		node_size=1200,
		font_color='white',
		font_size=12,
		)
f.savefig("ndgraph.png")