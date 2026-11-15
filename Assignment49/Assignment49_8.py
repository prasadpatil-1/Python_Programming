# Python program that calculates TP, TN, FP, FN for the following arrays:
# actual = [ 1,1,1,1,0,0,0,0]
# predicted = [ 1,1,0,1,0,1,0,0]

import numpy as np
from sklearn.metrics import confusion_matrix

def CM():
    
    actual = [ 1,1,1,1,0,0,0,0]
    predicted = [ 1,1,0,1,0,1,0,0]
    cm = confusion_matrix(actual, predicted, labels=[0,1])
    
    tn,fp ,fn, tp = cm.ravel()
    
    print(f"True Positives (TP): {tp}")
    print(f"True Negatives (TN): {tn}")
    print(f"False Positives (FP): {fp}")
    print(f"False Negatives (FN): {fn}")
    
def main():
    CM()
    
if __name__ =="__main__":
    main()