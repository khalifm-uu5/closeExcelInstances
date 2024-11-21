import requests
import pandas as pd

# URLs for the FastForex API requests
url_currencies = 'https://api.fastforex.io/currencies?api_key=bfae1b22ba-d09e05af83-sn8xgx'
url_rates = 'https://api.fastforex.io/fetch-all?api_key=bfae1b22ba-d09e05af83-sn8xgx'

# Fetch currencies data
response_currencies = requests.get(url_currencies)

# Fetch exchange rates data
response_rates = requests.get(url_rates)

# Initialize dictionaries to store data
currencies_data = {}
exchange_rates_data = {}
updated_date = "N/A"
base_currency = "N/A"

# Check if currencies API call was successful
if response_currencies.status_code == 200:
    currencies_response = response_currencies.json()
    if 'currencies' in currencies_response:
        currencies_data = currencies_response['currencies']

# Check if exchange rates API call was successful
if response_rates.status_code == 200:
    rates_response = response_rates.json()
    exchange_rates_data = rates_response.get('results', {})
    updated_date = rates_response.get('updated', 'N/A')
    base_currency = rates_response.get('base', 'N/A')

# Combine data into a list of dictionaries for the DataFrame
combined_data = []
for abbreviation, currency_name in currencies_data.items():
    exchange_rate = exchange_rates_data.get(abbreviation, "N/A")  # Get exchange rate or "N/A" if missing
    combined_data.append({
        "Abbreviation": abbreviation,
        "Currency Name": currency_name,
        "Exchange Rate": exchange_rate
    })

# Create a DataFrame
df = pd.DataFrame(combined_data)

# Display the DataFrame
print("\nCombined Currency Table:")
print(df)

# Optional: Add metadata as context
print("\nBase Currency:", base_currency)
print("Last Updated:", updated_date)
