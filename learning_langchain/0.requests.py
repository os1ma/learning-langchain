import requests
import os
import json

url = 'https://api.openai.com/v1/completions'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + os.environ['OPENAI_API_KEY']
}
data = {
    'model': 'text-davinci-003',
    'prompt': 'hello!',
    'temperature': 0,
}

response = requests.post(url=url, headers=headers, json=data)
print(json.dumps(response.json(), indent=2))
