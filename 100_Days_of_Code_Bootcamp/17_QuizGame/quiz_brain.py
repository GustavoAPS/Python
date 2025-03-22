class QuizBrain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        answer = input(f"Q.{self.question_number+1} {self.question_list[self.question_number].text}(true/false)?\n")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        print(f"Your current score is {self.score}/{self.question_number+1}\n")
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was {correct_answer}")
