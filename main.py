from image_extract import *
from sentence_extract import *

sent = input('enter a sentence:')
obj_inp, action_inp, scene_inp = sen_to_space(sent)
print(obj_inp, action_inp, scene_inp)

match_sen(obj_inp, action_inp, scene_inp)

# show_url('https://vision.cs.uiuc.edu/pascal-sentences/aeroplane/2008_001227.jpg') One jet lands at an airport while another takes off next to it.
