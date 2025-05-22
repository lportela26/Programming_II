import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

params = {
    "vs_currency": "usd",
    "days": 30,
    "interval": "daily"
}

response = requests.get(url, params=params)
data = response.json()

prices = data["prices"] 

df = pd.DataFrame(prices, columns=["timestamp", "price"])
df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
df = df[["date", "price"]]

plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["price"], marker="o", linestyle="-")
plt.title("Bitcoin Price (Last 30 Days)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.tight_layout()
plt.show()

