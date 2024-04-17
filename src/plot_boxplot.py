import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_boxplot(data, variable_name):
    '''
    Create a boxplot given a list of data points and the name of the variable.
    
    Parameters:
        data (list or pandas.Series): List of data points
        variable_name (str): Name of the variable
    '''
    # Create a boxplot
    plt.figure(figsize=(6, 6))
    sns.boxplot(y=data, color='skyblue')
    plt.ylabel(variable_name)
    plt.title(f'Boxplot of {variable_name}')
    plt.savefig(f'resources/visualizations/{variable_name}_box_plot.png')
    plt.show()

    # Print out the values used to make the boxplot
    print(f'\nBoxplot values for {variable_name}:')
    print('Minimum:', min(data))
    print('(Q1) 25th Percentile:', np.percentile(data, 25))
    print('(Q2) Median:', np.median(data))
    print('(Q3) 75th Percentile:', np.percentile(data, 75))
    print('Maximum:', max(data))