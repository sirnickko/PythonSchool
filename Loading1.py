#reading what is stored in the fie and allocating it to mydata variable
#reading the first 20 rows

import pandas as pd
import matplotlib.pyplot as plt

mydata = pd.read_csv(r'C:\Users\Sirnickko\Desktop\zetech\Year 2 SEM 2\DATA SCIENCE\medal.csv')
print(mydata.head())

country_data = mydata["country"]
medal_data = mydata["gold_medal"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0.1, 0, 0, 0, 0)
plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Gold medal achievements of five most successful\n"+"countries in 2023 Summer Olympics")
plt.show()