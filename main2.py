from image_extract import *
from sentence_extract import *
from image_download import *
loc = input('enter image location: ')

obj_inp = pred(loc)

# obj_inp, action_inp, scene_inp = sen_to_space(sent)
# print(obj_inp, action_inp, scene_inp)

# match_sen([str(obj_inp)],[],[])
match_sen(['airplane'],[],[])
