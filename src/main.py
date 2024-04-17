import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

import plot_boxplot as pbp

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

# Calculate the correlation coefficient between DBH & TAB
corr_coef = np.corrcoef(size, value)[0, 1]
dbh_tab_df = trees[['DBH', 'TreeHeight', 'CrownWidthNS', 'Pollution_Removal_oz', 'Stormwater_ft', 'Total_Annual_Benefits']]
correlation_matrix = dbh_tab_df.corr()

# Print DBH stats
print('Descriptive Statistics for Diameter at Breast Height:')
print(f'Mean: {size_mean:.2f}')
print(f'Median: {size_median:.2f}')
print(f'Range: {size_range:.2f}')
print(f'Std-Dev: {size_std_dev:.2f}')

# Plotting DBH box-plot
pbp.plot_boxplot(size, 'DBH')

# Print TAB stats
print('\nDescriptive Statistics for Total Annual Benefits:')
print(f'Mean: {value_mean:.2f}')
print(f'Median: {value_median:.2f}')
print(f'Range: {value_range:.2f}')
print(f'Std-Dev: {value_std_dev:.2f}')

# Plot TAB box-plot
pbp.plot_boxplot(value, 'TAB')

# Plot TAB & DBH scatter plot
plt.clf() # Clear the current plot so you don't plot over the previous graph
plt.scatter(size, value, 0.75)
plt.xlabel('Diameter at Breast Height')
plt.ylabel('Total Annual Benefits')
plt.title('Total Annual Benefits of Portland Parks Tree Inventory\nby Tree Diameter at Breast Height')
plt.savefig('resources/visualizations/TABxDBH_scatter_plot.png')
plt.show()

# Print the DBH & TAB correlation coefficient
print(f'\nCorrelation coefficient between DBH & TAB: {corr_coef:.2f}')
print(f'\nCorrelation matrix:\n{correlation_matrix}')


