import pandas as pd
data = {
'Name': ['Peter', 'Joyce', 'George', 'Phylis', 'Moses','Priscillah', 'Eliud'],
'Age': [25, 30, 22, 28, 24, 34, 19],
'Gender': ['Male', 'Female', 'Male', 'Female','Male', 'Female','Male'],
'Marks': [85, 92,'NaN', 88, 'NaN',79,80]
}
wainaina = pd.DataFrame(data)
#wainaina.head(20)
print(wainaina)

c=0
avg=0
sum=0
for me in wainaina['Marks']:
  if str(me).isnumeric():
      c=c+1;
      #c+=1
      #avg+=me
      sum=sum+me
      avg=sum/c
print("\n Cout=\n",c)
print("\n Sum=\n",sum)
print("\n Average=\n",avg)
wainaina=wainaina.replace(to_replace="NaN",value=avg)
print("\n NEW DATA \n")
print(wainaina)

wainaina['Gender'] = wainaina['Gender'].replace({'Female': 1.0, 'Male': 0.0})
wainaina['Gender'] = wainaina['Gender'].map({'Female': 1.0, 'Male': 0.0}).astype(float)

wainaina=wainaina[wainaina['Marks']>=85]
wainaina=wainaina.drop(['Gender'],axis=1)
print(wainaina)
