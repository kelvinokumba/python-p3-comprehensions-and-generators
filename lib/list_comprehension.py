#!/usr/bin/env python3

def return_evens(num_list):
    return [item for item in num_list if item % 2 == 0]



def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]

sentence_list=["Hello", "I'm doing great", "Python is fun"]
result=make_exclamation(sentence_list)
print(result)