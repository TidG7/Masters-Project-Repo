import numpy as np
import pandas as pd
import os
orbs = ('s', 'p', 'd', 'f')


def magTune_import(atom1, n1_0, l1_0, j1_0, atom2, n2_0, l2_0, j2_0, l1_1, l2_1):
    magFile = fr'C:\\Users\\tommy\\OneDrive - Durham University\\level 4 Project\\Data\\Zeeman tunes\\{atom1}{atom2}\\{orbs[l1_0]}{orbs[l2_0]}\\to {orbs[l1_1]}{orbs[l2_1]}\\j1j2({j1_0},{j2_0})\\{n1_0}{n2_0}.csv'
    
    if os.path.exists(magFile):
        data = pd.read_csv(magFile)
        return data['tunes']
    else:
        print("Magnetic file doesn't exist")

def channels_import(atom1, l1_0, j1_0, atom2, l2_0, j2_0, l1_1, l2_1):
    data = pd.read_csv(fr'C:\\Users\\tommy\\OneDrive - Durham University\\level 4 Project\\Data\\channels\\{atom1}{atom2}\\{orbs[l1_0]}{orbs[l2_0]}\\j1j2({j1_0},{j2_0})\\to {orbs[l1_1]}{orbs[l2_1]}.csv')
    
    print(f'{data}')

    return data