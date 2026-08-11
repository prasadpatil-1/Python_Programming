import pandas as pd

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

#################################################################
#   1   : Average StudyHours of student
#################################################################

print("Average Study Hours :", df["StudyHours"].mean())

#################################################################
#   2   : Average Attendace of student
#################################################################

print("Average Attendance :", df["Attendance"].mean())

#################################################################
#   2   : Maximum Privious score of student
#################################################################

print("Maximum Previous Score :", df["PreviousScore"].max())

#################################################################
#   2   : Maximum Privious score of student
#################################################################

print("Minimum Sleep Hours :", df["SleepHours"].min())


