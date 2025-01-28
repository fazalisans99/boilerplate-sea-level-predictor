import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    years = data['Year']
    sea_levels = data['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(years, sea_levels, color='blue', label='Original Data')

    # Create first line of best fit
    regression_all = linregress(years, sea_levels)
    x_pred_all = pd.Series(range(1880, 2051))  # Predict from 1880 to 2050
    y_pred_all = regression_all.slope * x_pred_all + regression_all.intercept
    plt.plot(x_pred_all, y_pred_all, color='red', label='Best Fit Line (All Data)')

    # Create second line of best fit
    recent_data = data[data['Year'] >= 2000]  # Filter data from 2000 onwards
    regression_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))  # Predict from 2000 to 2050
    y_pred_recent = regression_recent.slope * x_pred_recent + regression_recent.intercept
    plt.plot(x_pred_recent, y_pred_recent, color='green', label='Best Fit Line (2000 onwards)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()