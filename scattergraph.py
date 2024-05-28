import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
file_path = 'books.csv'
data = pd.read_csv(file_path)

# Assuming 'Date' is in the format 'YYYY-MM-DD', you might want to convert it to a datetime object
data['Date'] = pd.to_datetime(data['Date'])

# Sorting data by 'Date' for better visualization
data = data.sort_values(by='Date')

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(data['Date'], data['Flight_Duaration_in_minutes'], marker='o')
plt.title('Flight Duration Over Time (Scatter Plot)')
plt.xlabel('Date')
plt.ylabel('Flight Duration (minutes)')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
