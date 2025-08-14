#             # How To Create My Own Classes and Add Attributes
# class User:           #How to create a class
#     def __init__(self, user_id, username): # How to add attribute which are basically variables. You must use the __init__() object initializer
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#
# user_1 = User("001", "Andre") # Here user_1 is the object and User is the class. So we are adding data/variables to our class.
#
# print(user_1.followers)

# Adding Methods to a Class

# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#
#     def follow(self, user): # A method must always have a self parameter as the 1st parameter.
#         user.followers += 1
#         user.following += 1
#
# user_1 = User("001", "Andre")
# user_2 = User("002", "Arwen")
#
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

#### Quiz: OOP Project 2

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_got_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")