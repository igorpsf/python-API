import requests
import pprint
try:
    import json
except ImportError:
    print("No json module")

# GET /users/:username

r = requests.get("https://api.github.com/users/igor-qa")
print(r.status_code)
print(r.headers)
print(r.history)
print(r.reason)
print(r.url)
print(r.content)
print(r.text)

pprint.pprint(r.json())
r = r.json()
#print(r["created_at"])
#print(r["location"])
# json
''' 

json.dumps(a) - returns a string representing a json object from an object.
json.loads(‘{“page”: 2, ...}’) - returns an object from a string representing a json object.


'''
