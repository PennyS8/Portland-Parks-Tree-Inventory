import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the current directory of the script
parnet_dir = os.path.dirname(os.path.dirname(__file__))

# Construct the full path to the CSV file
csv_file_path = os.path.join(parnet_dir, 'resources', 'Parks_Tree_Inventory.csv')

# Check if the file exists
if os.path.exists(csv_file_path):
    # Read the CSV file into a DataFrame
    trees = pd.read_csv(csv_file_path)
    # Now you can work with the 'trees' DataFrame
else:
    print("Error: CSV file not found at", csv_file_path)

size = [float(i) for i in trees['DBH']]
value = [float(j) for j in trees['Total_Annual_Benefits']]

plt.clf() # Clear the current plot so you don't plot over the previous graph
plt.scatter(size, value, 0.75)
plt.xlabel('Diameter at Breast Height')
plt.ylabel('Total Annual Benefits')
plt.title('Total Annual Benefits of Portland Parks Tree Inventory\nby Tree Diameter at Breast Height')
plt.savefig('resources/TABxDBH_scatter_plot.png')
plt.show() # NOTE: Opens an interactive graph
