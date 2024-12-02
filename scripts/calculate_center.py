from pymol import cmd

import chempy
import numpy as np
import math

@cmd.extend
def calculate_center(object):
    model = cmd.get_model(object)
    x = 0.0
    y = 0.0
    z = 0.0
    count = 0
    for atom in model.atom:
        x += atom.coord[0]
        y += atom.coord[1]
        z += atom.coord[2]
        print(atom.coord[0], atom.coord[1], atom.coord[2])
        count += 1
    print ([x/count, y/count, z/count])
