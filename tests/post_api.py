import json
import requests


url = 'http://localhost:5000/api/'
data = json.dumps({'name': 'mituba'})

result = requests.post(url, data, headers={'Content-Type': 'application/json'})

print(result.text)
