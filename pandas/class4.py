import pandas as pd

food1 = {'number':[1,2,3,4,5],'name':['corn','bananas','pizza','chips','protein'],'price':[5,2,8,4,10]}
food2 = {'color':['white','yellow','orange','red','blue'],'weight':[100,200,150,175,225],'qt':[1,2,1,3,4]}

table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

fusion = table1.join(table2)

print(fusion)