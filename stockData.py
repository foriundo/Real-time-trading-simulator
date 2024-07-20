import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = 'LQEY50XE8FGG6W8Z'
symbol = 'AAPL'
function = 'TIME_SERIES_DAILY'
output_size = 'compact'  # use 'full' for more data

# Construct the API URL
url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&outputsize={output_size}&apikey={api_key}'

# Make the API request
response = requests.get(url)
data = response.json()

# Convert the data to a DataFrame
df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
df = df.astype(float)  # convert data types to float

# Print the DataFrame
print(df.head())

# Save the DataFrame to a CSV file
df.to_csv('stock_data.csv')
