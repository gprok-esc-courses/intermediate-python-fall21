import json
import requests

url = 'https://opentdb.com/api.php?amount=10&type=multiple'
response = requests.get(url)
data = json.loads(response.text)
questions = data['results']

counter = 1
for question in questions:
    print("Question ", counter, ": ", question['question'])
    counter += 1
