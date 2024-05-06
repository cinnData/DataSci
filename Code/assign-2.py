## Assignment 2 ##

# Importing the data  #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
rides1 = pd.read_csv(path + 'bay_rides-1.csv.zip')
rides2 = pd.read_csv(path + 'bay_rides-2.csv.zip')
rides3 = pd.read_csv(path + 'bay_rides-3.csv.zip')
rides4 = pd.read_csv(path + 'bay_rides-4.csv.zip')
rides5 = pd.read_csv(path + 'bay_rides-5.csv.zip')
rides = pd.concat([rides1, rides2, rides3, rides4, rides5])

# # Q1. Are classic bikes lagging behind electric bikes? #
rides['hour'] = rides['start_time'].str[:-6] + ':00:00'
rides['hour'] = rides['hour'].astype('datetime64[ns]')
rides['electric'] = (rides['bike_type'] == 'electric')
rides['classic'] = (rides['bike_type'] == 'classic')
df = rides[['hour', 'electric', 'classic']].groupby(by='hour').sum()
df
df.index.name = None
df['electric'].resample('M').mean().plot(figsize=(8,5), title="Figure 1. Monthly total demand",
	color='black', linewidth=1, legend=True)
df['classic'].resample('M').mean().plot(figsize=(8,5), title="Figure 1. Monthly total demand",
	color='black', linewidth=1, linestyle='--', legend=True);

# Q2. Dockless bike share #
rides['start_dockless'] = rides['start_station_id'].isna()
rides['end_dockless'] = rides['end_station_id'].isna()
pd.crosstab(rides['start_dockless'], rides['electric'])
pd.crosstab(rides['end_dockless'], rides['electric'])
pd.crosstab(rides['start_dockless'], rides['end_dockless'])
electric = rides[rides['bike_type'] == 'electric']
pd.crosstab(electric['start_dockless'], electric['end_dockless'])
df = electric[['hour', 'start_dockless', 'end_dockless']].groupby(by='hour').mean()
df
df['start_dockless'].resample('M').mean().plot(figsize=(8,5), title='Figure 2. Monthly demand of dockless bikes',
	color='black', linewidth=1, legend=True)
df['end_dockless'].resample('M').mean().plot(figsize=(8,5),
	color='black', linewidth=1, linestyle='--', legend=True);

# Q3. Which are the top-10 starting stations? Are they the same as the top-10 ending stations? #
rides['start_station_id'].value_counts().head(10)
rides['end_station_id'].value_counts().head(10)

# Q4. Stations with very low activity #
rides['start_station_id'].value_counts().tail(10)
rides['end_station_id'].value_counts().tail(10)
