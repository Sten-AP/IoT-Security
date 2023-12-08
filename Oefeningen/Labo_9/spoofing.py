import requests

s = requests.Session()

url = "https://bol.com"
referer = "Dit is iets."

headers = {'Referer': referer}
response = s.get(url, headers=headers)
for header in response.headers:
    print(f"{header}: {response.headers[header]}\n")
