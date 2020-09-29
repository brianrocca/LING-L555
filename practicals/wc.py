#count letters
import sys

counter = 0
str = sys.stdin.read()
for c in str:
        if c in 'abcdefghijklmnopqrstuvwxyz':
                counter = counter + 1
print("letters", counter)

#count words
words = 0
for c in str:
        if c == ' ':
               words = words + 1
print("words", words)


#count  consonants

consonants = 0

for c in str:
        if c in 'bcdfghjklmnpqrstvwxyz':
                consonants = consonants + 1
print("consonants", consonants)

#count vowels
vowels = 0

for c in str:
        if c in 'aeiou':
                vowels = vowels + 1
print("vowels", vowels)

print("avg syllables per word", vowels / words)


#count paragraphs
lines = 0
for c in str:

	if c ==  '\n':
		lines = lines + 1
print("paragraphs", lines)

#count sentences
sentences = 0
for c in str:
	if c == '.':
		sentences = sentences +1
print("sentences", sentences)

