import pandas as pd

food1 = {'number':[1,2,3,4,5],'name':['corn','bananas','pizza','chips','protein'],'price':[5,2,8,4,10]}
food2 = {'number':[1,2,3,4,5],'name':['apples','bananas','pizza','beans','protein'],'price':[2,2,8,4,10]}

table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

#Merge two tables that have the same values
fusion = pd.merge(table1, table2)
#Its possible to keep some columns with exceptions
fusion = pd.merge(table1,table2,on='number')

print(fusion)