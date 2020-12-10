import sys
fd = open('wiki.conllu', 'r')
input = fd.readlines()
fd.close()

#create dictionaries
freq = {}
m = {}
pos = {}
for line in input:
	# if there is no tab character, skip the line
	if '\t' not in line:
		continue
        # make a list of the cells in the row. If there aren't 10 cells, skip the line.
	row = line.split('\t')
	if len(row) != 10:
		print('ERROR:', line)
		continue
        # identify which row to read
	form = row[1]
	tag = row[3]
	#store and count unique words in freq
	if form not in freq:
		freq[form] = 0
	freq[form] += 1
	#create dictionary for m
	if form not in m:
		m[form] = {}
	if tag not in m[form]:
		m[form][tag] = 0
	if tag in m[form]:
		m[form][tag] += 1
	#create dictionary for tags
	if tag not in pos:
		pos[tag] = 0
	pos[tag] += 1
print(sum(freq.values()))
header = ('#P', 'count', 'tag', 'form')
print('\t'.join(header))
for tag in pos:
	print(str('%.2f' % (pos[tag]/sum(freq.values()))) + '\t' + str(pos[tag]) + '\t' + tag + '\t' + '_' + '\n', end='')
for form in m:
	for tag in m[form]:
		print(str('%.2f' % (m[form][tag]/freq[form])) + '\t' + str(freq[form]) + '\t' + tag + '\t' + form + '\n', end='')
