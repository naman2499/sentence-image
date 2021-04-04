from image_extract import *
from sentence_extract import *
from image_download import *
import nltk
from nltk.corpus import wordnet 

option = input("Input 's' for sentence, 'i' for image: ")

if option == 's':
    sent = input('enter a sentence: ')
    obj_inp, action_inp, scene_inp = sen_to_space(sent)
    print(obj_inp, action_inp, scene_inp)
    match_sen(obj_inp, action_inp, scene_inp, option)


elif option == 'i':
    loc = input('enter image location: ')
    obj_inp = []
    obj_org = pred(loc)
    obj_inp.append(str(obj_org))
    for synset in wordnet.synsets(obj_org):
        for lemma in synset.lemmas():
            obj_inp.append(str(lemma.name())) 
    
    match_sen(obj_inp,[],[],option)

else:
    print('try again')
