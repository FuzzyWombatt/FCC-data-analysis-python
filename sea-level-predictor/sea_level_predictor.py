import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,5))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    reg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    #create a range array that covers to the year 2050 for calculation
    x_fit1 = np.arange(start=1880, stop=2051)
    y_fit1 = (reg1.slope*x_fit1)+reg1.intercept
    plt.plot(x_fit1,y_fit1, color='r')

    # Create second line of best fit
    df_fit = df[df['Year']>=2000]
    reg2 = linregress(df_fit['Year'], df_fit['CSIRO Adjusted Sea Level'])
    x_fit2 = np.arange(start=2000, stop=2051)
    y_fit2 = (reg2.slope*x_fit2)+reg2.intercept
    plt.plot(x_fit2,y_fit2, color='g')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()