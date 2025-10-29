import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib  # for saving model

# Loading the dataset
import pandas as pd

data = pd.read_csv("C:\\Users\\Sirnickko\\Desktop\\zetech\\Year 2 SEM 2\\DATA SCIENCE\\road_accidents.csv")
print(data.head())


# Selecting the independent and dependent variables
X = data[['Speed_limit', 'Weather_condition', 'Road_surface_condition', 'Light_condition']]
y = data['Accident_Severity']

# Spliting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("R² Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Saving the  model
joblib.dump(model, 'accident_severity_model.pkl')

# Load the saved model
model = joblib.load('accident_severity_model.pkl')

# example
sample_data = pd.DataFrame({
    'Speed_limit': [80],
    'Weather_condition': [2],  # e.g., 1=Clear, 2=Rainy, etc.
    'Road_surface_condition': [1],  # e.g., 1=Dry, 2=Wet
    'Light_condition': [1]  # e.g., 1=Daylight, 2=Dark
})

predicted_severity = model.predict(sample_data)
print("Predicted Accident Severity:", predicted_severity[0])
