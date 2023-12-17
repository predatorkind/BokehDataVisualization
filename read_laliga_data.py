import pandas as pd

s_15_16 = pd.read_csv('Data/season-1516_csv.csv', parse_dates=['Date'], date_format='%d/%m/%y')
s_16_17 = pd.read_csv('Data/season-1617_csv.csv', parse_dates=['Date'], date_format='%d/%m/%y')
s_17_18 = pd.read_csv('Data/season-1718_csv.csv', parse_dates=['Date'], date_format='%d/%m/%y')
s_18_19 = pd.read_csv('Data/season-1819_csv.csv', parse_dates=['Date'], date_format='%d/%m/%Y')

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# calculate points obtain depending on match result
s_15_16['HomePoints'] = s_15_16['FTR'].apply(lambda x: 3 if x == 'H' else 1 if x == 'D' else 0)
s_15_16['AwayPoints'] = s_15_16['FTR'].apply(lambda x: 3 if x == 'A' else 1 if x == 'D' else 0)
s_16_17['HomePoints'] = s_16_17['FTR'].apply(lambda x: 3 if x == 'H' else 1 if x == 'D' else 0)
s_16_17['AwayPoints'] = s_16_17['FTR'].apply(lambda x: 3 if x == 'A' else 1 if x == 'D' else 0)
s_17_18['HomePoints'] = s_17_18['FTR'].apply(lambda x: 3 if x == 'H' else 1 if x == 'D' else 0)
s_17_18['AwayPoints'] = s_17_18['FTR'].apply(lambda x: 3 if x == 'A' else 1 if x == 'D' else 0)
s_18_19['HomePoints'] = s_18_19['FTR'].apply(lambda x: 3 if x == 'H' else 1 if x == 'D' else 0)
s_18_19['AwayPoints'] = s_18_19['FTR'].apply(lambda x: 3 if x == 'A' else 1 if x == 'D' else 0)

# get Real Madrid games and points accumulated over time in season 15/16
real_games1516 = s_15_16.loc[(s_15_16['HomeTeam'] == 'Real Madrid') | (s_15_16['AwayTeam'] == 'Real Madrid'),
['Date', 'HomeTeam', 'AwayTeam', 'HomePoints', 'AwayPoints']]
real_games1516['RealPoints'] = real_games1516.apply(lambda row: row['HomePoints'] if row['HomeTeam'] == 'Real Madrid' else
row['AwayPoints'], axis=1).cumsum()

# get Barcelona games and points accumulated over time in season 15/16
barca_games1516 = s_15_16.loc[(s_15_16['HomeTeam'] == 'Barcelona') | (s_15_16['AwayTeam'] == 'Barcelona'),
['Date', 'HomeTeam', 'AwayTeam', 'HomePoints', 'AwayPoints']]

barca_games1516['BarcaPoints'] = barca_games1516.apply(lambda row: row['HomePoints'] if row['HomeTeam'] == 'Barcelona' else
row['AwayPoints'], axis=1).cumsum()

# get Real Madrid games and points accumulated over time in season 16/17
real_games1617 = s_16_17.loc[(s_16_17['HomeTeam'] == 'Real Madrid') | (s_16_17['AwayTeam'] == 'Real Madrid'),
['Date', 'HomeTeam', 'AwayTeam', 'HomePoints', 'AwayPoints']]
real_games1617['RealPoints'] = real_games1617.apply(lambda row: row['HomePoints'] if row['HomeTeam'] == 'Real Madrid' else
row['AwayPoints'], axis=1).cumsum()

# get Barcelona games and points accumulated over time in season 16/17
barca_games1617 = s_16_17.loc[(s_16_17['HomeTeam'] == 'Barcelona') | (s_16_17['AwayTeam'] == 'Barcelona'),
['Date', 'HomeTeam', 'AwayTeam', 'HomePoints', 'AwayPoints']]

barca_games1617['BarcaPoints'] = barca_games1617.apply(lambda row: row['HomePoints'] if row['HomeTeam'] == 'Barcelona' else
row['AwayPoints'], axis=1).cumsum()

# get Real Madrid games and points accumulated over time in season 17/18
real_games1718 = s_17_18.loc[(s_17_18['HomeTeam'] == 'Real Madrid') | (s_17_18['AwayTeam'] == 'Real Madrid'),
['Date', 'HomeTeam', 'AwayTeam', 'HomePoints', 'AwayPoints']]
real_games1718['RealPoints'] = real_games1718.apply(lambda row: row['HomePoints'] if row['HomeTeam'] == 'Real Madrid' else
row['AwayPoints'], axis=1).cumsum()

# get Barcelona games and points accumulated over time in season 17/18
barca_games1718 = s_17_18.loc[(s_17_18['HomeTeam'] == 'Barcelona') | (s_17_18['AwayTeam'] == 'Barcelona'),
['Date', 'HomeTeam', 'AwayTeam', 'HomePoints', 'AwayPoints']]

barca_games1718['BarcaPoints'] = barca_games1718.apply(lambda row: row['HomePoints'] if row['HomeTeam'] == 'Barcelona' else
row['AwayPoints'], axis=1).cumsum()

# get Real Madrid games and points accumulated over time in season 18/19
real_games1819 = s_18_19.loc[(s_18_19['HomeTeam'] == 'Real Madrid') | (s_18_19['AwayTeam'] == 'Real Madrid'),
['Date', 'HomeTeam', 'AwayTeam', 'HomePoints', 'AwayPoints']]
real_games1819['RealPoints'] = real_games1819.apply(lambda row: row['HomePoints'] if row['HomeTeam'] == 'Real Madrid' else
row['AwayPoints'], axis=1).cumsum()

# get Barcelona games and points accumulated over time in season 18/19
barca_games1819 = s_18_19.loc[(s_18_19['HomeTeam'] == 'Barcelona') | (s_18_19['AwayTeam'] == 'Barcelona'),
['Date', 'HomeTeam', 'AwayTeam', 'HomePoints', 'AwayPoints']]

barca_games1819['BarcaPoints'] = barca_games1819.apply(lambda row: row['HomePoints'] if row['HomeTeam'] == 'Barcelona' else
row['AwayPoints'], axis=1).cumsum()

goals_15_16 = s_15_16.loc[:, ['Date', 'FTHG', 'FTAG']].groupby(['Date']).sum().reset_index()
goals_16_17 = s_16_17.loc[:, ['Date', 'FTHG', 'FTAG']].groupby(['Date']).sum()
goals_17_18 = s_17_18.loc[:, ['Date', 'FTHG', 'FTAG']].groupby(['Date']).sum()
goals_18_19 = s_18_19.loc[:, ['Date', 'FTHG', 'FTAG']].groupby(['Date']).sum()
