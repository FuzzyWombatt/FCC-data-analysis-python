import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date']).set_index('date')

# Clean data, using numpy percentile is faster than quantile
df = df[(df.value > np.percentile(df.value, 2.5)) & (df.value < np.percentile(df.value, 97.5))]


def draw_line_plot():
    # Draw line plot
    #test doesn't work by standard usage of matplot lib. must use subplots to avoid errors
    fig, ax1 = plt.subplots(figsize=(10,5))
    ax1.plot(df.value, color='r')
    ax1.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    #must use copy function to not modify original data
    df_bar = df.copy()
    df_bar['month'] = df.index.month
    df_bar['year'] = df.index.year

    # Draw bar plot
    fig = df_bar.groupby(['year', 'month'])['value'].mean().unstack().plot.bar(figsize=(7,7), ylabel='Average Page Views', xlabel='Years', legend=True).figure
    #not fig.legend....plt.legend
    plt.legend(['January','February','March','April','May','June','July','August','September','October','November','December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    

    # Draw box plots (using Seaborn)
    #single axis multiplot figure. only along x axis
    fig, ax = plt.subplots(figsize=(15,5), nrows=1, ncols=2)
    #first plot in array ax
    ax[0] = sns.boxplot(x=df_box['year'], y=df_box['value'], ax=ax[0])

    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    ax[1] = sns.boxplot(x=df_box['month'], y=df_box['value'], ax=ax[1], order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    #second graph labels
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
