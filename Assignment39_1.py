import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split



def main():

#################################################################
#   Step 1 : Loading CSV data
#################################################################

    df = pd.read_csv("student_performance_ml.csv")

#################################################################
#   Step 2 : Separating Featurse and Target 
#################################################################
    X = df.drop("FinalResult" , axis=1)
    Y = df["FinalResult"]

#################################################################
#   Step 3 : Split the Data
#################################################################


    X_train ,X_test, Y_train, Y_test = train_test_split(X , Y ,test_size=0.2, random_state= 42)

#################################################################
#   Step 4 : Creating object of DecisionTreeClassifier
#################################################################

    model = DecisionTreeClassifier()

#################################################################
#   Step 5 : Train using fit
#################################################################

    model.fit(X_train, Y_train)


if __name__ == "__main__":
    main()