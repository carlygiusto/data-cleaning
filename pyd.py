import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv('Influenza_Laboratory-Confirmed_Cases_By_County__Beginning_2009-10_Season.csv')

#dropping unecessary columns
to_drop = ['FIPS', 'Region', 'County Centroid',]
df.drop(to_drop, inplace=True, axis=1)


#dropping rows with flu incidences of 0
df = df[~df['Count'].isin(['0'])]

df['Season'].is_unique
df = df.set_index('Season')
print(df.loc['2011-2012'])

print('----')

df.loc[df['Count'] < 200, 'County'] = 'Other' # Represent only large counties
fig = px.pie(df, values='Count', names='County', title='Incidences of Influenza NY 2011-2012')
fig.show()


