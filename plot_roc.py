import argparse
from os import listdir
from pathlib import Path
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as sklearn
from random import randint

def extract(root, filePaths):
    result = dict()
    for filePath in filePaths:
        file_name = Path(filePath).stem
        file = open(root+"\\"+filePath, 'r')
        marker = "--"
        got_marker = False
        for line in file.readlines():
            if line.startswith(marker):
                got_marker = True
                continue
            if got_marker:
                result.update({file_name:line.split()[1]})
                break
    return sort_dict_by_value(result)

# this one is sorting the dictionary by value
# afterwards only take_count will be returned
#  depending if reverse parameter is set to True or False, the best or the worst values will be taken
def sort_dict_by_value(x):
    s = dict(sorted(x.items(), key=lambda item: item[1], reverse=False))
    print(s)
    take_count = 40
     # comment this line in, so that only take_count will be returned. If the line is commented out, all values will be returned.
    # s = {k: s[k] for k in list(s)[:take_count]}
    return s

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-dp', '--decoy_path', required=True)
    argument_parser.add_argument('-lp', '--ligand_path', required=True)

    args = argument_parser.parse_args()
    
    decoy_path = args.decoy_path
    ligand_path = args.ligand_path

    ligand_paths = [f for f in listdir(ligand_path) if isfile(join(ligand_path, f))]
    decoy_paths = [f for f in listdir(decoy_path) if isfile(join(decoy_path, f))]

    ligands = extract(ligand_path, ligand_paths)
    decoys = extract(decoy_path, decoy_paths)


    # this part will prepare the lists y_true and y_score for the roc_curve function
    y_true = []
    y_score = []
    for key in ligands:
        y_true.append(1)
        y_score.append(float(ligands[key]))
    for key in decoys:
        y_true.append(2)
        y_score.append(float(decoys[key]))


    # plots the roc curve
    fpr, tpr, thresholds = sklearn.roc_curve(np.array(y_true), np.array(y_score), pos_label=1)
    roc_auc = sklearn.auc(fpr, tpr)
    plt.plot(fpr, tpr, color='blue', lw=2, label='ROC curve' % roc_auc)
    plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--', label='Random classifier')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve for 1a4g')
    plt.legend(loc="lower right")
    plt.show()
    print(roc_auc)

    # plots the decoys and ligands against each others
    '''
    plt.plot(np.array(list(decoys.values())), label='decoys')
    plt.plot(np.array(list(ligands.values())), label='ligands') 
    plt.legend(loc='best')
    plt.show()
    '''
main()