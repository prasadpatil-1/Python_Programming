import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#################################################################
#   Load the CSV
#################################################################
DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

#################################################################
#   Realtionship between Assignment Completed and FinalResult
#################################################################

df["FinnalResult"] = df["FinalResult"].map({0 : "Fail", 1 : "Pass"})

sns.boxplot(x="FinalResult", y ="AssignmentsCompleted" , data=df)

plt.xlabel("Final Result")
plt.ylabel("Assignment Completed")
plt.title("Assignment Completed vs Final Result")

plt.show()

#################################################################
#   The plot compares the number of assignments completed by students who passed and failed.
#   If the median number of assignments is higher for Pass students, 
#   it indicates that students who complete more assignments tend to perform better. T
#   The box plot also shows the spread and possible outliers in assignment completion.
##################################################################
