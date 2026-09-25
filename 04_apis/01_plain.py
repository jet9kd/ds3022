import httpx
import json

USER = "schacon"
URL = "https://api.github.com/users/{user}/events/public"

response = httpx.get(URL.format(user=USER))

data = response.json()

#print(json.dumps(data, indent=2))

for item in data:
  print(item["repo"]["name"], " - ", item["type"])

