## [DS-05E] Example - Bay Wheels Data ##

# Importing the data #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
# path = 'Dropbox/ds_course/data/'
rides1 = pd.read_csv(path + 'bay_rides-1.csv.zip')
rides2 = pd.read_csv(path + 'bay_rides-2.csv.zip')
rides3 = pd.read_csv(path + 'bay_rides-3.csv.zip')
rides4 = pd.read_csv(path + 'bay_rides-4.csv.zip')
rides5 = pd.read_csv(path + 'bay_rides-5.csv.zip')
rides = pd.concat([rides1, rides2, rides3, rides4, rides5])

# Exploring the data #
rides.info()
rides.head()

# Q1. Add a column with the hour #
rides['hour'] = rides['start_time'].str[:-6] + ':00:00'
rides.head()
rides['hour'] = rides['hour'].astype('datetime64[ns]')
rides.info()

# Q2. Aggregate to hourly data #
rides['casual'] = rides['user_type'] == 'casual'
rides['member'] = rides['user_type'] == 'member'
rides = rides.drop(columns=['bike_type', 'user_type', 'start_time', 'start_station_id', 'end_time', 'end_station_id'])
df = rides[['hour', 'casual', 'member']].groupby(by='hour').sum()
df.head()
df.index

# Q3. Time trend #
df.index.name = None
df['total'] = df['member'] + df['casual']
df['total'].plot(figsize=(8,5), title='Figure 1. Hourly total demand', color='black', linewidth=1);
df['total'].resample('D').mean().plot(figsize=(8,5), title='Figure 2. Daily total demand', 
	color='black', linewidth=1);
df['total'].resample('W').mean().plot(figsize=(8,5), title='Figure 3. Weekly total demand',
	color='black', linewidth=1);
df['total'].resample('M').mean().plot(figsize=(8,5), title='Figure 4. Monthly total demand', 
	color='black', linewidth=1);
df['casual'].resample('M').mean().plot(figsize=(8,5), title="Figure 5. Casuals' monthly total demand", 
	color='black', linewidth=1);
df['member'].resample('M').mean().plot(figsize=(8,5), title="Figure 6. Members' monthly total demand", 
	color='black', linewidth=1);

# Q4. Intraday variation #
df['hour'] = df.index.hour
df.head()
df[['casual', 'hour']].groupby('hour').mean().round(1)
df[['casual', 'hour']].groupby('hour').mean().plot.bar(figsize=(7,5),
	title="Figure 7. Intraday variation of casuals' average demand", color='gray', legend=False);
df[['member', 'hour']].groupby('hour').mean().plot.bar(figsize=(7,5),
	title="Figure 8. Intraday variation of members' average demand", color='gray', legend=False);
df[['casual', 'member', 'hour']].groupby('hour').mean().plot.bar(figsize=(7,5),
	title='Figure 9. Intraday variation of average demand', color=['0.4', '0.7'], stacked=True);

# Q5. Intraweek variation #
df['weekday'] = df.index.weekday
df[['casual', 'member', 'weekday']].groupby('weekday').mean().plot.bar(figsize=(7,5),
	title= 'Figure 10. Intraweek variation of total demand', color=['0.4', '0.7'], stacked=True);

# Q6. Monthly seasonality #
df['month'] = df.index.month
df[['casual', 'member', 'month']].groupby('month').mean().round(1)
df[['total', 'month']].groupby('month').mean().plot(figsize=(8,5), 
    title='Figure 11. Monthly seasonality', color='black', linewidth=1, legend=False);
