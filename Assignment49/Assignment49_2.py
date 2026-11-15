# Python Program that calculates the variance and standard deviation of the dataset
# [6,7,8,9,10,11,12]

import numpy as np
import math
import statistics

def Mean():
    
    X = [6,7,8,9,10,11,12]
    
    mean_X = np.mean(X)
    
    # using manual Calculation
    print("using manual Calculation")
    
    variance = sum ((X- mean_X) ** 2 )/ len(X)

    print("Variance :", variance)
    
    Std_Deviation = math.sqrt(variance)
    
    print("Standard deviation :", Std_Deviation)
    
    # Using Statistics module
    print("Using Statistics module")
    
    variance_stats= statistics.pvariance(X)
    Std_Deviation_stats = statistics.pstdev(X)
    
    print("Variance :", variance_stats)
    print("Standard deviation :", Std_Deviation_stats)
    
def main():
    
    Mean()

if __name__ == "__main__":
    main()