import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv(r"C:/Users/kushal.singh01/Desktop/Kushal Python/my_venv\student_scores.csv")
print(df.head())

df.describe()
df.info()
df.isnull().sum()

df= df.drop("Unnamed: 0", axis=1)
print(df.head())

plt.figure(figsize=(5,5))
plt.title("Gender Distribution")
ax = sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
plt.show()
#we have analyzed that females are more than the male counts

gb= df.groupby("ParentEduc").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb)

plt.figure(figsize=(4,4))
plt.title("Relationship between parent's education and student's score")
sns.heatmap(gb, annot= True)
plt.show()
#Parent's education is affecting the Student's score.

gb1= df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb1)
plt.title("Relationship between parent's marital status and student's score")
sns.heatmap(gb1, annot=True)
plt.show()
#parent marital status have negligible impact on student's score

sns.boxplot(data=df, x="WritingScore")
plt.show()

print(df["EthnicGroup"].unique()) 

gpA= df.loc[(df["EthnicGroup"]=="group A")].count()
gpB=df.loc[(df["EthnicGroup"]=="group B")].count()
gpC=df.loc[(df["EthnicGroup"]=="group C")].count()
gpD=df.loc[(df["EthnicGroup"]=="group D")].count()
gpE=df.loc[(df["EthnicGroup"]== "group E")].count()

lb=["group A","group B","group C","group D","group E"]
plt.title("Distribution of groups")
plt.pie([gpA["EthnicGroup"],gpB["EthnicGroup"],gpC["EthnicGroup"],gpD["EthnicGroup"],gpE["EthnicGroup"]],labels=lb, autopct= "%1.2f%%")
print([gpA["EthnicGroup"],gpB["EthnicGroup"],gpC["EthnicGroup"],gpD["EthnicGroup"],gpE["EthnicGroup"]])
plt.show()

ax = sns.countplot(data=df,x="EthnicGroup")
ax.bar_label(ax.containers[0])
plt.show()






 


