import pandas as pd


df=pd.read_csv("http://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")
# df.head(10)
print('null percentage', df.isnull().sum()/len(df)*100)
# Apply value_counts() on column LaunchSite
print(df.groupby('LaunchSite')['LaunchSite'].value_counts().reset_index())
landing_outcomes = df['Outcome'].value_counts()
for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)

bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
bad_outcomes
landing_class=[]
landing_class=[]
for outcome in df['Outcome'].values:
    if outcome in bad_outcomes:
        landing_class.append(0)
    else:
        landing_class.append(1)

# landing_class = 0 if bad_outcome
# landing_class = 1 otherwise
landing_class
df['Class']=landing_class
df[['Class']].head(8)
df.to_csv("dataset_part_2.csv", index=False)
