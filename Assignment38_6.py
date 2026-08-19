import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#################################################################
#   Load the CSV
#################################################################
DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

#################################################################
#   Histogram for StudyHours 
#################################################################

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="StudyHours",
    bins=10,
    kde=True
)

plt.title("Distrubution of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")

plt.show()

#################################################################
#  The histogram shows the distribution of study hours among students. 
#  Most students are concentrated around a particular range of study hours. 
#  The shape of the histogram helps us understand whether the data is normally distributed or skewed. 
#  A higher frequency in a particular range indicates that more students study for that number of hours. 
#  The distribution also helps identify students who study unusually fewer or more hours.
#################################################################