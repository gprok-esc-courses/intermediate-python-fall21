import json
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
data = json.loads(response.text)

for blogpost in data:
    print(blogpost['title'])

