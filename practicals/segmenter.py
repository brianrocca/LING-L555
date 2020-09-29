import sys
str = sys.stdin.read()
segment = str.replace('[. ][! ]', '.\n')
sys.stdout.write(segment)

"""
Here each sentence has been separated onto its own line. A simple approach, and the one we are going to try first, would simply be to replace every full stop '.' followed by a space ' ' with a full stop and a newline character '\n'. Can you write a program to do that? The program should be called segmenter.py and you should add it to your GitHub repository.
Questions

    How should you segment sentences with semi-colon? As a single sentence or as two sentences? Should it depend on context?
    Should sentences with ellipsis... be treated as a single sentence or as several sentences?
    If there is an exclamation after the first word in the sentence should it be a separate sentence? How about if there is a comma?
    Can you think of some hard tasks for the segmenter?
"""
