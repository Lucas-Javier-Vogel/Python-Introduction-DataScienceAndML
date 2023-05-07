import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

person = {"finance": [2,5,3,7,10,4,8,9,1,6,2,7,4,10,8,6,9,1,3,5,7,2,10,8,1,4,6,3,9,5],
          "management":[8,1,6,2,9,10,7,2,3,9,1,5,10,6,7,9,2,8,3,10,4,6,8,5,2,9,1,7,4,3],
          "logistic":[6,1,9,10,2,4,7,2,8,10,7,5,8,2,9,1,10,5,7,6,3,5,9,8,3,3,2,5,8,1],
          "get_work":[1,0,0,1,1,0,1,0,1,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0]
}

Data=pd.DataFrame(person,columns=["finance","management","logistic","get_work"])
#print(Data)

x=Data[["finance","management","logistic"]]
y=Data["get_work"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

lr = LogisticRegression()
lr.fit(x_train,y_train)
y_prediction = lr.predict(x_test)

conf_mat = pd.crosstab(y_test,y_prediction,rownames=["true"],colnames=["prevision"])

sb.heatmap(conf_mat,annot=True)

print("Accurace:",metrics.accuracy_score(y_test,y_prediction))

plt.show()