import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#----------------------------------
# Step 1. Load the Dataset
#----------------------------------

Border = '-'*40
print(Border)

df = pd.read_csv("Fraudulent_Transaction_Detection (1).csv")

print("Datset load succesfully")
print(Border)

print(df.head())

#----------------------------------
# Step 2. Check missing values
#----------------------------------

print(Border)
print("Step 2 . Check Missing Values")
print(Border)

print("Missing values\n :", df.isnull().sum())

#----------------------------------
# Step 2. split dataset for training and testing
#----------------------------------

X = df.drop(['Fraud'], axis= 1)
Y = df['Fraud']

X_train, X_test, Y_train, Y_test =  train_test_split(X,Y, train_size=0.8, random_state=42)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

#----------------------------------
# Step 2. Decision tree
#---------------------------------


