import requests

s = requests.Session()
r = requests.get('https://api.github.com/repos/psf/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')

if r.status_code == requests.codes.ok:
    print(r.headers['content-type'])
    
commit_data = r.json()

print(commit_data.keys())
print(commit_data['committer'])
print(commit_data['message'])