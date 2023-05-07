import pandas as pd

employee = {'number':[1,2,3,4,5],'name':['Abby','John','Lina','Mark','Bob'],'hourly_salary':[15,25,32,27,40]}
table1 = pd.DataFrame(employee)

#The first column on the table
print(table1.head(1))
#The last column on the table
print(table1.tail(1))