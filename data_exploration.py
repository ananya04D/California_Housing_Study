import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('california_housing_data.csv')

# Display basic information about the data
print(data.info())
print(data.describe())

# Scatter plot
sns.scatterplot(x='AveRooms', y='TARGET_COLUMN', data=data)
plt.show()
