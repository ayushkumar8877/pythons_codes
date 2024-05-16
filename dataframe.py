import pandas as pd
#x = {'Name':['prince','ayush','ritik','manohar'],'Age':[21,23,24,5]}
x=[['jack',20,'bhilai','mtech'],['rahul',23,'patna','bca'],['ayush',21,'mumbai','btech'],['tanishk',20,'delhi','btech']]

df=pd.DataFrame(x,columns=['NAME','AGE','CITY','COURSE'])
print(df)
#x=df.drop('Age',axis=1)
#print(x)
#x=df.iloc[0:3]
x=df.loc[0:2]
print(x)