import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
file_path = 'books.csv'
data = pd.read_csv(file_path)

# Check the columns in the dataset
print(data.columns)

# Remove any extra spaces from column names and display the columns again
data.columns = data.columns.str.strip()
print(data.columns)

# Now, create the pie chart using the correct column name
source_country_counts = data['Source_Country'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
source_country_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Source Countries Distribution')
plt.ylabel('')  # Remove y-label
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.legend(loc='upper right')  # Add a legend
plt.show()
