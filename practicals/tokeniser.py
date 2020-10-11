
import sys
str = sys.stdin.readlines()

line = 0
counter = 0

for c in str:
	line = line + 1
	print('# sent_id = %d' % (line))
	print('# text = %s' % (c))
	counter = 0
	lista = c.replace('.', ' .').replace(',', ' ,').replace('?', ' ?').replace('!', ' !').replace(';', ' ;').replace(':', ' :').replace(')', ' )').replace('(', '( ').replace(' "', '" ').replace('" ', ' " ')
	lista = lista.split(' ')
	for token in lista:
		counter = counter + 1

		listb = (counter, token, '_', '_', '_', '_', '_', '_', '_', '_')
		print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (listb))



