import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#################################################################
#   Load the CSV
#################################################################
DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

#################################################################
#   Box plot for Attendance
#################################################################

sns.boxplot(y=df["Attendance"])

plt.title("Box plot for Attendance")

plt.ylabel("Attendance")

plt.show()

#################################################################
#  The box plot represents the distribution of students' attendance
#  The median shows the typical attendance level, while the box represents the middle 50% of the observations. 
#  The whiskers show the normal range of attendance, and any points beyond the whiskers represent possible outliers.
#  This plot helps identify the spread and unusual attendance values in the dataset.
##################################################################
