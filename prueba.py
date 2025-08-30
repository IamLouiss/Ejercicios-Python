import requests

url = "https://valorant-api.com/v1/maps"
response = requests.get(url)
data = response.json()

print(data["data"][0]["callouts"])

for i in range(len(data["data"][0]["callouts"])):
  print(data["data"][0]["callouts"][i]["regionName"])

response.close()