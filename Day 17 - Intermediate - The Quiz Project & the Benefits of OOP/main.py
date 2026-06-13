from data import question_data
from question_model import Question
import quiz_brain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = quiz_brain.QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"Quiz completed\nYour final score was: {quiz.score}/{quiz.question_number}")
