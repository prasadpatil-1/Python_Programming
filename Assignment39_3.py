import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



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


    X_train ,X_test, Y_train, Y_test = train_test_split(X , Y ,test_size=0.4, random_state= 42)

#################################################################
#   Step 4 : Creating object of DecisionTreeClassifier
#################################################################

    model = DecisionTreeClassifier()

#################################################################
#   Step 5 : Train using fit
#################################################################

    model.fit(X_train, Y_train)

#################################################################
#   Step 6 : Prediction
#################################################################

    Y_Pred = model.predict(X_test)
    
    print("Result for X is :",Y_Pred)

#################################################################
#   Step 6 : Accurarcy in Percentage
#################################################################

    Result = accuracy_score(Y_test, Y_Pred)

    print("Acuuarcy is : ",Result * 100)

if __name__ == "__main__":
    main()