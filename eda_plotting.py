# pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.
import matplotlib.pyplot as plt
#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics
import seaborn as sns

df = pd.read_csv(
    'http://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv')

# sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 5)
# plt.xlabel("Flight Number",fontsize=20)
# plt.ylabel("Pay load Mass (kg)",fontsize=20)
# plt.show()

# HINT use groupby method on Orbit column and get the mean of Class column
orbit=df.groupby('Orbit')['Class'].mean()
df_new=pd.DataFrame(orbit, columns=['Class'])
df_new['Orbit']=orbit.index
sns.barplot(y="Class", x="Orbit",  data=df_new)
plt.xlabel("Orbit",fontsize=20)
plt.ylabel("Class",fontsize=20)

