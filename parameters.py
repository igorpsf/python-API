import requests
import json

# GET
payload = {"key1":"value1", "key2":"value2"}
r = requests.get("https://httpbin.org/get", params=payload)
print("URL:", r.url)
print("ENCODING:", r.encoding)
print("STATUS_CODE:", r.status_code)
print("HEADERS:", r.headers)
print("TEXT:", r.text)
print("CONTENT:", r.content)
print("JSON:", r.json)

# POST
r = requests.post('https://httpbin.org/post', data = {'name':'Joe'})

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)

# GET Currency Exchange Data

url = 'https://api.exchangeratesapi.io/2018-01-15'
r = requests.get(url, params={'base':'USD'})
print(r.text)

# Decoding JSON data

rates_json = json.loads(r.text)['rates']
print(rates_json)
print(rates_json['GBP'])
gbp = float(rates_json['GBP'])
print('200USD = ', str(gbp * 200), 'GBP')