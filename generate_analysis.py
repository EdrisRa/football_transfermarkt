import pandas as pd
import sys

# Redirect stdout to a file
sys.stdout = open('analysis_results.txt', 'w')

# Load the data
players_df = pd.read_csv('Data/players.csv')

# Basic Information about the Dataset
print("## Basic Information about the Dataset")
print(f"Dataset shape: {players_df.shape}")
print("\nColumns in the dataset:")
print(players_df.columns.tolist())
print("\nData types:")
print(players_df.dtypes)

# Missing Values Analysis
print("\n## Missing Values Analysis")
missing_values = players_df.isnull().sum()
missing_percentage = (missing_values / len(players_df)) * 100
missing_data = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage': missing_percentage
})
print(missing_data[missing_data['Missing Values'] > 0].sort_values('Percentage', ascending=False))

# Player Market Value Analysis
print("\n## Player Market Value Analysis")
market_value_stats = players_df['market_value_in_eur'].describe()
print("Market Value Statistics:")
print(market_value_stats)

# Top Players by Market Value
print("\n## Top Players by Market Value")
top_players = players_df.nlargest(10, 'market_value_in_eur')
print(top_players[['first_name', 'last_name', 'market_value_in_eur', 'current_club_name']])

# Player Age Analysis
print("\n## Player Age Analysis")
players_df['age'] = (pd.to_datetime('today') - pd.to_datetime(players_df['date_of_birth'])).dt.days / 365.25
print("Age Statistics:")
print(players_df['age'].describe())

# Club Analysis
print("\n## Club Analysis")
club_values = players_df.groupby('current_club_name')['market_value_in_eur'].sum().sort_values(ascending=False).head(10)
print("Top 10 Clubs by Total Player Market Value:")
print(club_values)

# Close the file
sys.stdout.close()