import requests
import json

url = 'https://lyrics-classifier.vercel.app/api/'

data = [["baby you can drive my car"]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)
