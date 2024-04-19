import pandas as pd
import os
import analysis as ana
import linear_regression as linr
import machine_learning as mach

parnet_dir = os.path.dirname(os.path.dirname(__file__))
csv_file_path = os.path.join(parnet_dir, 'resources', 'Parks_Tree_Inventory.csv')

# If file doesn't exist, then run error and exit program
try:
    # Read the CSV file into a DataFrame
    tree_inv = pd.read_csv(csv_file_path)
except:
    SystemExit('Error: CSV file not found at', csv_file_path)

variables = ['DBH', 'TreeHeight', 'CrownWidthNS', 'Pollution_Removal_oz', 'Stormwater_ft']
label = 'Total_Annual_Benefits'

tree_data = tree_inv.dropna(subset = variables+[label])

data = {}
for var in variables+[label]:
    data[var] = [float(i) for i in tree_data[var]]

# Data analysis
ana.analyze_data(data)

# Linear regression
linr.linear_regression(data)

# Machine learning
mach.machine_learning_plot(data)
