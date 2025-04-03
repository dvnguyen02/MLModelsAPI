import requests
import json

data = {"features": [5,6,7,8]}

url = "http://localhost:5000/predict"  
response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print(f"Prediction: {result['prediction']}")
else:
    print(f"Error: {response.status_code}, {response.text}")