import pandas as pd

url = 'https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv'
df = pd.read_csv(url)

num_rows = df.shape[0]  # Number of rows
num_cols = df.shape[1]  # Number of columns
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)

data_types = df.dtypes  # Data types of columns
print("Data types of columns:")
print(data_types)

df.info()  # Provides a summary of the DataFrame, including data types and memory usage
df.describe()  # Provides summary statistics of the numerical columns

unique_location_count = df['location'].nunique()
print("Count of unique values in 'location' column:", unique_location_count)

continent_max_frequency = df['continent'].value_counts().idxmax()
print("Continent with maximum frequency:", continent_max_frequency)

max_total_cases = df['total_cases'].max()
mean_total_cases = df['total_cases'].mean()
print("Maximum value in 'total_cases':", max_total_cases)
print("Mean value in 'total_cases':", mean_total_cases)

quartiles = df['total_deaths'].quantile([0.25, 0.5, 0.75])
print("25th Quartile value in 'total_deaths':", quartiles[0.25])
print("50th Quartile (Median) value in 'total_deaths':", quartiles[0.5])
print("75th Quartile value in 'total_deaths':", quartiles[0.75])

continent_max_hdi = df.loc[df['human_development_index'].idxmax(), 'continent']
print("Continent with maximum 'human_development_index':", continent_max_hdi)

continent_min_gdp = df.loc[df['gdp_per_capita'].idxmin(), 'continent']
print("Continent with minimum 'gdp_per_capita':", continent_min_gdp)

df = df[['continent', 'location', 'date', 'total_cases', 'total_deaths', 'gdp_per_capita', 'human_development_index']]

df = df.drop_duplicates()

missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

df = df.dropna(subset=['continent'])

df = df.fillna(0)

df['date'] = pd.to_datetime(df['date'])

df['month'] = df['date'].dt.month

df_groupby = df.groupby('continent').max()

df_groupby = df.groupby('continent').max().reset_index()

df['total_deaths_to_total_cases'] = df['total_deaths'] / df['total_cases']

import seaborn as sns
import matplotlib.pyplot as plt

sns.displot(df['gdp_per_capita'])
plt.show()

plt.scatter(df['gdp_per_capita'], df['total_cases'])
plt.xlabel('GDP per Capita')
plt.ylabel('Total Cases')
plt.title('Scatter Plot: Total Cases vs. GDP per Capita')
plt.show()

sns.pairplot(df_groupby)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='continent', y='total_cases', data=df)
plt.xlabel('Continent')
plt.ylabel('Total Cases')
plt.title('Bar Plot: Total Cases by Continent')
plt.show()

df_groupby.to_csv('D://vaishali//python//assignments//to//save//df_groupby.csv', index=False)
