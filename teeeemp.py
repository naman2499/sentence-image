obj = [1,2,3]
action = [44,4]
scene = [1]

obj_inp = [1,2,3]
action_inp = [44,4]
scene_inp = [1]
# if any(x == y for x in obj for y in act):
    # print('tttt')

# if  any(x==y for x in obj for y in obj_inp) and any(a == b for a in action for b in action_inp) and any(p == q for p in scene for q in scene_inp) :
# if (set(obj) == set(obj_inp)) and (set(action) == set(action_inp)) and (set(scene) == set(scene_inp)):
if obj_inp == obj:
    print('yesc')