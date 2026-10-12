import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    confusion_matrix,
    precision_score
)

data = pd.read_csv("student_performance_ml.csv")

print(data.head(10))

print(data.isnull().sum())


X = data.drop('FinalResult', axis=1)

Y = data['FinalResult']

print("Features are :", X)

print("Target is : ", Y)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier()

model = model.fit(X_train, Y_train)

Y_Pred = model.predict(X_test)

# -------------------------------
# Performance Metrics
# -------------------------------

accuracy = accuracy_score(Y_test, Y_Pred)

print("Accuracy score is : ", accuracy)

f1 = f1_score(Y_test, Y_Pred)

print("The f1 score is : ", f1)

cm = confusion_matrix(Y_test, Y_Pred)

print("Confusion matrix : ")
print(cm)

precision = precision_score(Y_test, Y_Pred)

print("Precision score is : ", precision)


# -------------------------------
# Feature Importance
# -------------------------------

importance = model.feature_importances_

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importance
})

# Sort from highest to lowest
feature_importance = feature_importance.sort_values(
    by='Importance',
    ascending=False
)

print("\nFeature Importance:")
print(feature_importance)


# -------------------------------
# Least Contributing Feature
# -------------------------------

least_feature = feature_importance.iloc[-1]

print("\nLeast Contributing Feature:")
print("Feature:", least_feature['Feature'])
print("Importance:", least_feature['Importance'])