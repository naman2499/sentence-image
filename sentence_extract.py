import spacy
import pandas as pd
from image_extract import *
from tqdm import tqdm
from nltk.stem.snowball import SnowballStemmer
## references && labels
## pos https://universaldependencies.org/docs/u/pos/
## dep https://github.com/clir/clearnlp-guidelines/blob/master/md/specifications/dependency_labels.md
## dep  https://nlp.stanford.edu/software/dependencies_manual.pdf

nlp = spacy.load("en_core_web_sm")

def sen_to_space(sen):
    doc = nlp(sen)
    obj = []
    action = []
    scene = []
    for token in doc:
        if ((token.pos_ == 'NOUN' or token.pos_ == 'PROPN') and (token.dep_ in {"nsubj", "nsubjpass", "csubj", "csubjpass", "agent", "expl","compound" ,"ROOT"} )):
            obj.append(str(token))
        if token.pos_ == 'VERB':
            stemmer = SnowballStemmer("english")
            action.append(str(stemmer.stem(str(token))))
        if token.pos_ == 'NOUN' and (token.dep_ in {"dobj", "dative", "attr", "oprd","pobj"}):
            scene.append(str(token))
    # print(doc)
    # for token in doc:
    #     print(token.text, token.pos_, token.dep_)
    # print(obj, action, scene) 
    return obj, action, scene


df = pd.read_csv("data.csv",error_bad_lines=False) 
# print(df)
# print(df.columns.values.tolist())
yoyo = df.columns.values.tolist()
yoyo.pop(0)

def match_sen(obj_inp, action_inp, scene_inp,option):
    for i in tqdm(range(0,1000)):
        for yo in yoyo:
            # print(sen_to_space(df[yo][i]))
            objb=[]
            actionb=[]
            sceneb=[]
            obj, action, scene = sen_to_space(df[yo][i])
            objb.append(obj)
            actionb.append(action)
            sceneb.append(scene)
            # print(obj, action, scene)
            if (option == 's'): 
                ##implement similarity - lin or nltk
                if  (any(x==y for x in obj for y in obj_inp) and any(a == b for a in action for b in action_inp)) and any(p == q for p in scene for q in scene_inp) :
                    show_url(df['img_url'][i])
                # else:
                #     if  (any(x==y for x in objb for y in obj_inp) and any(a == b for a in actionb for b in action_inp)) and any(p == q for p in sceneb for q in scene_inp) :
                #        show_url(df['img_url'][i])
                
            else:
                if  (any(x==y for x in obj for y in obj_inp)):
                    print(df[yo][i])
