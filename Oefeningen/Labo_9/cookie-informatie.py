import sys
import requests

s = requests.Session()
url = "https://bol.com"

response = s.get(url)
for cookie in response.cookies:
    print(cookie)
print()

cookie = "BE"
cookie = {'locale': cookie}
response = s.get(url, cookies=cookie)
for cookie in response.cookies:
    print(cookie)