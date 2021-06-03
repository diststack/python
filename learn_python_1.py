#!/usr/bin/env python3
# from  urllib.request import urlopen
# with urlopen('http://sixty-north.com/c/t.txt') as story:
# 	story_word = []
# 	for line in story:
# 		line_words = line.decode('utf-8').split()
# 		for word in line_words:
# 			story_word.append(word)

# for word in story_word:
# 	print(word)
import sys

def calculate(x):
	"""
	args: 
	return:
	"""
	return x*x


def even_or_odd(n):
	if n%2 == 0:
    		return 'even'
	else:
    		return 'odd'


def test(x):
    	print(x)
# print(calculate(5))
# print(even_or_odd(6))
def main(number):
	# number = sys.argv[0]
	#calculate((int)number)
	# calculate(number)
	#print(calculate(number)
	# print(even_or_odd(int(number))
	print(test(number))
def convert(s):
    try:
        x = int(s)
		# glob.glob(
    except Exception as exe:
        print(str(exe))
        x = -1
        return x
import os

def totfiles_count():
    	file_count = 0;
			for (dirname, dir, files)in os.walk('.'):
    				for file in files:
    							if filename.endswith('.txt')
									count +=1
file_name = raw_input('Enter file name:')
handle = pen(name, 'r')
text = handle.read()


import sys

for arg in sys.argv
	print('arg',arg)


cmd = 'ls -l'
fp = 	os.popen(cmd)
fp.read()
fp.close()


if __name__ == "__main__":
	 main(sys.argv[1])