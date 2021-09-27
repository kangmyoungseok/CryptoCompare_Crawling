import requests
import json
import pandas as pd

response = requests.get('https://coincodex.com/apps/coincodex/cache/all_coins.json')
df = pd.read_json(response.text)
df.to_csv("result.csv")
