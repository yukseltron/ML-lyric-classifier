import requests
import json

url = 'http://0.0.0.0:5000/api/'

data = [["baby you can drive my car"]]
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, json={'lyric':data,}, headers=headers)
print(r, r.json())
