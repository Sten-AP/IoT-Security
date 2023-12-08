import requests

s = requests.Session()

url = "https://bol.com"

response = s.get(url)
for header in response.headers:
    print(f"{header}: {response.headers[header]}\n")
