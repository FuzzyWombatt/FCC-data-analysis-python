import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight']/(df['height']/100)**2).apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
#read more into python functional programming. Monads and lambdas need to be learned just in case
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1 )
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1 )

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco', 'active', 'overweight'])
    #print(df_cat)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #total column needed for the count to be done next line without index overflow
    df_cat['total'] = 0
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
    
    
    # Draw the catplot with 'sns.catplot()'
    #need .fig at the end to get correct tests
    fig = sns.catplot(x='variable', y='total', data=df_cat, hue='value',kind='bar', col='cardio').fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    #quantile used over numpy to keep it as an easier logic cleaning
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
    #check out put of cleaning
    #print(df_heat)

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    #use as standard set up for plots now
    fig, ax = plt.subplots(figsize=(15,15))

    # Draw the heatmap with 'sns.heatmap()'
    # fig points to the same thing as ax
    fig = sns.heatmap(corr, mask=mask, cmap="Spectral", annot=True, square=True, vmin=0, vmax=.3, lw=.5, fmt='.1f').figure



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
