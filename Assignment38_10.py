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

sns.boxplot(x="FinalResult", y="SleepHours", data=df)

plt.title("Sleep Hours vs Final Result")

plt.xlabel("Final Result")
plt.ylabel("Sleep Hours")

plt.show()

#################################################################
#   The plot shows the relationship between SleepHours and FinalResult. 
#   Sleeping more does not guarantee success because students with adequate sleep can still fail. 
#   Academic performance depends on several factors such as study hours, attendance, previous scores, and assignment completion. 
##################################################################
