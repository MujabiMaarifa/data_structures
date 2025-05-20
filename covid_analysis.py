import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Covid 19 data analysis\n\n")

#fetch data from the csv file in covid folder
data = pd.read_csv('covid/covid_19_clean_complete.csv')
print(data.head())

#check the columns of the imported data
print("\n\nThe columns in the piece of data fetched..\n")
print(data.columns)

#identify the missing columns
print("\n\nEmpty fields in the fetched data...\n")
print(data.isnull().sum())

#filtering data based on the required countries
print("\n\nFiltered data based on the countries..\n")
countries = ['Kenya', 'USA', 'India']  
filtered_data = data[data['Country/Region'].isin(countries)]
print(filtered_data)

#cleaning data
print("\n\nEmpty columns deleted and dropped successfully...\n")
# print(filtered_data.isnull().sum())
critical_columns = ['Date', 'Recovered', 'Deaths', 'Active']
clean_data = filtered_data.dropna(subset=critical_columns)
print(clean_data)
# print(clean_data.isnull().sum()) --> checking the deleted empty null fields


#Convert date column to datetime: pd.to_datetime()
data['Date'] = pd.to_datetime(data['Date'])
print(data['Date'])


"""EDA"""
#sort values
print("\n\nThis is sorted data in order\n")
sorted_data = clean_data.sort_values(['Country/Region', 'Date'])
print(sorted_data)

#visualizations
plt.figure(figsize=(12,6))
for country in countries:
    country_data = clean_data[clean_data['Country/Region'] == country]
    plt.plot(country_data['Date'], country_data['Long'], label=country)

plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()

#total deaths over time
plt.figure(figsize=(12,6))
for country in countries:
    country_data = clean_data[clean_data['Country/Region'] == country]
    plt.plot(country_data['Date'], country_data['Deaths'], label=country)

plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.show()

#comparing new cases
clean_data['Daily_new_cases'] = clean_data.groupby('Country/Region')['Active'].diff().fillna(0)

plt.figure(figsize=(12,6))
for country in countries:
    country_data = clean_data[clean_data['Country/Region'] == country]
    plt.plot(country_data['Date'], country_data['daily_new_cases'], label=country)

plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('Daily New Cases')
plt.legend()
plt.show()

#death rate
clean_data['death_rate'] = clean_data['Deaths'] / clean_data['Active']
print(clean_data['death_rate'])


