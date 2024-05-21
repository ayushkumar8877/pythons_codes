'''import pandas as pd
import numpy as np
d={'red':2,'blue':3,'yellow':4}
a=pd.Series([3,4,5,6,7,8],index=['a','b','c','d','e','f'])
a=pd.Series([3,4,5,6,7,8],index=['red','blue','yelllow','black','red','orange'])
print(a.unique)
print(a)'''
#.array([1,2,6,7,8],index=['a','b','c','d','e'])
#b=pd.Series(a)
#print(b)



#FOR READ AND WRITE CSV FILE
import pandas as pd
#ayush=pd.read_csv("e:\\material\\lol.csv")
ayush=pd.read_csv("e:\\material\\lol.csv")
print(ayush)