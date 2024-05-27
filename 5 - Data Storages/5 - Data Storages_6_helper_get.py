import requests, json

data = requests.get('http://localhost:5000/get_data/')
json_data = data.json()
print(json.dumps(json_data, indent=2))