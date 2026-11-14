# implement simple linear Regression manually without using ML library
# Dataset
# X =[1,2,3,4,5]
# Y =[3,4,2,4,5]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    # Load the Data
    
    X =[1,2,3,4,5]
    Y =[3,4,2,4,5]
    
    print("Values of Independent Variable X :", X)
    print("Values of Dependent variables Y : ", Y)
    
    sum_X = 0
    sum_Y = 0
    
    for i in range(len(X)):
        sum_X = sum_X+ X[i]
        sum_Y = sum_Y+ Y[i]
        
    mean_X = sum_X / len(X)
    mean_Y = sum_Y / len(Y)
    
    print("Mean_X is :", mean_X)
    print("Mean_Y is :", mean_Y)
    
    n= len(X)
    
    numerator = 0
    Denomenator = 0

    # m = sum(x-xbar) *(y-ybar) / sum(x-xbar) **2
    # calculate slope ie m
    
    for i in range(n):
        numerator = numerator + ((X[i]- mean_X) * (Y[i]- mean_Y))
        Denomenator = Denomenator + ((X[i]-mean_X) ** 2)
        
    m = numerator/ Denomenator
    
    print("Slope of line ie m :", m)
    
    # y = mx+c
    # c= y-mx
    # c = ymean-m * xmean
    
    c = mean_Y - m * mean_X
    
    print("Y intercept ie C is :", c)
    
    Y = (f" {m} X  + {c}")
    
    print("Regression Equation :")
    print("Y = ", Y)
    
    X_new = 6
    
    Predicted_Y = m * X_new + c
    print("Predicted Y for X = ", X_new ,":", Predicted_Y)
    
def main():
    
    MarvellousPredictor()
    
if __name__ =="__main__":
    main()
