import requests
res = requests.get('http://localhost:9200?pretty')
print(res.content)