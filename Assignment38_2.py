import pandas as pd

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

#################################################################
#   1   : Total number of student
#################################################################

print("Total Students :", len(df))

#################################################################
#   2   : Passed student
#################################################################

passed = (df["FinalResult"] == 1).sum()
print("Passed Students :", passed)

#################################################################
#   3   : Failed student
#################################################################

failed = (df["FinalResult"] == 0).sum()

print("Failed Students :", failed)