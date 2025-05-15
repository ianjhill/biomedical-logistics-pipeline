import requests
import json
import pandas as pd

# Step 1: Define the API endpoint
url = "https://dummyjson.com/products"

# Optional: add pagination support (we’ll fetch 100 products max)
params = {
    "limit": 100,
    "skip": 0
}

# Make the GET request
response = requests.get(url, params=params)

# Check status and parse JSON
if response.status_code == 200:
    data = response.json()
    products = data['products']  # Get the list of product dicts

    # Load into a pandas DataFrame
    df = pd.DataFrame(products)

    # Optional: Preview and save
    print(df.head())
    df.to_csv("raw_inventory_data.csv", index=False)

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
