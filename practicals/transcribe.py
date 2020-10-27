import sys
str = sys.stdin.readlines()

line = 0
counter = 0
#dictionary
IPA = {}
IPA['a'] = 'a'
IPA['b'] = 'b'
IPA['c'] = 'tʃ'
IPA['d'] = 'd'
IPA['e'] = 'e'
IPA['f'] = 'f'
IPA['g'] = 'g'
IPA['h'] = 'h'
IPA['i'] = 'i'
IPA['j'] = 'ʤ'
IPA['k'] = 'k'
IPA['l'] = 'l'
IPA['m'] = 'm'
IPA['n'] = 'n'
IPA['o'] = 'o'
IPA['p'] = 'p'
IPA['q'] = 'q'
IPA['r'] = 'r'
IPA['s'] = 's'
IPA['t'] = 't'
IPA['u'] = 'u'
IPA['v'] = 'v'
IPA['w'] = 'w'
IPA['x'] = 'ks'
IPA['y'] = 'j'
IPA['z'] = 'z'

for c in str:
	line = line + 1
	print('# sent_id = %d' % (line))
	print('# text = %s' % (c))
	counter = 0
	lista = c.replace('.', ' .').replace(',', ' , ').replace('?', ' ?').replace('!', ' !').replace(';', ' ;').replace(':', ' :').replace(')', ' )').replace('(', '( ').replace(' "', '" ').replace('" ', ' " ').replace('\n', '').replace('"', ' " ').replace('/', ' / ')
	lista = lista.split(' ')
	for token in lista:
		counter = counter + 1
		transcription = token
		for letter in IPA:
			transcription = transcription.replace(letter, IPA[letter])
		listb = (counter, token, '_', '_', '_', '_', '_', '_', '_', transcription)
		print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (listb))
