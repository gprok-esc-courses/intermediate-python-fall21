import json
import requests

url = 'https://opentdb.com/api.php?amount=1&type=multiple'
response = requests.get(url)
data = json.loads(response.text)
question = data['results'][0]
print(question['correct_answer'])

print("QUESTION")
print("Question: ", question['question'])
print("Correct: ", question['correct_answer'])
print("Incorrect Answers:")
for a in question['incorrect_answers']:
    print(a)