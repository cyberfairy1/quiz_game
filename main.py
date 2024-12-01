from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list to hold Question objects
question_bank = []

# Convert question data into Question objects
for question_entry in question_data:
    text = question_entry["question"]  # Extract the question text
    answer = question_entry["correct_answer"]  # Extract the correct answer
    question_object = Question(text, answer)  # Create a new Question object
    question_bank.append(question_object)  # Add it to the question bank

# Initialize the quiz
quiz= QuizBrain(question_bank)

# Loop through all questions in the quiz
while quiz.has_more_questions():  
    quiz.ask_next_question()

# Display the final score
print("\nCongratulations, you've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.current_question_index}")
