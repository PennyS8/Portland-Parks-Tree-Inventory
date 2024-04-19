import matplotlib.pyplot as plt
import numpy as np
import plot_boxplot as pbp

def calculate_descriptive_stats(data):

    mean = np.mean(data)
    median = np.median(data)
    data_range = np.ptp(data)
    std_dev = np.std(data)

    return mean, median, data_range, std_dev

def analyze_data(data_dict):
    '''
    Analyzes the provided data related to tree inventory.

    Parameters:
    - data_dict (dict): Dictionary containing columns of data from the tree inventory CSV file.

    This function calculates descriptive statistics for each column in the data dictionary,
    including mean, median, range, and standard deviation. It also computes the correlation
    matrix among all the columns, and generates visualizations such as box plots and scatter plots.

    Prints:
    - Descriptive statistics for each column.
    - Box plots for each column.
    - Scatter plot showing the relationship between DBH & TAB.
    - Correlation matrix among all columns.
    '''
    for var_name, var_data in data_dict.items():
        # Calculate descriptive statistics for the current variable
        mean, median, data_range, std_dev = calculate_descriptive_stats(var_data)

        # Print descriptive statistics
        print(f'\nDescriptive Statistics for {var_name}:')
        print(f'Mean: {mean:.2f}')
        print(f'Median: {median:.2f}')
        print(f'Range: {data_range:.2f}')
        print(f'Std-Dev: {std_dev:.2f}')

        # Plotting DBH box-plot
        pbp.plot_boxplot(var_data, var_name)

    # Compute correlation matrix among all columns
    correlation_matrix = np.corrcoef([var_data for var_data in data_dict.values()])
    
    # Print correlation matrix
    print('\nCorrelation matrix:')
    print(correlation_matrix)

    # Show scatter plot for Diameter at Breast Height (DBH) and Total Annual Benefits (TAB)
    plt.scatter(data_dict['DBH'], data_dict['Total_Annual_Benefits'], 0.75)
    plt.xlabel('Diameter at Breast Height')
    plt.ylabel('Total Annual Benefits')
    plt.title('Total Annual Benefits vs. Diameter at Breast Height')
    plt.savefig('resources/visualizations/TABxDBH_scatter_plot.png')
    # plt.show()
