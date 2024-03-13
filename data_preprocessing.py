import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv('california_housing_data.csv')

# Drop rows with missing values
data.dropna(inplace=True)

# Separate features (X) and target variable (y)
X = data.drop('TARGET_COLUMN', axis=1)
y = data['TARGET_COLUMN']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the columns of the features
print(X.columns)
