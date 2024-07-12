from pymol import cmd

import chempy
import numpy as np
import math

@cmd.extend
def split_and_align(object_a, object_b):
    model_object_a = cmd.get_model(object_a)
    model_object_b = cmd.get_model(object_b)

    if len(model_object_a.atom) != len(model_object_b.atom):
        print("The number of atoms in the two objects are different")
        return
    
    cmd.split_states(object_b)
    
    

    for frame in range(cmd.count_frames()):

        ident_b = object_b+"_000"+str(frame+1)
        model_object_b = cmd.get_model(ident_b)

        print(cmd.align(object_a, ident_b)[0])
        cmd.delete(ident_b)