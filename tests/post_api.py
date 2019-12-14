import json
import requests
import base64


data = base64.b64encode(b'hello').decode('utf-8')

url = 'http://localhost:5000/api/'
print(data)

data = json.dumps({'data': data, 'speaked_at': '2018-12-31T05:00:30.001000'})

print(data)
result = requests.post(url, data, headers={'Content-Type': 'application/json'})

print(result.text)
