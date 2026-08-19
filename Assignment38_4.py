import pandas as pd

#################################################################
#   Load the CSV
#################################################################
DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

#################################################################
# Count Pass and Fail
#################################################################

count = df["FinalResult"].value_counts()

print("Final Result Count:")
print(count)

#################################################################
# Calculate percentage
#################################################################

percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("\nFinal Result Percentage:")
print(percentage)