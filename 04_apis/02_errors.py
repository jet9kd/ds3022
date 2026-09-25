import httpx
import json

USER = "schacon"
URL = "https://api.github.com/users/{user}/events/public"

try:
  response = httpx.get(URL.format(user=USER))
  response.raise_for_status()
  data = response.json()

  #print(json.dumps(data, indent=2))

  for item in data:
    print(item["repo"]["name"], " - ", item["type"])

except httpx.HTTPError as e:
  print(e)

