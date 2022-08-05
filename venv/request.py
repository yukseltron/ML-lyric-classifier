import requests
import json

url = 'https://lyrics-classifier-yukseltron.vercel.app/api/'

data = {'lyric': 'baby you can drive my car',}
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r, r.json())
