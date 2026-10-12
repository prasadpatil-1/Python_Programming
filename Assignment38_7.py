import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#################################################################
#   Load the CSV
#################################################################
DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

#################################################################
#   Scatter plot for StudyHours vs previousScore
#################################################################

sns.scatterplot(
    data=df,
    x="StudyHours",
    y = "PreviousScore"
)

plt.title("StudyHours vs Privious Score")
plt.xlabel("Study Hours")
plt.ylabel("Prvious Score")

plt.show()

#################################################################
#  The scatter plot shows the relationship between StudyHours and PreviousScore. 
#  If the points generally move upward as StudyHours increase, it indicates a positive relationship between the two variables. 
#  Students who study more hours tend to have higher previous scores. However, the relationship may not be perfect because other factors can also affect students' performance.
#################################################################