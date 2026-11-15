# Python program that calculates the mean of a dataset using Numpy for the following values 
# [6,7,8,9,10,11,12]

import numpy as np

def Mean():
    
    X = [6,7,8,9,10,11,12]
    
    mean_X = np.mean(X)
    
    print("Mean of dataset ie X is :", mean_X)
    
def main():
    
    Mean()
    
if __name__ =="__main__":
    main()