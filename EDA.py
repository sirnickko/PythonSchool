import pandas as pd
dataset = pd.read_csv('C:/Users/Sirnickko/Desktop/zetech/Year 2 SEM 2/DATA SCIENCE/EDA.csv')
dataset.head(10)

dulpicated_rows = dataset[dataset.duplicated()]
print("Duplicated rows:")
print(dulpicated_rows)
#duplicate in specific column
AgeDuplicate=dataset[dataset['Age'].duplicated()]
print("Duplicated Age rows:")
print(AgeDuplicate)

print("\nUnique values in 'AGE' Column:")
print(dataset['Age'].value_counts())
#handling missing values
null = dataset.isnull().sum()
print("null values are \n",null)

#replacing null values with 0
dataset_filled = dataset.fillna(0)
#replace a specific cell
dataset.at[3,'Testscore']=88

