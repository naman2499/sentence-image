import nltk
from nltk.corpus import wordnet 

def syn(obj_inp):
    obj_out = []
    for w in obj_inp:
        for synset in wordnet.synsets(w):
            for lemma in synset.lemmas():
                obj_out.append(str(lemma.name())) 
    res = []
    [res.append(x) for x in obj_out if x not in res]

    return res
