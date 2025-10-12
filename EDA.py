import pandas as pd
dataset = pd.read_csv('C:/Users/Sirnickko/Desktop/zetech/Year 2 SEM 2/DATA SCIENCE/EDA.csv')
dataset.head(10)

dulpicated_rows = dataset[dataset.duplicated()]
print("Duplicated rows:")
print(dulpicated_rows)

AgeDuplicate=dataset[dataset['Age'].duplicated()]
print("Duplicated Age rows:")
print(AgeDuplicate)

print("\nUnique values in 'AGE' Column:")
print(dataset['Age'].value_counts())