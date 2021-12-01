from quiz.DBConnection import DBConnection
from quiz.Question import Question
from quiz.User import User
import json
import requests

class Quiz:
    def __init__(self):
        self.questions = []
        self.user = User()
        self.score = 0
        self.current_question = 0

    def start(self):
        self.user.get_username()
        self.user.check_username()
        if self.user.is_valid:
            self.get_quiz()
            self.play()
            self.display_score()
            self.save_score()
        else:
            print("Invalid user.")

    def get_quiz(self):
        # Go to API and get 10 questions
        url = 'https://opentdb.com/api.php?amount=10&type=multiple'
        response = requests.get(url)
        data = json.loads(response.text)
        questions = data['results']
        for question in questions:
            # print("Question : ", question['question'])
            q = Question()
            q.answer = question['correct_answer']
            q.question = question['question']
            q.wrong_answers = question['incorrect_answers']
            q.category = question['category']
            q.difficulty = question['difficulty']
            self.questions.append(q)

    def play(self):
        for question in self.questions:
            question.display()
            answer = int(input())
            if question.check_answer(answer):
                self.score += 1

    def display_score(self):
        print("SCORE: " + str(self.score) + "/10")

    def save_score(self):
        db = DBConnection()
        db.save_score(self.user.id, self.score)


if __name__ == '__main__':
    quiz = Quiz()
    quiz.start()
