import sys
import _io
import pandas as pd
import re

# get text file from CLI argument 
def input_file():
    fin = open(sys.argv[1],"r")
    return fin

# read file line by line to lower case and replace txt
def text_sanitizer():
    fin = input_file()
    txt = ''
    for line in fin:
        line = line.lower()
        txt += line.replace('\t', '___')
        txt += '\n'
    
    return txt.rstrip('\n')

# count only alphabet in text file and sort it
def count_alphabet():
    fin = input_file()
    txt = ''
    for line in fin:
       txt += re.sub(r'[^a-zA-Z]', '', line).lower() 
       
    ct = pd.Series(list(txt)).value_counts().sort_index()

    return ct

# print output to console
if __name__ == '__main__':
    print('sanitizerd text : \n')
    print(text_sanitizer() + '\n')
    print('statistic : \n')
    print(count_alphabet())

