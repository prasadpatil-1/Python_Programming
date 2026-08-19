import pandas as pd

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

#################################################################
#   Anaylase StudyHours and Attendence
#################################################################

result = df.groupby("FinalResult")[["StudyHours","Attendance"]].mean()

print(result)

#################################################################
#   Fails and Pass based on Analysis of StudyHours and Attendence
#################################################################

result.index = ["Fail", "Pass"]

print(result)
