# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib  # To save the trained model

# Load preprocessed data
data = pd.read_csv("california_housing_data.csv")  # Update with your actual file path

# Assuming your target column is 'TARGET_COLUMN'
X = data.drop('TARGET_COLUMN', axis=1)
y = data['TARGET_COLUMN']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Save the trained model for future use
joblib.dump(model, "trained_model.joblib")  # Update with your desired file path
