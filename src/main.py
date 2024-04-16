import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os

# Get the current directory of the script
parnet_dir = os.path.dirname(os.path.dirname(__file__))

# Construct the full path to the CSV file
csv_file_path = os.path.join(parnet_dir, 'resources', 'Parks_Tree_Inventory.csv')

# If file doesn't exist, then run error and exit program
try:
    # Read the CSV file into a DataFrame
    trees = pd.read_csv(csv_file_path)
except:
    SystemExit('Error: CSV file not found at', csv_file_path)

trees = trees.dropna(subset=['DBH', 'Total_Annual_Benefits'])

# Establish table variables
size = [float(i) for i in trees['DBH']]
value = [float(j) for j in trees['Total_Annual_Benefits']]

# Calculate descriptive statistics
size_mean = np.mean(size)
size_median = np.median(size)
size_range = np.ptp(size) # Peak to peak, i.e., max - min
size_std_dev = np.std(size)

value_mean = np.mean(value)
value_median = np.median(value)
value_range = np.ptp(value)
value_std_dev = np.std(value)

print('Descriptive Statistics for Diameter at Breast Height (DBH):')
print(f'Mean: {size_mean:.2f}')
print(f'Median: {size_median:.2f}')
print(f'Range: {size_range:.2f}')
print(f'Std-Dev: {size_std_dev:.2f}')
print()
print('Descriptive Statistics for Total Annual Benefits (TAB):')
print(f'Mean: {value_mean:.2f}')
print(f'Median: {value_median:.2f}')
print(f'Range: {value_range:.2f}')
print(f'Std-Dev: {value_std_dev:.2f}')

# Plotting DBH box-plot
plt.figure(figsize=(6, 6))
sns.boxplot(y=size, color='yellow')
plt.title('Boxplot of Diameter at Breast Height (DBH)')
plt.ylabel('Diameter at Breast Height')
plt.savefig('resources/DBH_box_plot.png')
# plt.show()

# Plotting TAB box-plot
plt.figure(figsize=(6, 6))
sns.boxplot(y=value, color='green')
plt.title('Boxplot of Total Annual Benefits (TAB)')
plt.ylabel('Total Annual Benefits')
plt.savefig('resources/TAB_box_plot.png')
# plt.show()

# Plotting DBHxTAB
plt.clf() # Clear the current plot so you don't plot over the previous graph
plt.scatter(size, value, 0.75)
plt.xlabel('Diameter at Breast Height')
plt.ylabel('Total Annual Benefits')
plt.title('Total Annual Benefits of Portland Parks Tree Inventory\nby Tree Diameter at Breast Height')
plt.savefig('resources/TABxDBH_scatter_plot.png')
# plt.show()
