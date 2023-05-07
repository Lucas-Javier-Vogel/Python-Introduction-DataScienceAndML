import pandas as pd

employee = {'number':[1,2,3,4,5],'name':['Abby','John','Lina','Mark','Bob'],'hourly_salary':[15,25,32,27,40]}
table1 = pd.DataFrame(employee)

print(table1)