import nltk
#nltk.download('words')

#from nltk.corpus import words
#word_list = words.words()

import regex as re

reg= re.compile(r"(.)\1")
dl = {}

word_list=['aaabb','abc','abbc']

for word in word_list:
    match = re.search(reg, word)
    if match:
        if match.group(1) not in dl:
            dl[match.group(1)] =1
            
        else:
            dl[match.group(1)]+=1
    
        
print(dl)