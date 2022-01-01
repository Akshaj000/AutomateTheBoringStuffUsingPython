from os import read
import re

file = open('file.txt','r')
read = file.read()
noun,verb,adjective,adverb = '','','','';
noun=input("Noun: ")
verb=input("Verb: ")
adjective=input("Adjective: ")
adverb=input("Adverb: ")
list = [noun,verb,adjective,adverb]
list2 = ['NOUN','VERB','ADJECTIVE','ADVERB']
file.close()
file = open('file.txt','w')
for  i in range(4):
    read = re.sub(list2[i], list[i], read)
file.write(read)
file.close()