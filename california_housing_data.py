import pandas as pd
from sklearn.datasets import fetch_california_housing

# Load the California housing dataset
california_housing = fetch_california_housing()

# Create a DataFrame from the dataset
data = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
data['TARGET_COLUMN'] = california_housing.target

# Save the dataset to a CSV file
data.to_csv('california_housing_data.csv', index=False)

# Display the columns
print(data.columns)
