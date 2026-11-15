# python program using scikit-learn to generate a classification report for the following data:
# actual = [ 1,1,1,1,0,0,0,0]
# predicted = [ 1,1,0,1,0,1,0,0]

import numpy as np
from sklearn.metrics import classification_report

def CR():
    
    actual = [ 1,1,1,1,0,0,0,0]
    predicted = [ 1,1,0,1,0,1,0,0]
    
    Y_actual = np.array([ 1,1,1,1,0,0,0,0])
    Y_pred = np.array([ 1,1,0,1,0,1,0,0])
    
    report = classification_report(Y_actual, Y_pred, target_names=["Class 0", "Class 1"])
    
    print("Classification report :")
    print(report)
    
def main():
    
    CR()
    
if __name__ == "__main__":
    main()

