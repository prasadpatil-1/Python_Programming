import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay


def main():

    #################################################################
    # Step 1 : Loading CSV data
    #################################################################

    df = pd.read_csv("student_performance_ml.csv")


    #################################################################
    # Step 2 : Separating Features and Target
    #################################################################

    X = df.drop("FinalResult", axis=1)
    Y = df["FinalResult"]


    #################################################################
    # Step 3 : Split the Data
    #################################################################

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.4,
        random_state=42
    )


    #################################################################
    # Step 4 : Creating object of DecisionTreeClassifier for different depth
    #################################################################

    model1 = DecisionTreeClassifier(
        max_depth=1,
        random_state=42
    )

    model2 = DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )

    model3 = DecisionTreeClassifier(
        max_depth=None,
        random_state=42
    )


    #################################################################
    # Step 5 : Train using fit
    #################################################################

    model1.fit(X_train, Y_train)
    model2.fit(X_train, Y_train)
    model3.fit(X_train, Y_train)


    #################################################################
    # Step 6 : Prediction
    #################################################################

    Y_Pred1 = model1.predict(X_test)
    print("Result for X1 is :", Y_Pred1)

    Y_Pred2 = model2.predict(X_test)
    print("Result for X2 is :", Y_Pred2)

    Y_Pred3 = model3.predict(X_test)
    print("Result for X3 is :", Y_Pred3)

    #################################################################
    # Step 7 : Accuracy in Percentage
    #################################################################

    Result1 = accuracy_score(Y_test, Y_Pred1)
    print("Accuracy of first model is :", Result1  * 100)

    Result2 = accuracy_score(Y_test, Y_Pred2)
    print("Accuracy of second model is :", Result2  * 100)

    Result3 = accuracy_score(Y_test, Y_Pred3)
    print("Accuracy of third model is :", Result3 * 100)

    

if __name__ == "__main__":
    main()