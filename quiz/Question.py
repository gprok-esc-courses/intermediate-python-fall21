
class Question:
    def __init__(self):
        self.question = ''
        self.answer = ''
        self.wrong_answers = []
        self.category = ''
        self.difficulty = ''

    def display(self):
        print("Q: " + self.question)
        print("1. " + self.answer)
        print("2. " + self.wrong_answers[0])
        print("3. " + self.wrong_answers[1])
        print("4. " + self.wrong_answers[2])
        print("Choose: ")

    def check_answer(self, ans_no):
        if ans_no == 1:
            return True
        else:
            return False