import requests

# GET /users/:username

r = requests.get("https://api.github.com/users/igor-qa")
print(r.status_code)
print(r.headers)
print(r.history)
print(r.reason)
print(r.url)
print(r.content)
print(r.text)
print(r.json())
